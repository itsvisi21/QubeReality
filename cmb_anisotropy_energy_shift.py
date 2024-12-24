# Fifth simulation: Cosmic Microwave Background (CMB) Anisotropies
import numpy as np
import matplotlib.pyplot as plt

# Simulating CMB anisotropy patterns based on tetrahedron dynamics
energy_shift = np.linspace(0.1, 1.0, 100)  # Hypothetical energy shift values (arbitrary units)
cmb_anisotropy = np.sin(2 * np.pi * energy_shift) * np.exp(-energy_shift)  # Simplified anisotropy behavior

# Plot CMB anisotropy vs energy shift
plt.figure(figsize=(8, 6))
plt.plot(energy_shift, cmb_anisotropy, label="CMB Anisotropy", color='red')
plt.xlabel("Energy Shift (arbitrary units)")
plt.ylabel("CMB Anisotropy (arbitrary units)")
plt.title("CMB Anisotropy vs Energy Shift")
plt.legend()
plt.grid()
output_path_cmb = "./figures/cmb_anisotropy_energy_shift.png"
plt.savefig(output_path_cmb)
plt.show()

output_path_cmb
