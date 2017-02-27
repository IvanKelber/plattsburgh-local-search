import random
import math

from graphics import *
from tspProposals import *
from basic import *


PROPOSALS = [
    swapRandom,
    # swapBeginning,
    # swapLocal,
    # shuffle
]
WINDOW_SIZE = 800
MARGIN = WINDOW_SIZE/4
NUM_POINTS = 100
POINT_RADIUS = 3

# POINTS = [(random.randrange(MARGIN,WINDOW_SIZE-MARGIN),random.randrange(MARGIN,WINDOW_SIZE-MARGIN)) for i in range(NUM_POINTS)]

def tsp(points):
    total = 0
    for p,q in zip(points,points[1:]):
        total += distance(p,q)
    return total

def distance(p,q):
    return ((q[0]-p[0])**2 + (q[1]-p[1])**2)**.5

def plot(win,points):
    r = Rectangle(Point(0,0),Point(WINDOW_SIZE,WINDOW_SIZE))
    r.setFill("white")
    r.draw(win)
    for p,q in zip(points,points[1:]):
        Line(Point(p[0],p[1]),Point(q[0],q[1])).draw(win)
        c = Circle(Point(p[0],p[1]),POINT_RADIUS)
        c.setFill("red")
        c.setOutline("red")
        c.draw(win)

def circle():
    return [((WINDOW_SIZE/4)*(math.sin(i)+1)+MARGIN,(WINDOW_SIZE/4)*(math.cos(i)+1)+MARGIN) for i in range(NUM_POINTS)]


def main():
    POINTS = circle()

    win = GraphWin("My Circle", WINDOW_SIZE, WINDOW_SIZE)


    epsilons = [1000,500,100,50,10,1000,1]
    xp = POINTS
    bestSoFar = xp
    print "Starting Guess: %.10f" % tsp(POINTS)
    for eps in epsilons:
        for i in range(5):
            plot(win,xp)
            xp = localSearch(tsp,random.choice(PROPOSALS),xp,eps,1)
            if(tsp(xp) <= tsp(bestSoFar)):
                bestSoFar = xp
        print "Best for epsilon %.2f: %.10f" %(eps, tsp(bestSoFar))
    print "=========="
    print "Original: ", tsp(POINTS)
    print "Best: ", tsp(bestSoFar)
    plot(win,bestSoFar)
    raw_input(">")

if __name__ == '__main__':
    main()
