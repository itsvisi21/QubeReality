import numpy as np
import matplotlib.pyplot as plt

# Constants for Large-Scale Structures Simulation
galaxy_clustering = np.exp(-np.linspace(0, 5, 100)) * (1 + 0.05 * np.random.randn(100))  # Simulated galaxy clustering effect
dark_matter_distribution = np.exp(-np.linspace(0, 5, 100)) * (1 + 0.03 * np.random.randn(100))  # Simulated dark matter effect

# Plotting the results for both galaxy clustering and dark matter distribution
plt.figure(figsize=(10, 6))
plt.plot(galaxy_clustering, label='Galaxy Clustering')
plt.plot(dark_matter_distribution, label='Dark Matter Distribution', linestyle='--')
plt.title('Impact of Alpha_t Variability on Large-Scale Structures', fontsize=14)
plt.xlabel('Simulation Step', fontsize=12)
plt.ylabel('Density', fontsize=12)
plt.grid(True)
plt.legend()
plt.tight_layout()

# Save the plot as an image file
plt.savefig('large_scale_structures.png')

# Show the plot
plt.show()
