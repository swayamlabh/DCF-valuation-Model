# DCF Valuation Model — Listed Equity

## Overview
A comprehensive integrated financial modeling and DCF (Discounted Cash Flow) valuation framework for listed equity investments. This project combines 3-statement financial modeling with DCF valuation methodology to derive intrinsic share value, benchmarked against street estimates.

## Features
- **Integrated 3-Statement Model**: Income Statement, Balance Sheet, and Cash Flow Statement
- **DCF Valuation Analysis**: Enterprise Value calculation and per-share valuation
- **Sensitivity Analysis**: WACC (Weighted Average Cost of Capital) and terminal growth rate variations
- **Valuation Benchmarking**: Comparison with analyst street estimates and market consensus

## Project Structure
```
DCF-valuation-Model/
├── README.md
├── models/
│   └── dcf_valuation_model.py
├── data/
│   └── sample_company_financials.csv
├── analysis/
│   └── sensitivity_analysis.py
└── docs/
    └── methodology.md
```

## Getting Started

### Prerequisites
- Python 3.8+
- pandas
- numpy
- matplotlib (for visualizations)

### Installation
```bash
git clone https://github.com/swayamlabh/DCF-valuation-Model.git
cd DCF-valuation-Model
pip install -r requirements.txt
```

## Usage
[Coming soon]

## Methodology
The DCF valuation follows these key steps:
1. Project future free cash flows
2. Calculate the Weighted Average Cost of Capital (WACC)
3. Discount projected cash flows to present value
4. Determine terminal value
5. Calculate enterprise value and per-share intrinsic value
6. Perform sensitivity analysis on key assumptions

## Valuation Benchmarking
Compare derived intrinsic value against:
- Analyst consensus price targets
- Historical P/E multiples
- Industry peer valuations
- Street estimates

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## License
[Add appropriate license]

## Contact
Created by [@swayamlabh](https://github.com/swayamlabh)

## References
- DCF Valuation Theory and Practice
- Financial Modeling Best Practices
