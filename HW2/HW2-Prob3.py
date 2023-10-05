# Generate n = 100 continuous random variables uniformly-distributed within the interval
# [0, n]. Take any sub-interval of length 10. Count how many random variables that you have
# generated fall into this sub-interval. Let this number be Z, which should be random each
# time when you execute your code. Generate 100 samples of this random number Z and plot
# its empirical PMF. Does it fit the PMF of a Poisson random variable? If the fit is less than
# perfect, increase n to 1000 and try again. What is the mean of the Poisson random variable?
# (You may want to cross-reference Problem (3).)

import matplotlib.pyplot as plt
import numpy as np

n = 1000
samples = 100
sub_length = 10
lambda_param = 1/10
np.random.seed(30)
uniform = np.random.uniform(0,n,n)

counts = np.sum((uniform >= 0) & (uniform < sub_length))
print(counts)
z_samples = np.random.poisson(lam=counts, size=samples)

unique_values, counts = np.unique(z_samples, return_counts=True)

# Calculate the empirical PMF
pmf = counts / samples

# Plot the empirical PMF
plt.bar(unique_values, pmf, label='Empirical PMF', width=1, align='center')
plt.xlabel('Z')
plt.ylabel('PMF')
plt.title(f'Empirical PMF of Z (Poisson with Mean {counts.mean():.2f})')
plt.grid(True)
plt.legend()
plt.show()

# Calculate the mean of the Poisson random variable
poisson_mean = counts.mean()
print(f"Mean of the Poisson Random Variable: {poisson_mean}")