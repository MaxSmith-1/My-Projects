#numpy, mathlib

import numpy as np
import matplotlib.pyplot as plt
fig = plt.figure()
ax = plt.axes(projection='3d')

# Generate data for the graph
x = [1, 2, 3, 4, 5]
y = [5, 6, 7, 8, 9]
z = [2, 4, 1, 6, 3]

plt.plot([.1,.1,.1],[.2,.4,.9],[.2,.4,10], linestyle="solid",color="royalblue")

# Show the graph
plt.show()