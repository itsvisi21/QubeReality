# Fourth simulation: Cosmic Clustering and Structure Formation
import numpy as np
import matplotlib.pyplot as plt

# Simulating clustering behavior based on energy flux and tetrahedron dynamics
alpha_t = np.linspace(0.1, 1.0, 100)  # Hypothetical alpha_t values (arbitrary units)
clustering_index = np.log(1 + alpha_t**2)  # Hypothetical clustering behavior formula

# Plot clustering index vs alpha_t
plt.figure(figsize=(8, 6))
plt.plot(alpha_t, clustering_index, label="Clustering Index", color='orange')
plt.xlabel("Alpha_t (arbitrary units)")
plt.ylabel("Clustering Index (arbitrary units)")
plt.title("Cosmic Clustering vs Alpha_t Variability")
plt.legend()
plt.grid()
output_path_clustering = "./figures/cosmic_clustering_alpha_t.png"
plt.savefig(output_path_clustering)
plt.show()

output_path_clustering
