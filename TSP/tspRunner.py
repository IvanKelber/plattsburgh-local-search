import random
import math
import sys
import time

import matplotlib as mpl
mpl.rcParams['toolbar'] = 'None'
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import matplotlib.patches as mpatches
from matplotlib.collections import PatchCollection

fig, ax = plt.subplots()


sys.path.append('../') #add parent directory to import path
# from graphics import GraphWin,Point,Circle,Line,Rectangle
from basic import localSearch

from proposals import *

PATCHES = []

PROPOSALS = [
    swapPairs,
    swapRandom,
    insertion,
    # swapBeginning,
    # swapLocal,
    # shuffle,
]
RADIUS = 100
NUM_POINTS = 100
POINT_RADIUS = RADIUS/NUM_POINTS


def random_locus():
    return [(random.randrange(0,RADIUS),random.randrange(0,RADIUS)) for i in range(NUM_POINTS)]

def tsp(points):
    total = 0
    for p,q in zip(points,points[1:]):
        total += distance(p,q)
    return total

def circle_locus():
    return [((RADIUS)*(math.sin(i*math.pi*2/NUM_POINTS)+1),(RADIUS)*(math.cos(i*math.pi*2/NUM_POINTS)+1)) for i in range(NUM_POINTS)]

def sin_wave_locus(period):
        return [(i*period*2,(RADIUS)*(math.sin(i*1*math.pi*2*period/NUM_POINTS)+1)) for i in range(NUM_POINTS)]


def distance(p,q):
    return ((q[0]-p[0])**2 + (q[1]-p[1])**2)**.5

def plot(points):

    x_values, y_values = plot_points(points)
    line = mlines.Line2D(x_values, y_values, lw=1, alpha=1,color='black',zorder=1)
    ax.add_line(line)

    plt.axis('equal')
    plt.axis('off')

    plt.pause(.01)

def plot_points(points):
    clear()
    global PATCHES
    x_values = []
    y_values = []
    plot_points = points
    for plot_point_index,point in enumerate(points):
        x_values.append(point[0])
        y_values.append(point[1])
        circle = mpatches.Circle(list(plot_points[plot_point_index]), POINT_RADIUS, ec="none")
        PATCHES.append(circle)
    colors = np.linspace(0, 1, len(PATCHES))
    collection = PatchCollection(PATCHES, color='red', alpha=1,zorder=2)
    # collection.set_array(np.array(colors))
    ax.add_collection(collection)

    return x_values,y_values

def clear():
    global PATCHES
    PATCHES = []
    plt.cla()




def main():
    POINTS = sin_wave_locus(2)
    random.shuffle(POINTS)
    plt.ion()

    epsilons = [100,75,50,40,20,10,10]
    xp = POINTS
    bestSoFar = xp
    print "Starting Guess: %.10f" % tsp(POINTS)
    start = time.clock()
    for eps in epsilons:
        for i in range(5):
            plot(xp)
            xp = localSearch(tsp,random.choice(PROPOSALS),xp,eps,NUM_POINTS/100 + .5)
            if(tsp(xp) <= tsp(bestSoFar)):
                bestSoFar = xp
        print "Best for epsilon %.2f: %.10f" %(eps, tsp(bestSoFar))
    print "=========="
    print "Original: ", tsp(POINTS)
    print "Best: ", tsp(bestSoFar)
    print "Actual Best: ", 2*(RADIUS)*math.pi
    end = time.clock()
    plot(bestSoFar)

    raw_input("Took %.4f seconds. Press enter to close:" % (end-start))

if __name__ == '__main__':
    main()
