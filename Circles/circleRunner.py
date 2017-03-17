#runner
import random
import math
import sys
import time

import matplotlib as mpl
mpl.rcParams['toolbar'] = 'None'
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.collections import PatchCollection


sys.path.append('../') #add parent directory to import path
from basic import localSearch
from circle import circles

from proposals import *

fig, ax = plt.subplots()
PATCHES = []

PROPOSALS = [
    wideScaleRandomNoise,
    wideScaleRandomNoiseSingleCoordinate,
    singleRandomNoise,
]

WINDOW_SIZE = 500
MARGIN = 0
NUM_POINTS = 10
POINT_RADIUS = 1

POINTS = [(random.randrange(MARGIN,WINDOW_SIZE-MARGIN),random.randrange(MARGIN,WINDOW_SIZE-MARGIN)) for i in range(NUM_POINTS)]


def plot(points):
    clear()
    global PATCHES
    for radius,point in enumerate(points):
        circle = mpatches.Circle(list(point), radius, ec="none")
        PATCHES.append(circle)
    colors = np.linspace(0, 1, len(PATCHES))
    collection = PatchCollection(PATCHES, cmap=plt.cm.hsv, alpha=.4)
    collection.set_array(np.array(colors))
    ax.add_collection(collection)
    # draw_bounding_box(points)
    plt.axis('equal')
    # plt.axis('off')

    plt.pause(.01)

def clear():
    global PATCHES
    PATCHES = []
    plt.cla()

def draw_bounding_box(points):
    minX = points[0][0] - 1
    minY = points[0][1] - 1
    maxX = points[1][0] + 1
    maxY = points[1][0] + 1

    for radius,point in enumerate(points):
        minX = min(minX,point[0]-radius)
        minY = min(minY,point[1]-radius)
        maxX = max(maxX,point[0]+radius)
        maxY = max(maxY,point[1]+radius)

    side = circles(points)

    # print side
    rectangle = mpatches.Rectangle((minX,minY),side,side,fill=False)
    PATCHES.append(rectangle)
    ax.add_patch(rectangle)

def main():
    plt.ion()


    plot(POINTS)
    raw_input("Press enter to continue:")

    epsilons = [0.05,0.03,0.04,0.02,0.01]
    xp = POINTS
    bestSoFar = xp
    print "Starting Guess: %.10f" % circles(POINTS)
    start = time.clock()
    for eps in epsilons:
        for i in range(5):
            plot(xp)
            xp = localSearch(circles,random.choice(PROPOSALS),xp,eps,.5)
            if(circles(xp) <= circles(bestSoFar)):
                bestSoFar = xp
        print "Best for epsilon %.2f: %.10f" %(eps, circles(bestSoFar))
    print "=========="
    print "Original: ", circles(POINTS)
    print "Best: ", circles(bestSoFar)
    end = time.clock()
    plot(bestSoFar)
    draw_bounding_box(bestSoFar)


    raw_input("Took %.4f seconds. Press enter to close:" % (end-start))
if __name__ == '__main__':
    main()
