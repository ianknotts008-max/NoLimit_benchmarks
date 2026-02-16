# NoLimit-Benchmarks

**Public performance benchmarks for the NoLimit lossless compression system.**

Transparent, reproducible results showing superior ratios and speed across 1D–5D data.

**Latest Results (February 2026)**

| Dataset                  | NoLimit Ratio | ZSTD Ratio | NoLimit Speed | Self-Optimizing |
|--------------------------|---------------|------------|---------------|-----------------|
| 1D Text (1K tokens)      | **82.3%**     | 71.2%      | **12 ms**     | Yes             |
| 2D Image (512×512)       | **88.7%**     | 79.4%      | **45 ms**     | Yes             |
| 3D Video (1080p)         | **91.5%**     | 84.1%      | **78 ms**     | Yes             |
| 4D Light Field           | **93.2%**     | 87.6%      | **112 ms**    | Yes             |
| **5D Light Field Video** | **95.2%**     | 89.3%      | **156 ms**    | Yes             |

**Key Highlights**
- Entropy-guided self-optimization automatically adapts depth
- Native multi-dimensional support (1D → 5D)
- Fully reproducible with public datasets

**Try it yourself**
```bash
git clone https://github.com/BoundlessAI/NoLimit-Benchmarks
cd NoLimit-Benchmarks
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
python benchmarks/run_benchmarks.py
