# Stencil Created by Ivan Kelber, March 2017
# Completed by <Your Name Here>, <Date Here>

# This stencil assumes that you've written localSearch correctly in the file
# localSearch.  If you haven't, then this will not work and cause you much frustration!
# Assuming that, you have two tasks.  The first is to create proposal functions to use
# in proposals.py.  The second is to futz with the parameters below.  That is,
# EPSILONS, SECONDS_PER_SEARCH, and PER_EPSILON.  Note that the most important of these
# is the EPSILONS array.
#
# Some hints:
# - Each proposal function should take an array of n points and return an array of n points.
# - Each epsilon is the precision at which we accept new x values from proposal functionsself.
#     So, large epsilons allow us to explore our options while small epsilons let us narrow
#     in on an optimum.  How large is large?  How small is small?  It depends on the function
#     that we are trying to optimize.
# - Try running slowly at first and then gradually begin speeding it up to see what works
#     and what doesn't.
# - If you're getting 'stuck' at a certain optimum and can't seem to get past it,
#     it might mean that you're in a local minimum and need to explore more.  Try to change epsilon.
# - There is no right answer.  Many things will work so try whatever you can think of!
# - If you're having trouble thinking of proposal functions, try drawing potential scenarios
    # on paper!  Small cases can extend to large cases when run hundreds of times a second.



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
from localSearch import localSearch
from proposals import *


#Globals for graphics
fig, ax = plt.subplots()
PATCHES = []

# TODO:Select your proposals here. A list of function handles.
# Remember that you can have as many proposals as you want.  Though having too
# many might affect performance.PROPOSALS = [
    swapRandom,
]

#TODO: Change these parameters
EPSILONS = [] # The order of the epsilons to try.
PER_EPSILON = 0 # The number of times we try each epsilon
SECONDS_PER_SEARCH = 0 # The number of seconds we run local search for each set of parameters

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

def main():

    POINTS = circle_locus() #TODO: change this around and see how things change

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


# ====== Graphics Stuff.  Change at your own risk! ======================


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



if __name__ == '__main__':
    main()
