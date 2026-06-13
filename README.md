# Bank Loan Default — Exploratory Data Analysis

Exploratory analysis of an 850-record bank loan dataset to identify patterns in borrower demographics, debt ratios, and loan default behaviour.

&nbsp;

## Objective

Understand which borrower characteristics are associated with higher default risk, and surface insights that could support lending decisions.

&nbsp;

## Dataset

| Feature | Description |
|---------|-------------|
| `age` | Borrower age |
| `ed` | Education level (1–4) |
| `employ` | Years at current employer |
| `address` | Years at current address |
| `income` | Annual income |
| `debtinc` | Debt-to-income ratio |
| `creddebt` | Credit card debt |
| `othdebt` | Other debt |
| `default` | Loan default (1 = yes, 0 = no) |

&nbsp;

## Key Findings

- **26.1%** of borrowers defaulted on their loans.
- Higher **debt-to-income ratios** showed a visible correlation with default.
- Age distribution is concentrated between **25–40**, with default rates relatively consistent across age groups.
- 150 records had missing default status — handled during analysis.

&nbsp;

## Tools Used

`Python` · `pandas` · `matplotlib` · `seaborn`

&nbsp;

## How to Run

```bash
pip install pandas matplotlib seaborn
python bank_loan_eda.py
```

&nbsp;

## Output

The script generates three visualisations:

- `age_distribution.png` — histogram of borrower ages
- `default_rate_by_age.png` — default rate across age groups
- `income_vs_debtinc.png` — scatter plot of income vs debt-to-income ratio, coloured by default status
