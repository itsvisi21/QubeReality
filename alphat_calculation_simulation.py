import numpy as np
import matplotlib.pyplot as plt

# Constants
e_base = 1.602e-19  # Electron charge (Coulombs)
epsilon_0_base = 8.854e-12  # Permittivity of free space (F/m)
hbar_base = 1.055e-34  # Reduced Planck's constant (J·s)
c_base = 3.0e8  # Speed of light (m/s)

# Function to calculate alpha_t based on varying constants
def calculate_alpha_t(e, epsilon_0, hbar, c):
    return (e**2) / (4 * np.pi * epsilon_0 * hbar * c)

# Varying constants
e_values = np.linspace(e_base * 0.9, e_base * 1.1, 100)  # Vary electron charge (10% change)
epsilon_0_values = np.linspace(epsilon_0_base * 0.9, epsilon_0_base * 1.1, 100)  # Vary epsilon_0
hbar_values = np.linspace(hbar_base * 0.9, hbar_base * 1.1, 100)  # Vary Planck's constant
c_values = np.linspace(c_base * 0.9, c_base * 1.1, 100)  # Vary speed of light

# Calculate alpha_t for each variation
alpha_t_e = np.array([calculate_alpha_t(e, epsilon_0_base, hbar_base, c_base) for e in e_values])
alpha_t_epsilon_0 = np.array([calculate_alpha_t(e_base, epsilon_0, hbar_base, c_base) for epsilon_0 in epsilon_0_values])
alpha_t_hbar = np.array([calculate_alpha_t(e_base, epsilon_0_base, hbar, c_base) for hbar in hbar_values])
alpha_t_c = np.array([calculate_alpha_t(e_base, epsilon_0_base, hbar_base, c) for c in c_values])

# Plotting the results
plt.figure(figsize=(12, 8))

# Plot for varying electron charge (e)
plt.subplot(2, 2, 1)
plt.plot(e_values, alpha_t_e, label=r'$\alpha_t$ vs $e$', color='b')
plt.title(r'$\alpha_t$ vs Electron Charge $e$')
plt.xlabel('Electron Charge $e$ (C)')
plt.ylabel(r'$\alpha_t$')
plt.grid(True)

# Plot for varying permittivity of free space (epsilon_0)
plt.subplot(2, 2, 2)
plt.plot(epsilon_0_values, alpha_t_epsilon_0, label=r'$\alpha_t$ vs $\epsilon_0$', color='g')
plt.title(r'$\alpha_t$ vs Permittivity of Free Space $\epsilon_0$')
plt.xlabel('Permittivity of Free Space $\epsilon_0$ (F/m)')
plt.ylabel(r'$\alpha_t$')
plt.grid(True)

# Plot for varying Planck's constant (hbar)
plt.subplot(2, 2, 3)
plt.plot(hbar_values, alpha_t_hbar, label=r'$\alpha_t$ vs $\hbar$', color='r')
plt.title(r'$\alpha_t$ vs Planck\'s Constant $\hbar$')
plt.xlabel('Planck\'s Constant $\hbar$ (J·s)')
plt.ylabel(r'$\alpha_t$')
plt.grid(True)

# Plot for varying speed of light (c)
plt.subplot(2, 2, 4)
plt.plot(c_values, alpha_t_c, label=r'$\alpha_t$ vs $c$', color='m')
plt.title(r'$\alpha_t$ vs Speed of Light $c$')
plt.xlabel('Speed of Light $c$ (m/s)')
plt.ylabel(r'$\alpha_t$')
plt.grid(True)

# Adjust layout and show plot
plt.tight_layout()
plt.show()
