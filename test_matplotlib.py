"""
Reference for matplotlib artists

This example displays several of matplotlib's graphics primitives (artists)
drawn using matplotlib API. A full list of artists and the documentation is
available at http://matplotlib.org/api/artist_api.html.

Copyright (c) 2010, Bartosz Telenczuk
BSD License
"""
import random

import matplotlib as mpl
mpl.rcParams['toolbar'] = 'None'
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import matplotlib.patches as mpatches
from matplotlib.collections import PatchCollection



fig, ax = plt.subplots()
# create 3x3 grid to plot the artists
grid = np.mgrid[0.2:0.8:3j, 0.2:0.8:3j].reshape(2, -1).T

patches = []

# add a circle
# for i in range(10):
#     circle = mpatches.Circle([random.random()*100,random.random()*100], 1, ec="none")
#     patches.append(circle)

# add a rectangle
# rect = mpatches.Rectangle(grid[1] - [0.025, 0.05], 0.05, 0.1, ec="none")
# patches.append(rect)
# label(grid[1], "Rectangle")
#

x, y = np.array([[1,2],[2,1]])
line = mlines.Line2D(x, y, lw=1, alpha=1,color='black')


# colors = np.linspace(0, 1, len(patches))
collection = PatchCollection(patches, cmap=plt.cm.hsv, alpha=.4)
# collection.set_array(np.array(colors))
ax.add_collection(collection)
ax.add_line(line)


# plt.subplots_adjust(left=0, right=1, bottom=0, top=1)
plt.axis('equal')
# plt.axis('off')

plt.show()
