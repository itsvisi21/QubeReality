# Second simulation: Gravitational Wave Propagation
import numpy as np
import matplotlib.pyplot as plt

# Define parameters for edge-length variability and gravitational wave properties
edge_length = np.linspace(1, 10, 100)  # Edge lengths (arbitrary units)
wave_amplitude = edge_length**-1.5  # Hypothetical amplitude behavior
wave_frequency = edge_length**0.5  # Hypothetical frequency behavior

# Plot amplitude vs. edge length
plt.figure(figsize=(8, 6))
plt.plot(edge_length, wave_amplitude, label="Wave Amplitude", color='blue')
plt.xlabel("Edge Length (arbitrary units)")
plt.ylabel("Wave Amplitude (arbitrary units)")
plt.title("Gravitational Wave Amplitude vs Edge Length")
plt.legend()
plt.grid()
amplitude_output_path = "./figures/gravitational_wave_amplitude.png"
plt.savefig(amplitude_output_path)
plt.show()

# Plot frequency vs. edge length
plt.figure(figsize=(8, 6))
plt.plot(edge_length, wave_frequency, label="Wave Frequency", color='green')
plt.xlabel("Edge Length (arbitrary units)")
plt.ylabel("Wave Frequency (arbitrary units)")
plt.title("Gravitational Wave Frequency vs Edge Length")
plt.legend()
plt.grid()
frequency_output_path = "./figures/gravitational_wave_frequency.png"
plt.savefig(frequency_output_path)
plt.show()

amplitude_output_path, frequency_output_path
