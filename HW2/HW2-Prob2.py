# Generate 100 samples of X, and plot the empirical CDF
# (i.e., you need to estimate P (X ≤ a) from your samples for each value of a). Does it fit the
# CDF of exponential distribution with mean 10? Further, calculate the empirical mean of the
# 100 samples of X. Is it close to 10? If any of the fit is less than perfect, try 1000 samples of
# X. Do the same for Y , except that in this case you can plot the empirical PMF (probability
# mass function) and see if it fits.
import matplotlib.pyplot as plt
import numpy as np

samples = 100
lambda_param = 1/10
np.random.seed(30)
uniform_samples = np.random.rand(samples)
exponential_samples = -np.log(1 - uniform_samples) / lambda_param

# Calculate the empirical CDF
sorted_samples = np.sort(exponential_samples)
ecdf = np.arange(1, samples + 1) / samples

# Plot the empirical CDF
plt.step(sorted_samples, ecdf, label='Empirical CDF')
plt.xlabel('X')
plt.ylabel('CDF')
plt.title('Empirical CDF of X (Exponential with Mean 10)')
plt.grid(True)
plt.legend()
plt.show()

empirical_mean = np.mean(exponential_samples)
print(f"Empirical Mean of X: {empirical_mean}")

# Calculate the theoretical mean (should be close to 10)
theoretical_mean = 1 / lambda_param
print(f"Theoretical Mean of X: {theoretical_mean}")
poisson_samples = np.zeros(samples, dtype=int)
lambda_param = 10
for i in range(samples):
    p = 1.0
    k = 0
    while True:
        k += 1
        p *= np.random.rand()
        if p < np.exp(-lambda_param):
            break
    poisson_samples[i] = k - 1
unique_vals, counts = np.unique(poisson_samples, return_counts=True)
pmf = counts/samples
plt.bar(unique_vals, pmf, label='Empirical PMF', width=0.5, align='center')
plt.xlabel('Y')
plt.ylabel('PMF')
plt.title('Empirical PMF of Y (Poisson with Mean 10)')
plt.grid(True)
plt.legend()
plt.show()

empirical_mean = np.mean(poisson_samples)
print(f"Empirical Mean of Y: {empirical_mean}")

# Calculate the theoretical mean (should be close to 10)
theoretical_mean = lambda_param
print(f"Theoretical Mean of Y: {theoretical_mean}")