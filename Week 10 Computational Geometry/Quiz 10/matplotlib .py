# an example related to computational geometry

import matplotlib.pyplot as plt

# First some simple text output.
vertices = [(0, 0), (100, 0), (1, 50), (100, 100), (0, 100), (0,0)]
vx, vy = zip(*vertices)  # Unpack them
points = [(1, 1), (20, 20), (20, 80), (60, 50),
     (97, 1), (1, 48), (1, 52), (97, 99), (1, 99)]
px, py = zip(*points) # Unpack
print("Vertex x values:", vx)
print("Vertex y values:", vy)
print("Point x values:", px)
print("Point y values:", py)

# Now a matplotlib graph
axes = plt.axes()
axes.plot(vx, vy, color='blue', marker='o', linestyle='--')
axes.plot(px, py, color='red', marker='x', linestyle='')
axes.set_title('The example from the geometry lecture notes')
plt.show()
