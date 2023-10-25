import numpy as np
import matplotlib.pyplot as plt

# Function to calculate Erlang-B blocking probability
def erlang_b(ρ, N):
    if ρ == 0:
        return 0.0
    sum_term = 0.0
    for n in range(N + 1):
        sum_term += (ρ ** n) / np.math.factorial(n)
    return (ρ ** N) / (np.math.factorial(N) * sum_term)

# Parameters
ρ_values = np.linspace(0, 5000, 40000)  # Range of ρ values
N_values = [4, 19]  # Different N values

# Plotting PB for different N values
for N in N_values:
    PB_values = [erlang_b(ρ, N) for ρ in ρ_values]
    plt.plot(ρ_values, PB_values, label=f'N={N}')

plt.xlabel('ρ (normalized load)')
plt.ylabel('PB (blocking probability)')
plt.legend()
plt.grid()
plt.title('Blocking Probability vs. Normalized Load')
plt.show()

# Function to calculate normalized throughput (γ/μ)
def normalized_throughput(ρ, N):
    PB = erlang_b(ρ, N)
    return ρ * (1 - PB)

# Plotting γ/μ for different N values
for N in N_values:
    throughput_values = [normalized_throughput(ρ, N) for ρ in ρ_values]
    plt.plot(ρ_values, throughput_values, label=f'N={N}')

plt.xlabel('ρ (normalized load)')
plt.ylabel('γ/μ (normalized throughput)')
plt.legend()
plt.grid()
plt.title('Normalized Throughput vs. Normalized Load')
plt.show()