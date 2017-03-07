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

WINDOW_SIZE = 300
MARGIN = WINDOW_SIZE/4
NUM_POINTS = 10
POINT_RADIUS = 1

POINTS = [(random.randrange(MARGIN,WINDOW_SIZE-MARGIN),random.randrange(MARGIN,WINDOW_SIZE-MARGIN)) for i in range(NUM_POINTS)]


def plot(win,points):
    for radius in range(len(points)):
        point = points[radius]
        c = Circle(Point(point[0],point[1]),radius)
        c.draw(win)


def main():
    win = GraphWin("My Graph",WINDOW_SIZE,WINDOW_SIZE)
    plot(win,POINTS)
    print circles(POINTS)

    raw_input(">")
if __name__ == '__main__':
    main()
