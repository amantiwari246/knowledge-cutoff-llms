# Datasets and Benchmarks

This section lists datasets and benchmarks relevant to studying knowledge cutoff effects, temporal awareness, outdated information, retrieval-augmented generation (RAG), and factuality in large language models.

## 1. EvolveBench

**Description:**
EvolveBench is a benchmark for evaluating temporal awareness in large language models using evolving knowledge. It evaluates multiple dimensions of temporal competence, including cognition, temporal awareness, trustworthiness, understanding, and reasoning.

**Relevance:**
Useful for evaluating whether an LLM can correctly handle information that changes over time and distinguish temporally aligned from misaligned information.

**Paper:**
Zhu, Z., et al. (2025). *EvolveBench: A Comprehensive Benchmark for Assessing Temporal Awareness in LLMs on Evolving Knowledge.*

**Resources:**

* Paper: https://aclanthology.org/2025.acl-long.788/
* GitHub: https://github.com/zzysjtuiwct/EvolveBench

---

## 2. HoH — How Outdated Information Harms RAG

**Description:**
HoH is a dynamic benchmark designed to evaluate the impact of outdated information on Retrieval-Augmented Generation systems. It contains question-answering data representing the evolution of real-world facts over time.

**Relevance:**
Directly relevant to studying how outdated information can affect retrieval and the generation of literature-review-style answers from changing knowledge sources.

**Paper:**
Ouyang, J., Pan, T., Cheng, M., Yan, R., Luo, Y., Lin, J., & Liu, Q. (2025). *HoH: A Dynamic Benchmark for Evaluating the Impact of Outdated Information on Retrieval-Augmented Generation.*

**Resources:**

* Paper: https://aclanthology.org/2025.acl-long.301/
* GitHub: https://github.com/0russwest0/HoH

---

## 3. Dated Data / Knowledge Cutoff Benchmark

**Description:**
Dated Data investigates the effective knowledge cutoff of large language models. It examines whether the knowledge demonstrated by an LLM actually aligns with the reported cutoff date of its training data.

**Relevance:**
This is directly related to the central research question of this repository: whether an LLM's effective knowledge cutoff differs from its stated or expected cutoff.

**Paper:**
Cheng, J., Marone, M., Weller, O., Lawrie, D., Khashabi, D., & Van Durme, B. (2024). *Dated Data: Tracing Knowledge Cutoffs in Large Language Models.*

**Resources:**

* Paper: https://arxiv.org/abs/2403.12958
* Hugging Face paper page: https://huggingface.co/papers/2403.12958

---

## 4. CRAG — Comprehensive RAG Benchmark

**Description:**
CRAG (Comprehensive RAG Benchmark) is a factual question-answering benchmark designed for evaluating Retrieval-Augmented Generation systems. It includes questions across multiple domains and incorporates different levels of temporal dynamism.

**Relevance:**
CRAG can be used to study whether retrieval systems provide sufficiently current and factually supported information when answering knowledge-intensive questions.

**Resources:**

* GitHub: https://github.com/facebookresearch/CRAG
* Dataset documentation: https://github.com/facebookresearch/CRAG/blob/main/docs/dataset.md

---

## Dataset Selection Rationale

The datasets and benchmarks above cover complementary aspects of the research problem:

| Dataset / Benchmark | Main Focus                  | Relevance to Topic                                     |
| ------------------- | --------------------------- | ------------------------------------------------------ |
| EvolveBench         | Temporal awareness          | Evaluates LLM handling of evolving knowledge           |
| HoH                 | Outdated information in RAG | Measures effects of stale information                  |
| Dated Data          | Effective knowledge cutoff  | Investigates actual vs. reported knowledge cutoffs     |
| CRAG                | Factual RAG evaluation      | Evaluates factuality and retrieval in dynamic settings |

These resources can support experiments involving temporal alignment, knowledge freshness, retrieval quality, factuality, and the reliability of LLM-generated literature reviews.
