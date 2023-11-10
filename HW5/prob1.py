import numpy as np
import matplotlib.pyplot as plt

# Define the function
def equation(l):
    return np.log((l / (l + 48)) * (1 - (l + 48) * 1e-5) / (1 + (((0.08 + (l + 48) / 3200) / 9600) - 1) * (l + 48) * 1e-5))
# Generate values for l
l_values = np.linspace(1, 10000, 10000)  # You can adjust the range and number of points as needed

# Calculate the corresponding y values using the equation
y_values = equation(l_values)

# Plot the results
plt.plot(l_values, y_values)
plt.xlabel('l')
plt.ylabel('log10(D/C)')
plt.title('Logarithm of the Equation')
plt.grid(True)
plt.show()
print(1e-5)