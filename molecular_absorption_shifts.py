import numpy as np
import matplotlib.pyplot as plt

# Constants for the simulation
alpha_t_initial = 1  # Initial value of fine-structure constant (dimensionless)
wavelength_initial = 1000  # Initial molecular absorption wavelength in nm (example)
alpha_t_variations = np.linspace(0.9, 1.1, 100)  # Simulating variations of alpha_t from 0.9 to 1.1

# Calculate the shift in wavelength due to variations in alpha_t (simplified model)
# The formula assumes the shift in wavelength is proportional to the variation in alpha_t
wavelength_shifts = wavelength_initial * (1 - alpha_t_initial / alpha_t_variations)

# Plotting the results
plt.figure(figsize=(10, 6))
plt.plot(alpha_t_variations, wavelength_shifts, label='Shift in Wavelength for H2')
plt.title('Impact of Alpha_t Variability on Molecular Absorption Line Shifts (H2)', fontsize=14)
plt.xlabel('Alpha_t Variability', fontsize=12)
plt.ylabel('Shift in Wavelength (nm)', fontsize=12)
plt.grid(True)
plt.legend()
plt.tight_layout()

# Save the plot as an image file
plt.savefig('molecular_absorption_shifts.png')

# Show the plot
plt.show()
