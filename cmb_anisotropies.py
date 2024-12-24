import numpy as np
import matplotlib.pyplot as plt

# Constants for CMB Anisotropies Simulation
alpha_t_variability = np.linspace(0.9, 1.1, 100)
delta_alpha_t = alpha_t_variability - 1  # Variations from the initial alpha_t = 1
temperature_fluctuations = 10 * delta_alpha_t * np.sin(np.linspace(0, 2 * np.pi, 100))  # Simulated temperature fluctuations

# Plotting the results
plt.figure(figsize=(10, 6))
plt.plot(alpha_t_variability, temperature_fluctuations, label='Temperature Fluctuations in CMB')
plt.title('Impact of Alpha_t Variability on CMB Anisotropies', fontsize=14)
plt.xlabel('Alpha_t Variability', fontsize=12)
plt.ylabel('Temperature Fluctuations (µK)', fontsize=12)
plt.grid(True)
plt.legend()
plt.tight_layout()

# Save the plot as an image file
plt.savefig('cmb_anisotropies.png')

# Show the plot
plt.show()
