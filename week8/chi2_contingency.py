import pandas as pd
from scipy.stats import chi2_contingency

data = [[30, 20],
        [35, 15]]

chi2, p, dof, expected = chi2_contingency(data)

print("Chi-Square Value:", chi2)
print("P-Value:", p)
print("Degree of Freedom:", dof)
print("Expected Frequencies:")
print(expected)

