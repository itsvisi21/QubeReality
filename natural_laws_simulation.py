import numpy as np
import matplotlib.pyplot as plt

# Constants
e_base = 1.602e-19  # Electron charge (Coulombs)
epsilon_0_base = 8.854e-12  # Permittivity of free space (F/m)
hbar_base = 1.055e-34  # Reduced Planck's constant (J·s)
c_base = 3.0e8  # Speed of light (m/s)
G_base = 6.67430e-11  # Gravitational constant (m^3 kg^-1 s^-2)

# Function to calculate alpha_t based on varying constants
def calculate_alpha_t(e, epsilon_0, hbar, c):
    return (e**2) / (4 * np.pi * epsilon_0 * hbar * c)

# Varying alpha_t for different constants
alpha_t_values = np.linspace(0.95, 1.05, 100)  # Vary alpha_t by ±5%

# Newton's laws of motion: F = ma
mass = 1.0  # kg (mass of an object)
acceleration = 9.8  # m/s^2 (acceleration due to gravity)
force_base = mass * acceleration  # Base force in Newtons (F = ma)

# Gravitational force: F = G * (m1 * m2) / r^2
m1 = 5.97e24  # mass of Earth (kg)
m2 = 1.0  # arbitrary mass (kg)
r = 6.37e6  # radius of Earth (m)
gravitational_force_base = G_base * (m1 * m2) / r**2  # Base gravitational force

# Electromagnetic force: F = k * (q1 * q2) / r^2
q1 = e_base  # electron charge (C)
q2 = e_base  # arbitrary charge (C)
r_em = 1e-10  # distance between charges (m)
k = 8.99e9  # Coulomb constant (N·m^2/C^2)
electromagnetic_force_base = k * (q1 * q2) / r_em**2  # Base electromagnetic force

# Arrays to hold recalibrated forces
force_recalibrated_newton = []
force_recalibrated_gravity = []
force_recalibrated_em = []

# Calculate recalibrated forces for varying alpha_t
for alpha_t in alpha_t_values:
    # Recalibrate constants for varying alpha_t
    e = e_base * alpha_t
    epsilon_0 = epsilon_0_base * alpha_t
    hbar = hbar_base * alpha_t
    c = c_base * alpha_t
    G = G_base * alpha_t
    
    # Recalculate alpha_t for the recalibrated constants
    alpha_t_recalculated = calculate_alpha_t(e, epsilon_0, hbar, c)
    
    # Recalibrate Newton's law force: F = ma
    force_recalibrated_newton.append(mass * acceleration)
    
    # Recalibrate gravitational force: F = G * (m1 * m2) / r^2
    force_recalibrated_gravity.append(G * (m1 * m2) / r**2)
    
    # Recalibrate electromagnetic force: F = k * (q1 * q2) / r^2
    force_recalibrated_em.append(k * (q1 * q2) / r_em**2)

# Plotting the recalibrated forces as a function of alpha_t
plt.figure(figsize=(12, 8))

# Plot for recalibrated Newton's force
plt.subplot(2, 2, 1)
plt.plot(alpha_t_values, force_recalibrated_newton, label=r'$F_{Newton}$', color='b')
plt.title(r'Recalibrated Newton\'s Law Force with Varying $\alpha_t$')
plt.xlabel(r'$\alpha_t$')
plt.ylabel(r'Recalibrated Force (N)')
plt.grid(True)

# Plot for recalibrated gravitational force
plt.subplot(2, 2, 2)
plt.plot(alpha_t_values, force_recalibrated_gravity, label=r'$F_{Gravity}$', color='g')
plt.title(r'Recalibrated Gravitational Force with Varying $\alpha_t$')
plt.xlabel(r'$\alpha_t$')
plt.ylabel(r'Recalibrated Force (N)')
plt.grid(True)

# Plot for recalibrated electromagnetic force
plt.subplot(2, 2, 3)
plt.plot(alpha_t_values, force_recalibrated_em, label=r'$F_{Electromagnetic}$', color='r')
plt.title(r'Recalibrated Electromagnetic Force with Varying $\alpha_t$')
plt.xlabel(r'$\alpha_t$')
plt.ylabel(r'Recalibrated Force (N)')
plt.grid(True)

# Adjust layout and show plot
plt.tight_layout()
plt.show()
