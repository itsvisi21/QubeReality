import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Constants
L = 1  # Length of the string (normalized)
n_modes = 5  # Number of vibrational modes (we will simulate the first few)

# Create a grid for time and space
t = np.linspace(0, 2 * np.pi, 100)  # Time variable (for simplicity, we simulate one period)
x = np.linspace(0, L, 200)  # Space variable (position along the string)
X, T = np.meshgrid(x, t)  # Create a meshgrid for space-time

# Vibrational modes (sine waves with different frequencies)
def string_vibration(x, t, n_modes):
    vibration = np.zeros_like(t)
    for n in range(1, n_modes + 1):
        # Each mode has a different frequency, with the nth mode having n times the frequency
        vibration += np.sin(n * np.pi * x / L) * np.cos(n * np.pi * t)
    return vibration

# Simulate the string vibration in 3D (space and time)
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Calculate the vibration for each time point and plot it in 3D
Z = string_vibration(X, T, n_modes)  # String displacement in space-time

# Plotting the string vibration
ax.plot_surface(X, T, Z, cmap='viridis', edgecolor='none')
ax.set_title("Simplified String Vibration in Multiple Dimensions")
ax.set_xlabel("Space (x)")
ax.set_ylabel("Time (t)")
ax.set_zlabel("Displacement (z)")

plt.show()
