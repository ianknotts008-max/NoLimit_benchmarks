"""Utility for comparing multiple benchmark CSVs.

This is intentionally minimal – real logic is proprietary and kept out of
the public repository.
"""

from __future__ import annotations

from pathlib import Path


def compare(csv1: str | Path, csv2: str | Path) -> None:
    """Compare two benchmark result CSV files.

    Args:
        csv1: Path to the first CSV file.
        csv2: Path to the second CSV file.

    Raises:
        NotImplementedError: Always – comparison logic is not part of the public repo.
    """
    raise NotImplementedError("Comparison logic is not part of the public repo")
