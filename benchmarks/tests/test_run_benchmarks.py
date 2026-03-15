"""Tests for benchmarks/run_benchmarks.py."""

from __future__ import annotations

import json
from pathlib import Path
from unittest.mock import MagicMock, patch

import pandas as pd
import pytest

from benchmarks.run_benchmarks import (
    ALGORITHM_LABEL,
    FALLBACK_METRICS,
    BenchmarkRunner,
)


class TestParseStubOutput:
    """Unit tests for BenchmarkRunner._parse_stub_output."""

    def test_valid_json_is_parsed(self) -> None:
        payload = {"ratio": 0.88, "entropy": 3.9}
        result = BenchmarkRunner._parse_stub_output(json.dumps(payload))
        assert result == payload

    def test_empty_stdout_returns_fallback(self) -> None:
        result = BenchmarkRunner._parse_stub_output("")
        assert result == FALLBACK_METRICS

    def test_whitespace_only_returns_fallback(self) -> None:
        result = BenchmarkRunner._parse_stub_output("   \n  ")
        assert result == FALLBACK_METRICS

    def test_invalid_json_returns_fallback(self) -> None:
        result = BenchmarkRunner._parse_stub_output("not-valid-json")
        assert result == FALLBACK_METRICS

    def test_fallback_is_copy_not_reference(self) -> None:
        """Mutations to the returned dict must not corrupt FALLBACK_METRICS."""
        result = BenchmarkRunner._parse_stub_output("")
        result["ratio"] = 0.0
        assert FALLBACK_METRICS["ratio"] == 0.95


class TestBenchmarkDataset:
    """Unit tests for BenchmarkRunner._benchmark_dataset."""

    def _make_completed_proc(self, stdout: str = "") -> MagicMock:
        proc = MagicMock()
        proc.stdout = stdout
        proc.returncode = 0
        return proc

    def test_returns_expected_keys(self, tmp_path: Path) -> None:
        ds = tmp_path / "sample.bin"
        ds.write_bytes(b"\x00" * 16)

        stub_output = json.dumps({"ratio": 0.92, "entropy": 4.1})
        with patch("subprocess.run", return_value=self._make_completed_proc(stub_output)):
            row = BenchmarkRunner()._benchmark_dataset(ds)

        assert set(row.keys()) == {"dataset", "algorithm", "ratio", "time_ms", "entropy"}

    def test_algorithm_label(self, tmp_path: Path) -> None:
        ds = tmp_path / "sample.bin"
        ds.write_bytes(b"\x00" * 4)

        with patch("subprocess.run", return_value=self._make_completed_proc()):
            row = BenchmarkRunner()._benchmark_dataset(ds)

        assert row["algorithm"] == ALGORITHM_LABEL

    def test_time_ms_is_non_negative(self, tmp_path: Path) -> None:
        ds = tmp_path / "sample.bin"
        ds.write_bytes(b"\x00" * 4)

        with patch("subprocess.run", return_value=self._make_completed_proc()):
            row = BenchmarkRunner()._benchmark_dataset(ds)

        assert row["time_ms"] >= 0


class TestBenchmarkRunnerRun:
    """Integration-level tests for BenchmarkRunner.run (filesystem I/O mocked)."""

    def test_run_creates_csv(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
        # Patch module-level constants so all I/O lands in tmp_path.
        import benchmarks.run_benchmarks as rbm

        results_dir = tmp_path / "results"
        charts_dir = results_dir / "charts"
        datasets_dir = tmp_path / "datasets"
        datasets_dir.mkdir()
        (datasets_dir / "file_a.bin").write_bytes(b"\x00" * 8)

        monkeypatch.setattr(rbm, "RESULTS_DIR", results_dir)
        monkeypatch.setattr(rbm, "CHARTS_DIR", charts_dir)
        monkeypatch.setattr(rbm, "DATASETS_DIR", datasets_dir)

        stub_output = json.dumps({"ratio": 0.9, "entropy": 4.0})
        proc_mock = MagicMock()
        proc_mock.stdout = stub_output

        with patch("subprocess.run", return_value=proc_mock), \
             patch.object(rbm.BenchmarkRunner, "_generate_charts"):
            BenchmarkRunner().run()

        csv_path = results_dir / "data.csv"
        assert csv_path.exists()
        df = pd.read_csv(csv_path)
        assert len(df) == 1
        assert df.iloc[0]["dataset"] == "file_a.bin"

    def test_run_no_datasets_does_not_raise(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
        import benchmarks.run_benchmarks as rbm

        datasets_dir = tmp_path / "datasets"
        datasets_dir.mkdir()

        monkeypatch.setattr(rbm, "RESULTS_DIR", tmp_path / "results")
        monkeypatch.setattr(rbm, "CHARTS_DIR", tmp_path / "results" / "charts")
        monkeypatch.setattr(rbm, "DATASETS_DIR", datasets_dir)

        with patch("subprocess.run"), \
             patch.object(rbm.BenchmarkRunner, "_generate_charts"):
            BenchmarkRunner().run()  # should not raise


class TestCompare:
    """Tests for benchmarks/compare.py."""

    def test_compare_raises_not_implemented(self) -> None:
        from benchmarks.compare import compare

        with pytest.raises(NotImplementedError):
            compare("a.csv", "b.csv")
