
import numpy as np
from scipy.stats import bernoulli, binom

p = 0.7

print("----- Bernoulli Distribution -----")
samples = bernoulli.rvs(p, size=10)

print("Probability of Passing:", p)
print("Student Outcomes:", samples)
print("Probability of Pass:", bernoulli.pmf(1, p))
print("Probability of Fail:", bernoulli.pmf(0, p))

print("\n----- Binomial Distribution -----")
n, k = 10, 8

print("Number of Students:", n)
print("Probability of Passing:", p)
print("Probability exactly 8 pass:", binom.pmf(k, n, p))

random_binomial = binom.rvs(n, p, size=5)
print("Random Binomial Outcomes:", random_binomial)
