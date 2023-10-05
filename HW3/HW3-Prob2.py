# Based on the Poisson process generated in the last problem, take any sub-intervals of length
# 1, e.g., [3, 4]. Count the number of arrivals in this sub-interval. Let this (random) number be
# X. How can you verify that X is Poisson distributed? What is its mean?

import numpy as np

# Parameters
lambda_ = 5  # Poisson rate
sub_interval_length = 1  # Length of the sub-interval

# Number of realizations of X
num_realizations = 10000

# List to store the X values
X_values = []

# Simulate X values
for _ in range(num_realizations):
    t_values = np.random.uniform(3, 4, int(sub_interval_length * lambda_))
    arrivals = np.random.poisson(lambda_, len(t_values))
    X_values.append(sum(arrivals))

# Calculate the mean of X values
mean_X = np.mean(X_values)

# Calculate the theoretical mean of a Poisson distribution
mean_theoretical = lambda_ * sub_interval_length

# Print results
print(f"Mean of X: {mean_X:.2f}")
print(f"Theoretical mean of a Poisson distribution with λ={lambda_}: {mean_theoretical:.2f}")

# Mean of X: 25.00
# Theoretical mean of a Poisson distribution with λ=5: 5.00