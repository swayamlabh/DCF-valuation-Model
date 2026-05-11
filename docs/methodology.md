# DCF Valuation Methodology

This project models a listed equity investment using an integrated operating forecast and a discounted cash flow valuation.

## 1. Integrated Operating Forecast

The model starts with base-year revenue and operating assumptions. Forecast revenue is grown by year-specific growth rates, then linked to operating profitability, taxes, depreciation, capital expenditure, and working capital investment.

Free cash flow is calculated as:

```text
FCF = NOPAT + Depreciation - Capital Expenditures - Change in Net Working Capital
```

## 2. Discounted Cash Flow Valuation

Projected free cash flows are discounted at the weighted average cost of capital (WACC). The terminal value uses the Gordon Growth method:

```text
Terminal Value = Final Year FCF × (1 + Terminal Growth) / (WACC - Terminal Growth)
```

Enterprise value is the sum of discounted forecast cash flows and discounted terminal value. Equity value is calculated by adding cash and subtracting debt.

```text
Equity Value = Enterprise Value + Cash - Debt
Intrinsic Value per Share = Equity Value / Shares Outstanding
```

## 3. Sensitivity Analysis

The sensitivity analysis varies WACC and terminal growth assumptions to show how intrinsic share value changes under different discount rate and long-term growth scenarios.

## 4. Benchmarking

The model includes a street-estimate benchmark field so the derived intrinsic value can be compared with analyst consensus or other market reference points.
