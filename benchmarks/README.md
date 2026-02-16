# Benchmarks

This directory holds the Python harness used to run compression benchmarks.

- `run_benchmarks.py`: main script (invokes stub binary and logs results)
- `compare.py`: placeholder for comparison logic (not public)
- `datasets/`: public sample files for testing
- `results/`: generated CSVs and charts (ignored via `.gitignore`)

All logic is intentionally simple and safe; proprietary algorithms are never
included in this repository.