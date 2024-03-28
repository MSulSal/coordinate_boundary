from typing import List
import matplotlib.pyplot as plt
import numpy as np

points_x = np.random.uniform(-1000, 1000, 50)
points_y = np.random.uniform(-1000, 1000, 50)
min_x = min(points_x)
max_x = max(points_x)
min_y = min(points_y)
max_y = max(points_y)

figure, axes = plt.subplots()

# plot co-ordinates
plt.scatter(points_x, points_y)

#plot boundaries created by minimum and maximum x and y values
plt.plot([min_x, min_y], [-6000, 6000])
plt.plot([max_x, max_x], [-6000, 6000])
plt.plot([-6000, 6000], [min_y, min_y])
plt.plot([-6000, 6000], [max_y, max_y])
plt.plot([min_x, max_x], [min_y, max_y])


# plot tightest circular boundary around co-ordinates
radius = ((((max_x - min_x) ** 2) + ((max_y - min_y) ** 2)) ** 0.5) / 2
tup = (((max_x + min_x) / 2), ((max_y + min_y) / 2))

axes.set_xlim([-6000, 6000])
axes.set_ylim([-6000, 6000])
axes.add_artist(plt.Circle(tup, radius, facecolor="none", edgecolor="black"))

plt.show()

