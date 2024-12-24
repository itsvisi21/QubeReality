# Sixth simulation: High-Redshift Spectral Shifts
import numpy as np
import matplotlib.pyplot as plt

# Simulating spectral shifts based on tetrahedron energy transitions and environmental factors
redshift = np.linspace(0.1, 3.0, 100)  # Hypothetical redshift values (arbitrary units)
spectral_shift = 1 / (1 + redshift) * np.exp(-0.2 * redshift)  # Simplified spectral shift formula

# Plot spectral shift vs redshift
plt.figure(figsize=(8, 6))
plt.plot(redshift, spectral_shift, label="Spectral Shift", color='blue')
plt.xlabel("Redshift (arbitrary units)")
plt.ylabel("Spectral Shift (arbitrary units)")
plt.title("Spectral Shift vs Redshift")
plt.legend()
plt.grid()
output_path_spectral_shift = "./figures/spectral_shift_redshift.png"
plt.savefig(output_path_spectral_shift)
plt.show()

output_path_spectral_shift
