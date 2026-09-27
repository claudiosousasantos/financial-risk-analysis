import numpy as np

# ---------- PART A: VaR ----------
daily_returns = np.array([0.01, -0.02, 0.015, -0.005, 0.03, -0.04, 0.02, -0.01, 0.005, -0.025])
portfolio_value = 100000

dollar_returns = daily_returns * portfolio_value
VaR_95 = np.percentile(dollar_returns, 5)
print(f"95% 1-day VaR: ${abs(VaR_95):.2f}")

# ---------- PART B: Credit Scoring ----------
applicants = np.array([
    [80, 70, 90],
    [60, 40, 50],
    [95, 85, 99]
])
weights = np.array([0.4, 0.3, 0.3])

credit_scores = applicants.dot(weights)
approved = credit_scores >= 65

for i in range(len(credit_scores)):
    score = credit_scores[i]
    is_approved = approved[i]
    
    if is_approved:
        status = "✅ Approved"
    else:
        status = "❌ Denied"
    
    applicant_number = i + 1
    print(f"Applicant {applicant_number}: Score = {score:.1f} -> {status}")