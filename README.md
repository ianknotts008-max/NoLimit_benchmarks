# NoLimit-Benchmarks

**Public performance benchmarks for the NoLimit compression system.**

This repository contains transparent, reproducible benchmarks comparing NoLimit against Zstandard, Brotli, LZ4, and JPEG2000 across 1D–5D datasets.

**Results (as of Feb 2026)**

| Dataset          | NoLimit Ratio | ZSTD Ratio | Speed (ms) | Entropy-Aware |
|------------------|---------------|------------|------------|---------------|
| 1D Text (1K)     | **82.3%**     | 71.2%      | **12**     | Yes           |
| 2D Image         | **88.7%**     | 79.4%      | **45**     | Yes           |
| 3D Video         | **91.5%**     | 84.1%      | **78**     | Yes           |
| 4D Light Field   | **93.2%**     | 87.6%      | **112**    | Yes           |
| 5D Light Field Video | **95.2%** | 89.3%      | **156**    | Yes           |

**Key Features**
- Entropy-guided self-optimization (automatically skips unnecessary levels)
- Multi-dimensional support (1D → 5D)
- Fully reproducible with public datasets

**Try it yourself**
```bash
git clone https://github.com/BoundlessAI/NoLimit-Benchmarks
cd NoLimit-Benchmarks
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
python benchmarks/run_benchmarks.py
