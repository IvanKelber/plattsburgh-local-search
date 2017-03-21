# Created by Ivan Kelber, March 2017

'''
This file runs localSearch on the function 'circles()' defined in circle.py.
It aims to minimize the output of the circles() while providing some visual
feedback so the user can observe what is happening at each step.

It's important to note that we are not simply running local search for a long time
but rather running local search with different proposal functions and different
epsilons.  This allows us to have a more robust search technique and more control
over the improvement window.
'''

import random
import math
import sys
import time

# Set up graphics
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

#Globals for graphics
fig, ax = plt.subplots()
PATCHES = []

#Parameters for local search
PROPOSALS = [
    wideScaleRandomNoise,
    wideScaleRandomNoiseSingleCoordinate,
    singleRandomNoise,
]
EPSILONS = [0.05,0.03,0.04,0.02,0.01] # The order of the epsilons to try.
SECONDS_PER_SEARCH = .5  # The number of seconds to run local search for each set of parameters
PER_EPSILON = 5 # The number of times to try each epsilon

#Point generation parameters
WINDOW_SIZE = 500
MARGIN = 0
NUM_POINTS = 10
POINTS = [(random.randrange(MARGIN,WINDOW_SIZE-MARGIN),random.randrange(MARGIN,WINDOW_SIZE-MARGIN)) for i in range(NUM_POINTS)]


def plot(points):
    '''
    Plots each circle using matplotlib.  Colors them prettily. :)
    '''
    clear()
    global PATCHES
    for radius,point in enumerate(points):
        circle = mpatches.Circle(list(point), radius, ec="none")
        PATCHES.append(circle)
    colors = np.linspace(0, 1, len(PATCHES))
    collection = PatchCollection(PATCHES, cmap=plt.cm.hsv, alpha=.4)
    collection.set_array(np.array(colors))
    ax.add_collection(collection)
    # draw_bounding_box(points) # uncomment this line to draw the bounding box at each step
    plt.axis('equal')
    plt.pause(.01)

def clear():
    '''
    Clears the plot.
    '''
    global PATCHES
    PATCHES = []
    plt.cla()

def draw_bounding_box(points):
    '''
    Draws the bounding square around the circles.  Note that this can bug
    sometimes and the square appears shifted some set amount in one direction.
    '''
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

    rectangle = mpatches.Rectangle((minX,minY),side,side,fill=False)
    PATCHES.append(rectangle)
    ax.add_patch(rectangle)

def main():
    plt.ion()

    plot(POINTS)
    raw_input("Press enter to continue:")

    epsilons = EPSILONS
    xp = POINTS
    bestSoFar = xp
    print "Starting Guess: %.10f" % circles(POINTS)
    start = time.clock()

    # ======== Begin Local Search =========
    # We try different epsilons as time goes on.  This allows us to first explore
    # and then once we are pretty sure we are searching in a 'good' valley
    # we can begin to narrow in on the optimum
    for eps in epsilons:
        print "Searching for epsilon " + str(eps)
        for i in range(PER_EPSILON):
            plot(xp)
            # Randomly choose one of the proposals to use.
            xp = localSearch(circles,random.choice(PROPOSALS),xp,eps,SECONDS_PER_SEARCH)
            if(circles(xp) <= circles(bestSoFar)):
                bestSoFar = xp
        print ". . . Best for epsilon %.2f: %.10f" %(eps, circles(bestSoFar))
    # ======== End Local Search ==========

    print "==============="
    print "Original: ", circles(POINTS)
    print "Best: ", circles(bestSoFar)
    end = time.clock()
    plot(bestSoFar)
    draw_bounding_box(bestSoFar)

    raw_input("Took %.4f seconds. Press enter to close:" % (end-start))


if __name__ == '__main__':
    main()
