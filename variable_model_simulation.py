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

# Arrays to hold recalibrated forces for both models (fixed and variable)
force_recalibrated_newton_fixed = []
force_recalibrated_gravity_fixed = []
force_recalibrated_em_fixed = []

force_recalibrated_newton_variable = []
force_recalibrated_gravity_variable = []
force_recalibrated_em_variable = []

# Calculate forces for fixed and variable models
for alpha_t in alpha_t_values:
    # Fixed Model: Constants do not change
    e_fixed = e_base
    epsilon_0_fixed = epsilon_0_base
    hbar_fixed = hbar_base
    c_fixed = c_base
    G_fixed = G_base
    
    # Variable Model: Constants vary with alpha_t
    e_variable = e_base * alpha_t
    epsilon_0_variable = epsilon_0_base * alpha_t
    hbar_variable = hbar_base * alpha_t
    c_variable = c_base * alpha_t
    G_variable = G_base * alpha_t
    
    # Recalibrate alpha_t for fixed and variable models
    alpha_t_fixed = calculate_alpha_t(e_fixed, epsilon_0_fixed, hbar_fixed, c_fixed)
    alpha_t_variable = calculate_alpha_t(e_variable, epsilon_0_variable, hbar_variable, c_variable)
    
    # Recalibrate Newton's law force: F = ma
    force_recalibrated_newton_fixed.append(mass * acceleration)
    force_recalibrated_newton_variable.append(mass * acceleration)
    
    # Recalibrate gravitational force: F = G * (m1 * m2) / r^2
    force_recalibrated_gravity_fixed.append(G_fixed * (m1 * m2) / r**2)
    force_recalibrated_gravity_variable.append(G_variable * (m1 * m2) / r**2)
    
    # Recalibrate electromagnetic force: F = k * (q1 * q2) / r^2
    force_recalibrated_em_fixed.append(k * (q1 * q2) / r_em**2)
    force_recalibrated_em_variable.append(k * (q1 * q2) / r_em**2)

# Plotting the recalibrated forces for both models
plt.figure(figsize=(12, 8))

# Plot for recalibrated Newton's force (fixed vs variable)
plt.subplot(2, 2, 1)
plt.plot(alpha_t_values, force_recalibrated_newton_fixed, label=r'Fixed Model $F_{Newton}$', color='b')
plt.plot(alpha_t_values, force_recalibrated_newton_variable, label=r'Variable Model $F_{Newton}$', linestyle='--', color='c')
plt.title(r'Fixed vs Variable Newton\'s Law Force with Varying $\alpha_t$')
plt.xlabel(r'$\alpha_t$')
plt.ylabel(r'Recalibrated Force (N)')
plt.legend()
plt.grid(True)

# Plot for recalibrated gravitational force (fixed vs variable)
plt.subplot(2, 2, 2)
plt.plot(alpha_t_values, force_recalibrated_gravity_fixed, label=r'Fixed Model $F_{Gravity}$', color='g')
plt.plot(alpha_t_values, force_recalibrated_gravity_variable, label=r'Variable Model $F_{Gravity}$', linestyle='--', color='y')
plt.title(r'Fixed vs Variable Gravitational Force with Varying $\alpha_t$')
plt.xlabel(r'$\alpha_t$')
plt.ylabel(r'Recalibrated Force (N)')
plt.legend()
plt.grid(True)

# Plot for recalibrated electromagnetic force (fixed vs variable)
plt.subplot(2, 2, 3)
plt.plot(alpha_t_values, force_recalibrated_em_fixed, label=r'Fixed Model $F_{Electromagnetic}$', color='r')
plt.plot(alpha_t_values, force_recalibrated_em_variable, label=r'Variable Model $F_{Electromagnetic}$', linestyle='--', color='m')
plt.title(r'Fixed vs Variable Electromagnetic Force with Varying $\alpha_t$')
plt.xlabel(r'$\alpha_t$')
plt.ylabel(r'Recalibrated Force (N)')
plt.legend()
plt.grid(True)

# Adjust layout and show plot
plt.tight_layout()
plt.show()
