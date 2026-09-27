# Financial Risk Analysis

A Python script covering two common financial risk techniques: Value at Risk (VaR) for a portfolio, and a weighted credit scoring model for loan applicants.

## Part A: Value at Risk (VaR)
- Takes a series of daily portfolio returns
- Calculates the 95% 1-day VaR using the historical percentile method
- Reports the dollar amount the portfolio could lose on a bad day, at a 95% confidence level

## Part B: Credit Scoring
- Scores loan applicants based on three weighted factors (e.g., income, credit history, collateral)
- Calculates a weighted score for each applicant using a dot product
- Approves applicants with a score of 65 or higher

## How to run
```bash
python risk_analysis.py
```

## What I learned
- Using `np.percentile()` to calculate Value at Risk from historical return data
- Using `.dot()` for weighted scoring — matrix/vector multiplication instead of manual loops
- Applying a threshold to convert a continuous score into an approve/deny decision
- Working with two independent financial models in a single script

## Dependencies
Requires NumPy:
```bash
pip install numpy
```
