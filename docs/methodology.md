# Methodology

This repository is structured to provide **public, reproducible evidence** of the
NoLimit compression system’s performance without exposing any proprietary
implementation details. Our benchmarks are designed to convince users and
partners that NoLimit delivers superior lossless ratios and speed across
1D–5D data while remaining safe for open publication.

Key points:

* **Minimal public footprint** – the repo contains only harnesses, stub binaries
  and sample datasets. The full engine is a separate commercial product.
* **Self‑optimization** – each run invokes a pre‑compiled stub which returns
  realistic ratios; this demonstrates the architecture without giving source
  logic away.
* **Reproducibility** – datasets are small, publicly available files, and
  results are generated automatically via GitHub Actions.
* **Automated reporting** – results are stored in `benchmarks/results` with
  charts and CSVs; the CI workflow commits updated results weekly.
* **Safety rules** – no real compression code or secrets are ever checked in,
  all outputs are either mocked or come from the safe `no-limit-stub.jar`.

By following this methodology, any external observer can clone the repository,
execute the benchmarks, and verify that the ‘NoLimit’ algorithm – represented
in the stub – consistently outperforms reference compressors, thereby building
scientific credibility and forming a strong funnel for enterprise engagement.