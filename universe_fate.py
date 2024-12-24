import numpy as np
import matplotlib.pyplot as plt

# Simulate the impact of varying alpha_t on the fate of the universe
def universe_fate(alpha_t):
    # Example model: stronger alpha_t leads to Big Rip, weaker alpha_t leads to Big Freeze
    big_rip = np.exp(1 / alpha_t)  # Exponentially accelerated expansion
    big_freeze = np.log(alpha_t)  # Slower expansion towards a Big Freeze
    return big_rip, big_freeze

# Range of alpha_t values (varying from 0.9 to 1.1)
alpha_t_values = np.linspace(0.9, 1.1, 100)

# Calculate fate outcomes for these alpha_t values
big_rip_values, big_freeze_values = universe_fate(alpha_t_values)

# Plotting Big Rip and Big Freeze Outcomes
plt.figure(figsize=(8, 6))
plt.plot(alpha_t_values, big_rip_values, label="Big Rip", color='red')
plt.plot(alpha_t_values, big_freeze_values, label="Big Freeze", color='blue')
plt.title("Ultimate Fate of the Universe vs. Fine-Structure Constant (\( \alpha_t \))")
plt.xlabel("Fine-Structure Constant (\( \alpha_t \))")
plt.ylabel("Outcome (arbitrary units)")
plt.legend()
plt.grid(True)
plt.show()
