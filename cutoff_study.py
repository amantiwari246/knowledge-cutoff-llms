"""
Simulation testbed: knowledge-cutoff effects on automatically generated literature reviews.

A synthetic, fast-moving research field is generated (papers, citations, retractions,
preprint/journal versions, vocabulary drift, claims about the best method). Five review
systems are compared on temporal-completeness, stale-claim rate, invalid references,
false research gaps and re-run stability. Ground truth is known by construction.
"""
import json
import numpy as np

SEEDS = list(range(30))
T_NOW = 48          # reference time (months)
T_LATER = 54        # re-run time for the reproducibility test
N_REVIEW = 30       # references per review
K_TOPICS = 6
DRIFT_T = 30        # new vocabulary appears after this month


def ms(x):
    x = np.asarray(x, float)
    return [round(float(x.mean()), 3), round(float(x.std(ddof=1)), 3)]


# ------------------------------------------------------------------ corpus
def make_corpus(seed, horizon=T_LATER):
    r = np.random.RandomState(seed)
    emerge = r.randint(0, 37, K_TOPICS)
    entries, work_id = [], 0
    level = np.zeros(K_TOPICS, int)                 # claimed "best method" counter per topic
    for t in range(horizon):
        for k in range(K_TOPICS):
            if t < emerge[k]:
                continue
            lam = min(1.0 + 0.15 * (t - emerge[k]), 4.0)
            for _ in range(r.poisson(lam)):
                q = r.beta(4, 3)
                rel = r.beta(5, 2)
                auth = float(np.clip(0.5 * q + 0.5 * r.beta(3, 3), 0, 1))
                new_vocab = (t >= DRIFT_T) and (r.rand() < 0.7)
                retracted_at = t + r.uniform(3, 24) if r.rand() < 0.06 else None
                replicable = r.rand() < min(0.55 + 0.45 * q, 1.0)
                if r.rand() < 0.04:
                    level[k] += 1
                w = dict(work=work_id, topic=k, t=float(t), q=q, rel=rel, auth=auth,
                         new_vocab=new_vocab, retracted_at=retracted_at,
                         replicable=replicable, level=int(level[k]),
                         cite_factor=float(r.lognormal(0, 0.4)), preprint=False)
                entries.append(w)
                if r.rand() < 0.30:                  # earlier preprint version, same work
                    p = dict(w)
                    p["t"] = max(0.0, w["t"] - r.uniform(2, 8))
                    p["preprint"] = True
                    entries.append(p)
                work_id += 1
    return entries, emerge


def cites(e, now):
    age = max(now - e["t"], 0.0)
    base = 30 * e["q"] * (1 - np.exp(-age / 18)) * e["cite_factor"]
    return base * (0.3 if e["preprint"] else 1.0)


def retracted_known(e, now):
    return e["retracted_at"] is not None and e["retracted_at"] <= now


# ------------------------------------------------------------------ ground truth
def truth(entries, now):
    valid = [e for e in entries if e["t"] <= now and not e["preprint"]
             and not retracted_known(e, now)]
    for e in valid:
        e["_w"] = e["q"] * e["rel"]
    expected = sorted(valid, key=lambda e: -e["_w"])[:N_REVIEW]
    exp_ids = {e["work"]: e["_w"] for e in expected}
    true_level, n_valid = {}, {}
    for k in range(K_TOPICS):
        vs = [e for e in valid if e["topic"] == k]
        n_valid[k] = len(vs)
        good = [e["level"] for e in vs if e["replicable"]]
        true_level[k] = max(good) if good else None
    return exp_ids, true_level, n_valid


# ------------------------------------------------------------------ systems
def rank(entries, now, system, cutoff, weights=(0.5, 0.2, 0.15, 0.15)):
    pool = [e for e in entries if e["t"] <= now]
    if system == "S0_closed_book":
        pool = [e for e in pool if e["t"] <= cutoff]
    if system == "S4_frozen":
        pool = [e for e in pool if e["t"] <= cutoff]
    if system in ("S4_full", "S4_frozen"):
        know = cutoff if system == "S4_frozen" else now
        pool = [e for e in pool if not retracted_known(e, know)]
        best = {}
        for e in pool:                               # version collapse: keep latest version
            if e["work"] not in best or e["t"] > best[e["work"]]["t"]:
                best[e["work"]] = e
        pool = list(best.values())
    now_eff = cutoff if system in ("S0_closed_book", "S4_frozen") else now
    cs = np.array([cites(e, now_eff) for e in pool]) if pool else np.array([])
    cmax = np.log1p(cs.max()) if len(cs) else 1.0
    scores = []
    a, b, g, d = weights
    for e, c in zip(pool, cs):
        cn = np.log1p(c) / cmax
        vocab_pen = 0.7 if e["new_vocab"] else 1.0
        if system == "S0_closed_book":
            s = e["rel"] + 0.5 * cn
        elif system == "S1_rag_semantic":
            s = e["rel"] * vocab_pen
        elif system == "S2_rag_citation":
            s = e["rel"] * vocab_pen + 0.5 * cn
        elif system in ("S3_time_aware", "S3b_no_temporal_term", "S4_full", "S4_frozen"):
            temp = np.exp(-(now_eff - e["t"]) / 24)
            bb = 0.0 if system == "S3b_no_temporal_term" else b
            s = a * e["rel"] + bb * temp + g * e["auth"] + d * cn   # query expansion: no vocab penalty
        scores.append(s)
    order = np.argsort(scores)[::-1][:N_REVIEW]
    return [pool[i] for i in order]


def report_level(sel, k, system, know=T_NOW):
    ts = [e for e in sel if e["topic"] == k]
    if not ts:
        return None
    if system in ("S0_closed_book", "S1_rag_semantic", "S2_rag_citation"):
        return ts[0]["level"]                                  # top-ranked paper's claim
    if system in ("S3_time_aware", "S3b_no_temporal_term"):
        return max(ts, key=lambda e: e["t"])["level"]          # most recent paper wins
    ok = [e for e in ts if e["q"] >= 0.4 and not retracted_known(e, know)]   # evidence hierarchy
    return max(e["level"] for e in ok) if ok else None


def evaluate(entries, emerge, system, now=T_NOW, cutoff=36):
    exp_ids, true_level, n_valid = truth(entries, now)
    sel = rank(entries, now, system, cutoff)
    got = {e["work"] for e in sel}
    tc = sum(w for i, w in exp_ids.items() if i in got) / sum(exp_ids.values())
    topics = [k for k in range(K_TOPICS) if emerge[k] <= now and true_level[k] is not None]
    know = cutoff if system == "S4_frozen" else now
    stale = np.mean([report_level(sel, k, system, know) != true_level[k] for k in topics])
    seen = {}
    invalid = 0
    for e in sel:
        bad = retracted_known(e, now) or (e["work"] in seen)
        seen[e["work"]] = True
        invalid += bad
    inv_rate = invalid / max(len(sel), 1)
    big = [k for k in topics if n_valid[k] >= 5]
    gaps = [sum(1 for e in sel if e["topic"] == k) < 2 for k in big]
    false_gap = np.mean(gaps) if gaps else 0.0
    return dict(tc=tc, stale=stale, invalid=inv_rate, gap=false_gap, ids=got)


# ------------------------------------------------------------------ experiments
SYSTEMS = ["S0_closed_book", "S1_rag_semantic", "S2_rag_citation",
           "S3b_no_temporal_term", "S3_time_aware", "S4_full"]


def main():
    out = {}
    agg = {s: {"tc": [], "stale": [], "invalid": [], "gap": []} for s in SYSTEMS}
    sweep = {g: {"S0_closed_book": {"tc": [], "stale": []}, "S4_frozen": {"tc": [], "stale": []}}
             for g in (3, 6, 12, 24)}
    repro = {"S1_rag_semantic": [], "S4_full": []}
    vocab = {"semantic_only": [], "with_query_expansion": []}
    for s in SEEDS:
        entries, emerge = make_corpus(s)
        for sysn in SYSTEMS:
            m = evaluate(entries, emerge, sysn)
            for k in agg[sysn]:
                agg[sysn][k].append(m[k])
        for g in sweep:
            for sysn in sweep[g]:
                m = evaluate(entries, emerge, sysn, cutoff=T_NOW - g)
                sweep[g][sysn]["tc"].append(m["tc"])
                sweep[g][sysn]["stale"].append(m["stale"])
        for sysn in repro:                       # live re-run 6 months later vs original
            a = evaluate(entries, emerge, sysn, now=T_NOW)["ids"]
            b = evaluate(entries, emerge, sysn, now=T_LATER)["ids"]
            repro[sysn].append(len(a & b) / len(a | b))
        # vocabulary drift: share of included papers that use new vocabulary
        for name, sysn in (("semantic_only", "S1_rag_semantic"), ("with_query_expansion", "S3_time_aware")):
            sel = rank(entries, T_NOW, sysn, 36)
            pool_new = [e for e in entries if e["t"] <= T_NOW and e["new_vocab"] and not e["preprint"]]
            share_pool = len(pool_new) / max(1, len([e for e in entries if e["t"] <= T_NOW and not e["preprint"]]))
            share_sel = np.mean([e["new_vocab"] for e in sel])
            vocab[name].append(share_sel / share_pool if share_pool else 0)
    out["main"] = {s: {k: ms(v) for k, v in agg[s].items()} for s in SYSTEMS}
    out["cutoff_gap_sweep"] = {str(g): {sn: {k: ms(v) for k, v in d.items()} for sn, d in sweep[g].items()}
                               for g in sweep}
    out["live_rerun_jaccard_6mo"] = {k: ms(v) for k, v in repro.items()}
    out["new_vocab_representation_ratio"] = {k: ms(v) for k, v in vocab.items()}

    # paired difference S4 - S1 on TC and stale
    d_tc = np.array(agg["S4_full"]["tc"]) - np.array(agg["S1_rag_semantic"]["tc"])
    d_st = np.array(agg["S4_full"]["stale"]) - np.array(agg["S1_rag_semantic"]["stale"])
    out["paired_S4_minus_S1"] = {"tc_mean_diff": round(float(d_tc.mean()), 3),
                                 "tc_wins": int((d_tc > 0).sum()),
                                 "stale_mean_diff": round(float(d_st.mean()), 3),
                                 "stale_better": int((d_st < 0).sum()), "n": len(SEEDS)}
    json.dump(out, open("cutoff_results.json", "w"), indent=2)
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
