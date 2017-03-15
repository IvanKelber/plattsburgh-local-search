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
    # swapPairs,
    # swapRandom,
    insertion,
    # swapBeginning,
    # swapLocal,
    # shuffle,
]
RADIUS = 100
NUM_POINTS = 100
POINT_RADIUS = RADIUS/NUM_POINTS
PER_EPSILON = 5
SECONDS_PER_SEARCH = 1

def random_locus():
    return [(random.randrange(0,RADIUS),random.randrange(0,RADIUS)) for i in range(NUM_POINTS)]

def tsp(points):
    total = 0
    for p,q in zip(points,points[1:]):
        total += distance(p,q)
    return total

def circle_locus(period=1):
    return [((RADIUS)*(math.sin(i*math.pi*2*period/NUM_POINTS)+1),(RADIUS)*(math.cos(i*math.pi*2*period/NUM_POINTS)+1)) for i in range(NUM_POINTS)]

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

def draw_path(points):
    clear()
    x_values = y_values = []
    lines = []
    for p,q in zip(points,points[1:]):
        # x_values.append(p[0])
        # y_values.append(p[1])
        line = mlines.Line2D([p[0],q[0]], [p[1],q[1]], lw=2, alpha=1,color='white',zorder=1)
        lines.append(line)
        ax.add_line(line)
        plt.axis('equal')
        plt.axis('off')

    # line.set_color('black')
    for line,next_line in zip(lines,lines[1:]):
        line.set_color('black')
        next_line.set_color('green')
        plt.pause(.025)
    lines[-1].set_color('black')
    # line = mlines.Line2D(x_values,y_values, lw=1, alpha=0,color='black',zorder=1)





def clear():
    global PATCHES
    PATCHES = []
    plt.cla()




def main():
    POINTS = circle_locus()
    random.shuffle(POINTS)
    plt.ion()

    epsilons = [100,75,50,40,35,30,20,10]
    xp = POINTS
    bestSoFar = xp
    print "Starting Guess: %.10f" % tsp(POINTS)
    start = time.clock()
    for i, eps in enumerate(epsilons):
        for _ in range(PER_EPSILON):
            plot(xp)
            xp = localSearch(tsp,random.choice(PROPOSALS),xp,eps,SECONDS_PER_SEARCH)
            if(tsp(xp) <= tsp(bestSoFar)):
                bestSoFar = xp
        print "Best for epsilon %.2f: %.10f" %(eps, tsp(bestSoFar))
    print "=========="
    print "Original: ", tsp(POINTS)
    print "Best: ", tsp(bestSoFar)
    print "Actual Best: ", 2*(RADIUS)*math.pi
    end = time.clock()
    # plot(bestSoFar)
    clear()
    draw_path(bestSoFar)
    # clear()

    raw_input("Took %.4f seconds. Press enter to close:" % (end-start))

if __name__ == '__main__':
    main()
