"""DCF valuation utilities for a listed equity investment.

The module contains a compact integrated projection engine that links revenue,
operating profit, tax, reinvestment, working capital, enterprise value, equity
value, and intrinsic value per share. Inputs are intentionally simple so the
model can be reviewed, audited, and adapted to a fuller Excel workbook.
"""

from __future__ import annotations

import csv
from dataclasses import dataclass
from typing import Iterable


@dataclass(frozen=True)
class CompanyFinancials:
    """Base-year financial assumptions for a listed company."""

    year: int
    revenue: float
    ebit_margin: float
    tax_rate: float
    depreciation_pct_revenue: float
    capex_pct_revenue: float
    nwc_pct_revenue: float
    cash: float
    debt: float
    shares_outstanding: float
    street_estimate: float | None = None


@dataclass(frozen=True)
class DcfAssumptions:
    """Forecast and valuation assumptions used in the DCF model."""

    revenue_growth: tuple[float, ...] = (0.08, 0.075, 0.065, 0.055, 0.045)
    wacc: float = 0.095
    terminal_growth: float = 0.025

    def validate(self) -> None:
        """Validate assumptions that would break a Gordon Growth DCF."""
        if self.wacc <= self.terminal_growth:
            raise ValueError("WACC must be greater than terminal growth rate.")
        if not self.revenue_growth:
            raise ValueError("At least one revenue growth assumption is required.")


def load_financials(path: str) -> CompanyFinancials:
    """Load a single-row financials CSV into a typed assumptions object."""
    with open(path, newline="", encoding="utf-8") as csv_file:
        row = next(csv.DictReader(csv_file))

    return CompanyFinancials(
        year=int(row["year"]),
        revenue=float(row["revenue"]),
        ebit_margin=float(row["ebit_margin"]),
        tax_rate=float(row["tax_rate"]),
        depreciation_pct_revenue=float(row["depreciation_pct_revenue"]),
        capex_pct_revenue=float(row["capex_pct_revenue"]),
        nwc_pct_revenue=float(row["nwc_pct_revenue"]),
        cash=float(row["cash"]),
        debt=float(row["debt"]),
        shares_outstanding=float(row["shares_outstanding"]),
        street_estimate=float(row["street_estimate"]),
    )


def project_free_cash_flow(
    financials: CompanyFinancials,
    assumptions: DcfAssumptions,
) -> list[dict[str, float]]:
    """Build linked operating projections and free cash flow by forecast year."""
    assumptions.validate()

    rows: list[dict[str, float]] = []
    previous_revenue = financials.revenue
    previous_nwc = financials.revenue * financials.nwc_pct_revenue

    for period, growth in enumerate(assumptions.revenue_growth, start=1):
        year = financials.year + period
        revenue = previous_revenue * (1 + growth)
        ebit = revenue * financials.ebit_margin
        tax = ebit * financials.tax_rate
        nopat = ebit - tax
        depreciation = revenue * financials.depreciation_pct_revenue
        capex = revenue * financials.capex_pct_revenue
        net_working_capital = revenue * financials.nwc_pct_revenue
        change_in_nwc = net_working_capital - previous_nwc
        free_cash_flow = nopat + depreciation - capex - change_in_nwc

        rows.append(
            {
                "year": float(year),
                "revenue": revenue,
                "ebit": ebit,
                "tax": tax,
                "nopat": nopat,
                "depreciation": depreciation,
                "capex": capex,
                "change_in_nwc": change_in_nwc,
                "free_cash_flow": free_cash_flow,
            }
        )
        previous_revenue = revenue
        previous_nwc = net_working_capital

    return rows


def calculate_dcf(
    financials: CompanyFinancials,
    assumptions: DcfAssumptions,
) -> dict[str, float | list[dict[str, float]]]:
    """Calculate enterprise value, equity value, and intrinsic value per share."""
    forecast = project_free_cash_flow(financials, assumptions)
    for period, row in enumerate(forecast, start=1):
        discount_factor = 1 / ((1 + assumptions.wacc) ** period)
        row["discount_factor"] = discount_factor
        row["present_value_fcf"] = row["free_cash_flow"] * discount_factor

    final_fcf = forecast[-1]["free_cash_flow"]
    terminal_value = final_fcf * (1 + assumptions.terminal_growth) / (
        assumptions.wacc - assumptions.terminal_growth
    )
    present_value_terminal = terminal_value / ((1 + assumptions.wacc) ** len(forecast))
    enterprise_value = sum(row["present_value_fcf"] for row in forecast) + present_value_terminal
    equity_value = enterprise_value + financials.cash - financials.debt
    intrinsic_value_per_share = equity_value / financials.shares_outstanding

    return {
        "forecast": forecast,
        "terminal_value": terminal_value,
        "present_value_terminal": present_value_terminal,
        "enterprise_value": enterprise_value,
        "equity_value": equity_value,
        "intrinsic_value_per_share": intrinsic_value_per_share,
        "street_estimate": financials.street_estimate,
    }


def sensitivity_table(
    financials: CompanyFinancials,
    base_assumptions: DcfAssumptions,
    wacc_range: Iterable[float],
    terminal_growth_range: Iterable[float],
) -> list[dict[str, float]]:
    """Create a WACC-by-terminal-growth intrinsic value sensitivity table."""
    rows: list[dict[str, float]] = []
    for wacc in wacc_range:
        row: dict[str, float] = {"wacc": wacc}
        for terminal_growth in terminal_growth_range:
            assumptions = DcfAssumptions(
                revenue_growth=base_assumptions.revenue_growth,
                wacc=wacc,
                terminal_growth=terminal_growth,
            )
            valuation = calculate_dcf(financials, assumptions)
            row[f"tg_{terminal_growth:.1%}"] = float(valuation["intrinsic_value_per_share"])
        rows.append(row)
    return rows


if __name__ == "__main__":
    company = load_financials("data/sample_company_financials.csv")
    result = calculate_dcf(company, DcfAssumptions())
    print(f"Intrinsic value per share: ${result['intrinsic_value_per_share']:.2f}")
    if result["street_estimate"] is not None:
        print(f"Street estimate benchmark: ${result['street_estimate']:.2f}")
