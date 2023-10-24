import numpy as np
import matplotlib.pyplot as plt

# Step 1: Define the equation
def calculate_en(p):
    return (p/(1-p))

# Step 2: Create an array of 'n' values
p_values = np.linspace(0, 1,50)  # Adjust the range as needed

# Step 3: Calculate 'pn' values for each 'n'
en_values = [calculate_en(p) for p in p_values]

# Step 4: Create the plot
plt.plot(p_values, en_values, marker='o', linestyle='-')
plt.xlabel('p')
plt.ylabel('en')
plt.title('Plot of (en)')
plt.grid(True)
plt.show()