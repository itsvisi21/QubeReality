import numpy as np
import matplotlib.pyplot as plt

# Constants
alpha_t_base = 1.0  # Base value of the fine-structure constant (no variation)
time = np.linspace(0, 15, 100)  # Time from present to 15 billion years (arbitrary units)

# Function to simulate the recalibration of constants based on varying alpha_t
def recalibrate_constants(alpha_t, time):
    # Recalibration model for constants
    c = 3e8 * (alpha_t / alpha_t_base)  # Speed of light (in m/s), varies with alpha_t
    G = 6.67430e-11 * (alpha_t / alpha_t_base)  # Gravitational constant (m^3 kg^-1 s^-2), varies with alpha_t
    alpha = 1/137 * (alpha_t / alpha_t_base)  # Electromagnetic coupling constant, varies with alpha_t
    
    # Returning recalibrated constants as arrays over time
    return c * np.ones_like(time), G * np.ones_like(time), alpha * np.ones_like(time)

# Varying alpha_t over time (for simplicity, assume alpha_t varies linearly)
alpha_t_values = np.linspace(0.95, 1.05, 5)  # alpha_t varies between 0.95 to 1.05

# Plotting the recalibration of constants
plt.figure(figsize=(12, 8))

for alpha_t in alpha_t_values:
    c, G, alpha = recalibrate_constants(alpha_t, time)
    
    # Plotting recalibrated constants over time
    plt.plot(time, c / 1e8, label=f'c (alpha_t = {alpha_t:.2f})')  # Speed of light (in units of 10^8 m/s)
    plt.plot(time, G * 1e10, label=f'G (alpha_t = {alpha_t:.2f})')  # Gravitational constant (scaled for visibility)
    plt.plot(time, alpha * 137, label=f'α (alpha_t = {alpha_t:.2f})')  # Electromagnetic coupling constant (scaled)

# Labels and title
plt.title('Recalibration of Constants with Varying \( \alpha_t \)')
plt.xlabel('Time (arbitrary units)')
plt.ylabel('Recalibrated Constants (scaled)')
plt.legend()
plt.grid(True)
plt.show()
