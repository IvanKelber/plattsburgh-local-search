#runner
import random
import math
import sys
import time

sys.path.append('../') #add parent directory to import path
from graphics import GraphWin,Point,Circle,Line,Rectangle
from basic import localSearch
from circle import circles

from proposals import *

PROPOSALS = [
    # swapRandom,
    randomNoise,
    # shufflePoints
]

WINDOW_SIZE = 500
MARGIN = 15
NUM_POINTS = 10
POINT_RADIUS = 1

POINTS = [(random.randrange(MARGIN,WINDOW_SIZE-MARGIN),random.randrange(MARGIN,WINDOW_SIZE-MARGIN)) for i in range(NUM_POINTS)]


def plot(win,points):
    r = Rectangle(Point(0,0),Point(WINDOW_SIZE,WINDOW_SIZE))
    r.setFill("white")
    r.draw(win)
    for radius in range(len(points)):
        point = points[radius]
        c = Circle(Point(point[0],point[1]),radius)
        c.draw(win)


def main():
    win = GraphWin("My Graph",WINDOW_SIZE,WINDOW_SIZE)
    plot(win,POINTS)

    epsilons = [1000,100,500,200,200,50,100]
    xp = POINTS
    bestSoFar = xp
    print "Starting Guess: %.10f" % circles(POINTS)
    start = time.clock()
    for eps in epsilons:
        for i in range(5):
            plot(win,xp)
            xp = localSearch(circles,random.choice(PROPOSALS),xp,eps,1)
            if(circles(xp) <= circles(bestSoFar)):
                bestSoFar = xp
        print "Best for epsilon %.2f: %.10f" %(eps, circles(bestSoFar))
    print "=========="
    print "Original: ", circles(POINTS)
    print "Best: ", circles(bestSoFar)
    end = time.clock()
    plot(win,bestSoFar)

    raw_input(">")
if __name__ == '__main__':
    main()
