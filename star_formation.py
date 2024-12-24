import numpy as np
import matplotlib.pyplot as plt

# Simulate the effect of varying alpha_t on star formation rate
def star_formation_rate(alpha_t):
    # Example model: star formation rate inversely related to alpha_t (as an example)
    return 100 * (1 / alpha_t)

# Range of alpha_t values (varying from 0.9 to 1.1)
alpha_t_values = np.linspace(0.9, 1.1, 100)

# Calculate star formation rates for these alpha_t values
star_formation_values = star_formation_rate(alpha_t_values)

# Plotting Star Formation Rate vs. alpha_t
plt.figure(figsize=(8, 6))
plt.plot(alpha_t_values, star_formation_values, label="Star Formation Rate")
plt.title("Star Formation Rate vs. Fine-Structure Constant (\( \alpha_t \))")
plt.xlabel("Fine-Structure Constant (\( \alpha_t \))")
plt.ylabel("Star Formation Rate (arbitrary units)")
plt.grid(True)
plt.legend()
plt.show()
