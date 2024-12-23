# Reinitialize parameters for clustering simulation
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
import matplotlib.animation as animation

# Define parameters
large_grid_size = 100  # Grid size for clustering
time_steps_evolution = 50  # Number of time steps
initial_density_contrast = 1e-3  # Initial density contrast

# Initialize the density grid
density_evolution_grid = np.random.rand(large_grid_size, large_grid_size, large_grid_size)
density_evolution_grid *= initial_density_contrast  # Apply initial contrast

# Simulate temporal evolution of clustering
density_evolution_frames = []  # Store 2D projections for animation

for t in range(time_steps_evolution):
    # Update density grid: apply random small perturbations to simulate evolution
    density_evolution_grid += initial_density_contrast * np.random.rand(
        large_grid_size, large_grid_size, large_grid_size
    ) * 0.01  # Small perturbations
    
    # Save 2D projection (sum along the z-axis) for visualization
    frame = np.sum(density_evolution_grid, axis=2)
    density_evolution_frames.append(frame)

# Create an animation
fig, ax = plt.subplots(figsize=(8, 8))
im = ax.imshow(density_evolution_frames[0], cmap=cm.inferno, origin="lower")
title = ax.set_title("Clustering Evolution - Time Step 1")

# Update function for animation
def update(frame_idx):
    im.set_data(density_evolution_frames[frame_idx])  # Update the image data
    title.set_text(f"Clustering Evolution - Time Step {frame_idx + 1}")
    return im, title

# Create the animation
ani = animation.FuncAnimation(
    fig, update, frames=len(density_evolution_frames), interval=100, blit=False
)

# Save the animation to a file
animation_file_path = "galaxy_clustering_evolution.mp4"
ani.save(animation_file_path, writer="ffmpeg")

plt.close(fig)

# Provide the file location for download
animation_file_path
