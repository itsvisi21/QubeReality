# First simulation: Tetrahedron Energy Dynamics
import numpy as np
import matplotlib.pyplot as plt

# Parameters for the tetrahedron
edge_length = np.linspace(1, 10, 100)  # Edge lengths (arbitrary units)
energy_distribution = 1 / edge_length**2  # Hypothetical energy distribution formula

# Plot the energy distribution
plt.figure(figsize=(8, 6))
plt.plot(edge_length, energy_distribution, label="Energy Distribution")
plt.xlabel("Edge Length (arbitrary units)")
plt.ylabel("Energy (arbitrary units)")
plt.title("Tetrahedron Energy Distribution vs Edge Length")
plt.legend()
plt.grid()
# Save the figure for integration into LaTeX
output_path = "./figures/tetrahedron_energy_distribution.png"
plt.savefig(output_path)
plt.show()

output_path
