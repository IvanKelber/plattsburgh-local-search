import time
import sys

def gradientDescent(func, startX, step,epsilon, deltaThresh):
    x = startX
    xPrev = None
    count = 0
    while(not xPrev or abs(x-xPrev) > deltaThresh):
        count += 1
        print count, ":::::", x,func(x)
        slope = (func(x+epsilon) - func(x)) / epsilon
        xPrev = x
        x += -step*slope

    return x,func(x),count

def localSearch(func,proposalFunc,startingX,epsilon,timeThresh):
    startTime = time.clock()
    bestX = startingX
    bestY = func(startingX)
    while(time.clock() - startTime < timeThresh):
        xp = proposalFunc(startingX)
        yp = func(xp)
        if(yp != None and yp - func(startingX) <  epsilon):
            startingX = xp
            if(yp < bestY):
                bestX = xp
                bestY = yp
    return bestX


def main():
    func = lambda x: x**2
    # print gradientDescent(func,100,.0001,.1,.00001)
    print localSearch(func,lambda x:x-1,100,.1,.0001)


if __name__ == '__main__':
    main()
