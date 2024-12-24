import numpy as np
import matplotlib.pyplot as plt

# Constants
e = 1.602e-19  # Electron charge in Coulombs
epsilon_0 = 8.854e-12  # Vacuum permittivity in F/m (farads per meter)
h = 6.626e-34  # Planck's constant in Joule-seconds
m_e = 9.109e-31  # Electron mass in kg

# Function to calculate Bohr radius for varying alpha_t
def bohr_radius(alpha_t):
    # Formula for Bohr radius
    a_0 = (epsilon_0 * h**2) / (np.pi * m_e * e**2 * alpha_t)
    return a_0

# Function to calculate energy levels for varying alpha_t
def energy_levels(alpha_t):
    # Energy levels of hydrogen (in eV), depending on alpha_t
    energy = -13.6 * (alpha_t**2) / (np.array([1, 2, 3, 4, 5])**2)  # Energy levels for n = 1 to 5
    return energy

# Range of alpha_t values (varying from 0.9 to 1.1)
alpha_t_values = np.linspace(0.9, 1.1, 100)

# Calculate Bohr radius and energy levels for these alpha_t values
bohr_radii = bohr_radius(alpha_t_values)
energy_values = np.array([energy_levels(alpha) for alpha in alpha_t_values])

# Plotting Bohr radius as a function of alpha_t
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.plot(alpha_t_values, bohr_radii, label="Bohr Radius", color='blue')
plt.title("Bohr Radius vs. Fine-Structure Constant (\( \alpha_t \))")
plt.xlabel("Fine-Structure Constant (\( \alpha_t \))")
plt.ylabel("Bohr Radius (m)")
plt.grid(True)

# Plotting Energy levels as a function of alpha_t
plt.subplot(1, 2, 2)
for i in range(5):
    plt.plot(alpha_t_values, energy_values[:, i], label=f"n = {i+1}")

plt.title("Energy Levels vs. Fine-Structure Constant (\( \alpha_t \))")
plt.xlabel("Fine-Structure Constant (\( \alpha_t \))")
plt.ylabel("Energy (eV)")
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()
