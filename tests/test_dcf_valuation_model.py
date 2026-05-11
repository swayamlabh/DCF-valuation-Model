from models.dcf_valuation_model import (
    CompanyFinancials,
    DcfAssumptions,
    calculate_dcf,
    project_free_cash_flow,
    sensitivity_table,
)


def sample_financials() -> CompanyFinancials:
    return CompanyFinancials(
        year=2023,
        revenue=1250,
        ebit_margin=0.185,
        tax_rate=0.24,
        depreciation_pct_revenue=0.035,
        capex_pct_revenue=0.045,
        nwc_pct_revenue=0.12,
        cash=180,
        debt=420,
        shares_outstanding=75,
        street_estimate=38.5,
    )


def test_project_free_cash_flow_links_operating_assumptions():
    forecast = project_free_cash_flow(sample_financials(), DcfAssumptions())

    assert len(forecast) == 5
    assert forecast[0]["year"] == 2024
    assert forecast[0]["free_cash_flow"] > 0


def test_calculate_dcf_returns_intrinsic_share_value():
    result = calculate_dcf(sample_financials(), DcfAssumptions())

    assert result["enterprise_value"] > 0
    assert result["equity_value"] > 0
    assert result["intrinsic_value_per_share"] > 0
    assert result["street_estimate"] == 38.5


def test_sensitivity_table_builds_wacc_terminal_growth_matrix():
    table = sensitivity_table(
        sample_financials(),
        DcfAssumptions(),
        wacc_range=[0.09, 0.10],
        terminal_growth_range=[0.02, 0.03],
    )

    assert list(table[0]) == ["wacc", "tg_2.0%", "tg_3.0%"]
    assert len(table) == 2
