import numpy as np
import matplotlib.pyplot as plt

# Parameters
lambda_ = 5  # Poisson rate
T = 30  # Total time

# Generate Poisson process
t_values = np.linspace(0, T, 1000)  # Time values
poisson_samples = np.random.poisson(lambda_, len(t_values))

# Plot the Poisson process
plt.figure(figsize=(10, 6))
plt.step(t_values, np.cumsum(poisson_samples), where='post')
plt.xlabel('Time (t)')
plt.ylabel('N(t)')
plt.title(f'Poisson Process with λ = {lambda_}')
plt.grid(True)
plt.show()