# Research References

A curated collection of verified scholarly papers related to knowledge cutoff effects, temporal knowledge, LLM-generated literature reviews, retrieval-augmented generation, citation reliability, continual learning, and research automation.

## Contents

- [Survey and Review Papers](#survey-and-review-papers)
- [Foundational and Methods Papers](#foundational-and-methods-papers)
- [Recent Research and Benchmarks](#recent-research-and-benchmarks)
- [Literature Review and Research Automation](#literature-review-and-research-automation)
- [Temporal Knowledge and Continual Learning](#temporal-knowledge-and-continual-learning)

---

## Survey and Review Papers

### 1. Survey of Hallucination in Natural Language Generation

**Authors:** Ji, Z., Lee, N., Frieske, R., Yu, T., Su, D., Xu, Y., Ishii, E., Bang, Y. J., Madotto, A., & Fung, P.  
**Year:** 2023  
**Venue:** ACM Computing Surveys  
**DOI:** https://doi.org/10.1145/3571730

**Relevance:** Provides a comprehensive survey of hallucination in language generation, including factual inconsistency and unsupported information relevant to reliable literature reviews.

---

### 2. Continual Learning of Large Language Models: A Comprehensive Survey

**Authors:** Shi, H., Xu, Z., Wang, H., Qin, W., Wang, W., Wang, Y., Wang, Z., Ebrahimi, S., & Wang, H.  
**Year:** 2024  
**Venue:** arXiv  
**DOI:** https://doi.org/10.48550/arXiv.2404.16789

**Relevance:** Reviews continual-learning approaches for keeping large language models updated with evolving knowledge.

---

### 3. Continual Learning for Large Language Models: A Survey

**Authors:** Wu, T., Luo, L., Li, Y.-F., Pan, S., Vu, T.-T., & Haffari, G.  
**Year:** 2024  
**Venue:** arXiv  
**DOI:** https://doi.org/10.48550/arXiv.2402.01364

**Relevance:** Surveys methods for continual learning in LLMs and discusses challenges associated with updating model knowledge over time.

---

### 4. Generative Artificial Intelligence for Literature Reviews

**Authors:** Wagner, G., Prester, J., Mousavi, R., Lukyanenko, R., & Paré, G.  
**Year:** 2026  
**Venue:** Journal of Information Technology  
**DOI:** https://doi.org/10.1177/02683962261425675

**Relevance:** Examines the use of generative AI for literature-review activities and the opportunities and limitations of these systems.

---

### 5. Large Language Models for Conducting Systematic Reviews: On the Rise, but Not Yet Ready for Use—A Scoping Review

**Authors:** Wagner et al.  
**Year:** 2025  
**Venue:** Journal of Clinical Epidemiology, 181, 111746  
**DOI:** https://doi.org/10.1016/j.jclinepi.2025.111746

**Relevance:** Reviews how LLMs are being applied across systematic-review workflows and highlights remaining validation challenges.

---

## Foundational and Methods Papers

### 6. Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks

**Authors:** Lewis, P., Perez, E., Piktus, A., Petroni, F., Karpukhin, V., Goyal, N., Küttler, H., Lewis, M., Yih, W.-t., Rocktäschel, T., Riedel, S., & Kiela, D.  
**Year:** 2020  
**Venue:** Advances in Neural Information Processing Systems 33 (NeurIPS 2020)  
**DOI:** https://doi.org/10.48550/arXiv.2005.11401

**Relevance:** Introduces Retrieval-Augmented Generation, a key approach for connecting LLM generation with external and updatable knowledge sources.

---

### 7. On Faithfulness and Factuality in Abstractive Summarization

**Authors:** Maynez, J., Narayan, S., Bohnet, B., & McDonald, R.  
**Year:** 2020  
**Venue:** Proceedings of ACL 2020, 1906–1919  
**DOI:** https://doi.org/10.18653/v1/2020.acl-main.173

**Relevance:** Studies faithfulness and factuality problems in generated summaries, providing important foundations for evaluating LLM-generated literature reviews.

---

### 8. LitLLM: A Toolkit for Scientific Literature Review

**Authors:** Agarwal, S., Laradji, I. H., Charlin, L., & Pal, C.  
**Year:** 2024  
**Venue:** arXiv  
**DOI:** https://doi.org/10.48550/arXiv.2402.01788

**Relevance:** Presents a toolkit using retrieval-augmented generation and specialized prompting for automated scientific literature-review generation.

---

### 9. PaperQA: Retrieval-Augmented Generative Agent for Scientific Research

**Authors:** Lála, J., O'Donoghue, O., Shtedritski, A., Cox, S., Rodriques, S. G., & White, A. D.  
**Year:** 2023  
**Venue:** arXiv  
**DOI:** https://doi.org/10.48550/arXiv.2312.07559

**Relevance:** Introduces a retrieval-augmented research agent designed to answer questions using scientific literature with source-based evidence.

---

### 10. Synthesizing Scientific Literature with Retrieval-Augmented Language Models

**Authors:** Asai, A., He, J., Shao, R., Shi, W., Singh, A., Chang, J. C., Lo, K., Soldaini, L., Feldman, S., D'Arcy, M., Wadden, D., Latzke, M., Sparks, J., Hwang, J. D., Kishore, V., Tian, M., Ji, P., Liu, S., Tong, H., Wu, B., Xiong, Y., Zettlemoyer, L., Neubig, G., Weld, D. S., Downey, D., Yih, W.-t., Koh, P. W., & Hajishirzi, H.  
**Year:** 2026  
**Venue:** Nature, 650, 859–867  
**DOI:** https://doi.org/10.1038/s41586-025-10072-4

**Relevance:** Demonstrates retrieval-augmented approaches for synthesizing scientific literature and improving evidence-grounded scientific knowledge synthesis.

---

## Recent Research and Benchmarks

### 11. Dated Data: Tracing Knowledge Cutoffs in Large Language Models

**Authors:** Cheng, J., Marone, M., Weller, O., Lawrie, D., Khashabi, D., & Van Durme, B.  
**Year:** 2024  
**Venue:** arXiv  
**DOI:** https://doi.org/10.48550/arXiv.2403.12958

**Relevance:** Introduces the concept of an effective knowledge cutoff and investigates how actual model knowledge boundaries can differ from reported cutoff dates.

---

### 12. Can Prompts Rewind Time for LLMs? Evaluating the Effectiveness of Prompted Knowledge Cutoffs

**Authors:** Gao, X., Zhang, R., Du, D., Mahindre, S., Somayajula, S. A., & Xie, P.  
**Year:** 2025  
**Venue:** Proceedings of EMNLP 2025, 20777–20788  
**DOI:** https://doi.org/10.18653/v1/2025.emnlp-main.1049

**Relevance:** Evaluates whether prompting can make LLMs operate under an earlier knowledge cutoff and examines temporal leakage.

---

### 13. Carpe Diem: On the Evaluation of World Knowledge in Lifelong Language Models

**Authors:** Kim, Y., Yoon, J., Ye, S., Bae, S., Ho, N., Hwang, S. J., & Yun, S.-Y.  
**Year:** 2024  
**Venue:** Proceedings of NAACL-HLT 2024, 5401–5415  
**DOI:** https://doi.org/10.18653/v1/2024.naacl-long.302

**Relevance:** Evaluates how lifelong language models acquire and maintain knowledge as the world changes.

---

### 14. HoH: A Dynamic Benchmark for Evaluating the Impact of Outdated Information on Retrieval-Augmented Generation

**Authors:** Ouyang, J., Pan, T., Cheng, M., Yan, R., Luo, Y., Lin, J., & Liu, Q.  
**Year:** 2025  
**Venue:** Proceedings of ACL 2025, 6036–6063  
**DOI:** https://doi.org/10.18653/v1/2025.acl-long.301

**Relevance:** Provides a benchmark for studying the effects of outdated information in retrieval-augmented generation systems.

---

### 15. EvolveBench: A Comprehensive Benchmark for Assessing Temporal Awareness in LLMs on Evolving Knowledge

**Authors:** Zhu, Z., Liao, Y., Chen, Z., Wang, Y., Guan, Y., Wang, Y., & Wang, Y.  
**Year:** 2025  
**Venue:** Proceedings of ACL 2025, 16173–16188  
**DOI:** https://doi.org/10.18653/v1/2025.acl-long.788

**Relevance:** Evaluates the temporal awareness of LLMs when dealing with knowledge that changes over time.

---

### 16. DeepResearch Bench: A Comprehensive Benchmark for Deep Research Agents

**Authors:** Du, M., Xu, B., Zhu, C., Wang, X., & Mao, Z.  
**Year:** 2025  
**Venue:** arXiv  
**DOI:** https://doi.org/10.48550/arXiv.2506.11763

**Relevance:** Introduces a benchmark for evaluating deep research agents on complex research tasks, information retrieval, report quality, and citation accuracy.

---

## Literature Review and Research Automation

### 17. Automated Literature Research and Review-Generation Method Based on Large Language Models

**Authors:** Wu, S., Ma, X., Luo, D., Li, L., Shi, X., Chang, X., Lin, X., Luo, R., Pei, C., Du, C., Zhao, Z.-J., & Gong, J.  
**Year:** 2025  
**Venue:** National Science Review, 12(6), nwaf169  
**DOI:** https://doi.org/10.1093/nsr/nwaf169

**Relevance:** Presents an automated approach for conducting literature research and generating literature reviews using large language models.

---

### 18. History Matters: Temporal Knowledge Editing in Large Language Model

**Authors:** Yin, X., Jiang, J., Yang, L., & Wan, X.  
**Year:** 2024  
**Venue:** Proceedings of the AAAI Conference on Artificial Intelligence, 38(17)  
**DOI:** https://doi.org/10.1609/aaai.v38i17.29912

**Relevance:** Studies temporal knowledge editing and emphasizes preserving historical knowledge while integrating updated information.

---

## Temporal Knowledge and Continual Learning

### 19. Mitigating Temporal Misalignment by Discarding Outdated Facts

**Authors:** Zhang, M., & Choi, E.  
**Year:** 2023  
**Venue:** Proceedings of EMNLP 2023, 14213–14226  
**DOI:** https://doi.org/10.18653/v1/2023.emnlp-main.879

**Relevance:** Investigates temporal misalignment between model knowledge and current information and proposes methods for handling outdated facts.

---

### 20. Citation Constraints and Reference Hallucinations in Large Language Models

**Authors:** Davis, K., & Mahmoud, Q.  
**Year:** 2026  
**Venue:** Proceedings of the 39th Canadian Conference on Artificial Intelligence, 318, 464–475  
**Publisher:** PMLR

**Relevance:** Examines citation constraints and reference hallucinations in LLM-generated content, directly addressing citation reliability in academic writing.

---

## Notes

- Papers are organized according to their relevance to knowledge cutoffs, temporal knowledge, literature-review automation, retrieval-augmented generation, citation reliability, and continual learning.
- Links point to DOI or official scholarly sources where available.
- The collection is intended for research and academic resource curation.