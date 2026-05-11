# DCF Valuation Model — Listed Equity

## Overview
A comprehensive integrated financial modeling and DCF (Discounted Cash Flow) valuation framework for listed equity investments. This project combines 3-statement-style operating projections with DCF valuation methodology to derive intrinsic share value, benchmarked against street estimates.

## Project Summary
Built an integrated 3-statement model and DCF valuation in Excel; ran sensitivity on WACC and terminal growth to derive an intrinsic share value benchmarked vs. street estimates. This repository mirrors that workflow in Python so assumptions, valuation outputs, and sensitivity tables can be reproduced programmatically.

## Features
- **Integrated 3-Statement Model**: Links revenue, operating profit, taxes, capital expenditure, working capital, cash, debt, and equity value.
- **DCF Valuation Analysis**: Calculates projected free cash flow, terminal value, enterprise value, equity value, and per-share valuation.
- **Sensitivity Analysis**: Tests WACC (Weighted Average Cost of Capital) and terminal growth rate variations.
- **Valuation Benchmarking**: Compares intrinsic value per share with analyst street estimates or market consensus.

## Project Structure
```
DCF-valuation-Model/
├── README.md
├── requirements.txt
├── models/
│   └── dcf_valuation_model.py
├── data/
│   └── sample_company_financials.csv
├── analysis/
│   └── sensitivity_analysis.py
├── docs/
│   └── methodology.md
└── tests/
    └── test_dcf_valuation_model.py
```

## Getting Started

### Prerequisites
- Python 3.10+
- pytest (for tests)

### Installation
```bash
git clone https://github.com/swayamlabh/DCF-valuation-Model.git
cd DCF-valuation-Model
python -m pip install -r requirements.txt
```

## Usage

Run the base DCF valuation:
```bash
python models/dcf_valuation_model.py
```

Run the WACC and terminal growth sensitivity table:
```bash
python analysis/sensitivity_analysis.py
```

Run the test suite:
```bash
python -m pytest
```

## Methodology
The DCF valuation follows these key steps:
1. Project future free cash flows from linked operating assumptions.
2. Calculate and apply the Weighted Average Cost of Capital (WACC).
3. Discount projected cash flows to present value.
4. Determine terminal value using the Gordon Growth method.
5. Calculate enterprise value and per-share intrinsic value.
6. Perform sensitivity analysis on WACC and terminal growth assumptions.
7. Benchmark the derived intrinsic value against street estimates.

For more detail, see [docs/methodology.md](docs/methodology.md).

## Valuation Benchmarking
Compare derived intrinsic value against:
- Analyst consensus price targets
- Historical P/E multiples
- Industry peer valuations
- Street estimates

## Contributing
Contributions are welcome. Please feel free to submit a Pull Request.

## License
[Add appropriate license]

## Contact
Created by [@swayamlabh](https://github.com/swayamlabh)

## References
- DCF Valuation Theory and Practice
- Financial Modeling Best Practices
