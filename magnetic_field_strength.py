# Third simulation: Magnetic Polarity Interactions
import numpy as np
import matplotlib.pyplot as plt

# Simulating magnetic field strength based on vertex charge and distance
vertex_charge = np.linspace(1, 10, 100)  # Hypothetical magnetic charge values
field_strength = vertex_charge**2 / (vertex_charge + 1)  # Simplified field strength formula

# Plot the magnetic field strength as a function of vertex charge
plt.figure(figsize=(8, 6))
plt.plot(vertex_charge, field_strength, label="Field Strength", color='purple')
plt.xlabel("Vertex Magnetic Charge (arbitrary units)")
plt.ylabel("Field Strength (arbitrary units)")
plt.title("Magnetic Field Strength vs Vertex Magnetic Charge")
plt.legend()
plt.grid()
output_path_magnetic_field = "./figures/magnetic_field_strength.png"
plt.savefig(output_path_magnetic_field)
plt.show()

output_path_magnetic_field
