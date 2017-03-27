# Created by Ivan Kelber, March 2017

import random
import math
import sys
import time

#Set up matplotlib for graphics
import matplotlib as mpl
mpl.rcParams['toolbar'] = 'None'
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import matplotlib.patches as mpatches
from matplotlib.collections import PatchCollection



sys.path.append('../') #add parent directory to import path
from basic import localSearch
from proposals import *


#Globals for graphics
fig, ax = plt.subplots()
PATCHES = []

# Parameters for local search
PROPOSALS = [
    # swapRandom,
    insertion,
]
EPSILONS = [100,75,50,40,30,20,10,5] # The order of the epsilons to try.
PER_EPSILON = 5 # The number of times we try each epsilon
SECONDS_PER_SEARCH = 2 # The number of seconds we run local search for each set of parameters

# Point generation parameters
RADIUS = 100
NUM_POINTS = 100
POINT_RADIUS = RADIUS/NUM_POINTS


def tsp(points):
    '''
    The Travelling Salesman function takes a list of points and returns the
    sum of the distance between each adjacent point.  For example,
    suppose points = [a,b,c,d].  Then tsp(points) would return
    dist(a,b) + dist(b,c) + dist(c,d)
    '''
    total = 0
    for p,q in zip(points,points[1:]):
        total += distance(p,q)
    return total


# ============ Various locus' to test TSP with =============
def circle_locus(period=1):
    return [((RADIUS)*(math.sin(i*math.pi*2*period/NUM_POINTS)+1),(RADIUS)*(math.cos(i*math.pi*2*period/NUM_POINTS)+1)) for i in range(NUM_POINTS)]

def random_locus():
    return [(random.randrange(0,RADIUS),random.randrange(0,RADIUS)) for i in range(NUM_POINTS)]

def sin_wave_locus(period=2):
        return [(i*period*2,(RADIUS)*(math.sin(i*1*math.pi*2*period/NUM_POINTS)+1)) for i in range(NUM_POINTS)]
#===========


def distance(p,q):
    '''Calculates the euclidean distance between point p and q'''
    return ((q[0]-p[0])**2 + (q[1]-p[1])**2)**.5

def plot(points):
    '''
    Plots each point and each line segment between adjacent points.
    '''

    x_values, y_values = plot_points(points)
    line = mlines.Line2D(x_values, y_values, lw=1, alpha=1,color='black',zorder=1)
    ax.add_line(line)

    plt.axis('equal')
    plt.axis('off')

    plt.pause(.01)

def plot_points(points):
    '''
    Plots each point.  This was originally separated for purely graphical reasons.
    Those graphical reasons are no longer relevant.
    '''
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
    '''
    After local search has completed we draw the path in order so we can observe
    what the path looks like.
    '''
    clear()
    x_values = y_values = []
    lines = []
    for p,q in zip(points,points[1:]):
        line = mlines.Line2D([p[0],q[0]], [p[1],q[1]], lw=2, alpha=1,color='white',zorder=1)
        lines.append(line)
        ax.add_line(line)
        plt.axis('equal')
        plt.axis('off')

    for line,next_line in zip(lines,lines[1:]):
        line.set_color('black')
        next_line.set_color('green')
        plt.pause(.025)
    lines[-1].set_color('black')





def clear():
    '''
    Clears the plot.
    '''
    global PATCHES
    PATCHES = []
    plt.cla()


def main(locus):

    #Command line arguments
    if(locus == "circle"):
        POINTS = circle_locus()
    elif(locus == "random"):
        POINTS = random_locus()
    elif(locus == "sin"):
        POINTS = sin_wave_locus()
    else:
        print "Locus '" + locus + "' doesn't exist!"
        sys.exit(0)

    random.shuffle(POINTS)
    plt.ion()

    epsilons = EPSILONS
    xp = POINTS
    bestSoFar = xp
    print "Starting Guess: %.10f" % tsp(POINTS)
    start = time.clock()
    # ======== Begin Local Search =========
    # We try different epsilons as time goes on.  This allows us to first explore
    # and then once we are pretty sure we are searching in a 'good' valley
    # we can begin to narrow in on the optimum
    for i, eps in enumerate(epsilons):
        for _ in range(PER_EPSILON):
            plot(xp)
            # Randomly choose one of the proposals to use.
            xp = localSearch(tsp,random.choice(PROPOSALS),xp,eps,SECONDS_PER_SEARCH)
            if(tsp(xp) <= tsp(bestSoFar)):
                bestSoFar = xp
        print "Best for epsilon %.2f: %.10f" %(eps, tsp(bestSoFar))
    # ======== End Local Search ==========

    print "=========="
    print "Original: ", tsp(POINTS)
    print "Best: ", tsp(bestSoFar)
    end = time.clock()
    clear()
    draw_path(bestSoFar)

    raw_input("Took %.4f seconds. Press enter to close:" % (end-start))

if __name__ == '__main__':
    locus = sys.argv[1] if len(sys.argv) > 1 else "Use 'python tspRunner.py <locus>'"
    main(locus)
