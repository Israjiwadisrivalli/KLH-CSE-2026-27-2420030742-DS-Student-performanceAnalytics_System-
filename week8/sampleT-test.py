import numpy as np
from scipy.stats import ttest_1samp

# Sample data
data = np.random.normal(loc=11.8, scale=0.5, size=100)

# Population mean
population_mean = 12

# One Sample T-Test
t_statistic, p_value = ttest_1samp(data, population_mean)

print(f"T-Statistic: {t_statistic:.4f}")
print(f"P-Value: {p_value:.4f}")

# Significance level
alpha = 0.05

if p_value < alpha:
    print("Reject the null hypothesis: The average battery life is different from 12 hours.")
else:
    print("Fail to reject the null hypothesis: The average battery life is not significantly different from 12 hours.")