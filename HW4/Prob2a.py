import numpy as np
import matplotlib.pyplot as plt

# Step 1: Define the equation
def calculate_pn(n):
    return (1 - 0.8) * (0.8 ** n)

# Step 2: Create an array of 'n' values
n_values = np.arange(0, 21)  # Adjust the range as needed

# Step 3: Calculate 'pn' values for each 'n'
pn_values = [calculate_pn(n) for n in n_values]

# Step 4: Create the plot
plt.plot(n_values, pn_values, marker='o', linestyle='-')
plt.xlabel('n')
plt.ylabel('pn')
plt.title('Plot of pn = (1 - 0.8) * 0.8^n')
plt.grid(True)
plt.show()