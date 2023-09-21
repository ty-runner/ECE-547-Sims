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