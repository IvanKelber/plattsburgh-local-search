#define the circle function
import sys
import random
import math


def circles(points):
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

def printDistance(distance):
    for i in range(len(distance)):
        row = ""
        for j in range(len(distance)):
            row += str(distance[i][j]) + "\t"
        print row


def dist(a,b,ra,rb):
    return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2) - (ra + rb)

def main():
    POINTS = [(random.randrange(0,100),random.randrange(0,100)) for i in range(10)]
    print circles(POINTS)


if __name__ == '__main__':
    main()
