# Created by Ivan Kelber, March 2017

import sys
import random
import math


def circles(points):
    '''
    - points is a list of n tuples (x,y) representing locations of n circles.
        The point (x,y) at points[i] represents a circle whose center is at
        (x,y) and whose radius is i.

    This function returns the side of the smallest possible square that can
        surround each of these circles such that no two circles are overlapping.
        If two circles are found to be overlapping this function will return
        sys.maxint.
    '''
    minX = sys.maxint
    maxX = 0

    minY = sys.maxint
    maxY = 0
    distance = [[1000 for i in range(len(points))] for j in range(len(points))]
    for radius in range(len(points)):
        point = points[radius]
        #Update X
        minX = min(minX,point[0]-radius)
        maxX = max(maxX,point[0]+radius)

        #Update Y
        minY = min(minY,point[1]-radius)
        maxY = max(maxY,point[1]+radius)
        for radius2 in range(len(points)):
            point2 = points[radius2]

            if point is not point2:
                distance[radius][radius2] = dist(point,point2,radius,radius2)
                if(distance[radius][radius2] < 0):
                    # printDistance(distance)
                    return sys.maxint

    # printDistance(distance)
    return max(maxY-minY,maxX-minX)

def printDistance(distanceMatrix):
    '''
    Used to print out the distance matrix computed in the circles function;
    primarily for debugging.
    '''
    for i in range(len(distanceMatrix)):
        row = ""
        for j in range(len(distanceMatrix)):
            row += str(distanceMatrix[i][j]) + "\t"
        print row


def dist(a,b,ra,rb):
    '''
    - a,b are centers of circles
    - ra,rb are the respective radii of those two circles.

    This function calculates the distance between the edges of two circles.
        Note that this returns a negative value if two circles are overlapping.
    '''
    return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2) - (ra + rb)

def main():
    pass


if __name__ == '__main__':
    main()
