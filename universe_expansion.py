import numpy as np
import matplotlib.pyplot as plt

# Simulate the effect of varying alpha_t on cosmic expansion rate
def cosmic_expansion_rate(alpha_t):
    # Example model: expansion rate proportional to 1/alpha_t
    return 70 * (1 / alpha_t)  # Arbitrary units for expansion rate

# Range of alpha_t values (varying from 0.9 to 1.1)
alpha_t_values = np.linspace(0.9, 1.1, 100)

# Calculate cosmic expansion rates for these alpha_t values
expansion_values = cosmic_expansion_rate(alpha_t_values)

# Plotting Cosmic Expansion Rate vs. alpha_t
plt.figure(figsize=(8, 6))
plt.plot(alpha_t_values, expansion_values, label="Cosmic Expansion Rate")
plt.title("Cosmic Expansion Rate vs. Fine-Structure Constant (\( \alpha_t \))")
plt.xlabel("Fine-Structure Constant (\( \alpha_t \))")
plt.ylabel("Cosmic Expansion Rate (km/s/Mpc)")
plt.grid(True)
plt.legend()
plt.show()
