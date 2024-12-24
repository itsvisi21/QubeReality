import numpy as np
import matplotlib.pyplot as plt

# Constants for Intergalactic Magnetic Fields Simulation
magnetic_field_strength = np.exp(-np.linspace(0, 5, 100)) * (1 + 0.07 * np.random.randn(100))  # Simulated magnetic field strength

# Plotting the results
plt.figure(figsize=(10, 6))
plt.plot(magnetic_field_strength, label='Magnetic Field Strength')
plt.title('Impact of Alpha_t Variability on Intergalactic Magnetic Fields', fontsize=14)
plt.xlabel('Simulation Step', fontsize=12)
plt.ylabel('Magnetic Field Strength (nG)', fontsize=12)
plt.grid(True)
plt.legend()
plt.tight_layout()

# Save the plot as an image file
plt.savefig('intergalactic_magnetic_fields.png')

# Show the plot
plt.show()
