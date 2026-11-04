
import numpy as np
from scipy import stats
from statsmodels.stats.weightstats import ztest

print("----- Z-Test -----")

sample_marks = np.array([78, 82, 85, 88, 90, 76, 95, 89, 84, 91])
population_mean = 80

z_stat, p_value = ztest(sample_marks, value=population_mean)

print("Sample Marks:", sample_marks)
print("Population Mean:", population_mean)
print("Z-Statistic:", z_stat)
print("P-Value:", p_value)

alpha = 0.05
print("Result:", "Reject Null Hypothesis" if p_value < alpha
      else "Fail to Reject Null Hypothesis")

print("\n----- Independent t-Test -----")

class_A = np.array([78, 82, 85, 88, 90])
class_B = np.array([72, 75, 70, 68, 74])

t_stat, p_value = stats.ttest_ind(class_A, class_B)

print("Class A Marks:", class_A)
print("Class B Marks:", class_B)
print("t-Statistic:", t_stat)
print("P-Value:", p_value)

print("Result:", "Reject Null Hypothesis" if p_value < alpha
      else "Fail to Reject Null Hypothesis")
