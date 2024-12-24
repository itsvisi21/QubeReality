import numpy as np
import matplotlib.pyplot as plt

# Constants for the simulation
time = np.linspace(0, 15, 100)  # Time from the present to 15 billion years (arbitrary units)
alpha_t_values = np.linspace(0.9, 1.1, 5)  # Varying fine-structure constant values

# Function to simulate the cosmic expansion with varying alpha_t
def cosmic_expansion(alpha_t, time):
    # Basic model: expansion rate affected by alpha_t
    expansion_rate = np.exp(alpha_t * time / 10)  # Exponential expansion depending on alpha_t
    return expansion_rate

# Plotting the simulation for varying alpha_t values
plt.figure(figsize=(10, 6))

for alpha_t in alpha_t_values:
    expansion = cosmic_expansion(alpha_t, time)
    plt.plot(time, expansion, label=f'α_t = {alpha_t:.2f}')

plt.title('Simulation of Cosmic Expansion with Varying \( \alpha_t \)')
plt.xlabel('Time (arbitrary units)')
plt.ylabel('Cosmic Expansion Rate (arbitrary units)')
plt.legend()
plt.grid(True)
plt.show()
