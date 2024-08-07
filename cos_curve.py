# Generate a cos curve in the range of 0 <= x <= 360
import numpy as np
import matplotlib.pyplot as plt

# Calculate the cos values from a range of degrees
degrees_range = np.arange(0, 361, 1)
radians = np.deg2rad(degrees_range)
y = np.cos(radians)

# Plot the graph
plt.plot(degrees_range, y, color="green")
plt.xlabel("degrees")
plt.ylabel("cos")
plt.grid()
plt.show()