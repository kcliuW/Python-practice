import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Create figure and 3D axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d') # type: ignore

# Set sphere parameters
r1 = 5      # radius of sphere 1
r2 = 5      # radius of sphere 2
c1 = (0, 0, 10)   # center of sphere 1
c2 = (15, 0, 10)   # center of sphere 2

# Create sphere surfaces
u, v = np.mgrid[0:2*np.pi:20j, 0:np.pi:10j]
x1 = c1[0] + r1 * np.sin(u) * np.cos(v)
y1 = c1[1] + r1 * np.sin(u) * np.sin(v)
z1 = c1[2] + r1 * np.cos(u)
x2 = c2[0] + r2 * np.sin(u) * np.cos(v)
y2 = c2[1] + r2 * np.sin(u) * np.sin(v)
z2 = c2[2] + r2 * np.cos(u)

# Plot sphere surfaces
ax.plot_surface(x1, y1, z1, color='blue')
ax.plot_surface(x2, y2, z2, color='red')

# Set axis limits and labels
ax.set_xlim([-10, 20])
ax.set_ylim([-10, 20])
ax.set_zlim([-10, 20])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Show plot
plt.show()