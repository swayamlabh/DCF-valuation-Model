"""Run WACC and terminal growth sensitivity analysis for the DCF model."""

from __future__ import annotations

from pathlib import Path
import sys

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from models.dcf_valuation_model import (  # noqa: E402
    DcfAssumptions,
    load_financials,
    sensitivity_table,
)


DATA_PATH = REPO_ROOT / "data" / "sample_company_financials.csv"


def basis_point_range(start: int, stop: int, step: int) -> list[float]:
    """Return decimal rates from basis-point inputs, inclusive of stop."""
    return [basis_points / 10_000 for basis_points in range(start, stop + step, step)]


def print_table(rows: list[dict[str, float]]) -> None:
    """Render a small sensitivity table without external dependencies."""
    headers = list(rows[0])
    print(" | ".join(headers))
    print(" | ".join("---" for _ in headers))
    for row in rows:
        print(" | ".join(f"{row[header]:,.2f}" for header in headers))


def main() -> None:
    """Print an intrinsic value sensitivity table to the console."""
    financials = load_financials(str(DATA_PATH))
    assumptions = DcfAssumptions()
    table = sensitivity_table(
        financials=financials,
        base_assumptions=assumptions,
        wacc_range=basis_point_range(800, 1100, 100),
        terminal_growth_range=basis_point_range(150, 350, 50),
    )
    print_table(table)


if __name__ == "__main__":
    main()
