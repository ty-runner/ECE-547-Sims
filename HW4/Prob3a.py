import numpy as np
import matplotlib.pyplot as plt

# Define the range of traffic intensities (ρ)
rho_values = np.linspace(0, 50000, 100000)  # You can adjust the range as needed

# Set the system capacities (N)
N_values = [4, 19]

# Create a legend label for each N value
legend_labels = [f'N = {N}' for N in N_values]

# Initialize a figure for the plot
plt.figure(figsize=(10, 6))

# Plot PB for each N value
for N in N_values:
    blocking_probabilities = (rho_values**N) / np.math.factorial(N) / np.sum([(rho_values**n) / np.math.factorial(n) for n in range(N + 1)])
    plt.plot(rho_values, blocking_probabilities)

# Add labels and legend
plt.title('Blocking Probability vs. Traffic Intensity (ρ) for Finite M/M/1 Queue')
plt.xlabel('Traffic Intensity (ρ)')
plt.ylabel('Blocking Probability (PB)')
plt.legend(legend_labels)

# Show the plot
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 6))

# Calculate normalized throughput (γ/μ) using 1 - PB
normalized_throughput_values = 1 - blocking_probabilities

# Plot γ/μ for each value of N
for N in N_values:
    plt.plot(rho_values, N*normalized_throughput_values, label=f'N = {N}')

# Set labels and legend
plt.xlabel('ρ (Normalized Load)')
plt.ylabel('γ/μ (Normalized Throughput)')
plt.legend()

# Show the plot
plt.grid(True)
plt.title('Normalized Throughput vs. Normalized Load')
plt.show()