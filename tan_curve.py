# Generate a tan curve in the range of 0 <= x <= 360
import numpy as np
import matplotlib.pyplot as plt

# Calculate the tan values from a range of degrees
degrees_range = np.arange(0, 360, 1)
radians = np.deg2rad(degrees_range)
y = np.tan(radians)

# Plot the graph
plt.plot(degrees_range, y, color="green")
plt.xlabel("degrees")
plt.ylabel("tan")
plt.grid(True)
plt.show()