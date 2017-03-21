'''
Created by Ivan Kelber, March 2017
'''

import time
import sys


def gradientDescent(func, startX, step,epsilon, deltaThresh):
    '''
    -func is the convex function we are trying to optimize.
    -startX is our starting guess for what is optimal.
    -step is a scalar used in conjunction with the slope to prevent overstepping
        the optimal.
    -epsilon is the accuracy of the derivative.  Note that we are not finding the
        explicit derivative of func at x, but instead comparing two points on the
        function that are very close (epislon distance from each other) which has
        the effect of giving us an approximate derivative.  For practical purposes
        this approximation suffices.
    -deltaThresh is the accuracy of the final result.  If after a step of gradient
        descent we have not improved (or more accurately changed) our guess by
        deltaThresh then we end the loop and assume that we are within deltaThresh
        of the true optimum.
    '''
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
    '''
    -func is the function we are trying to optimize.
    -proposalFunc is the function that we are using to find new x values.  At each
        step we apply proposalFunc to our current x to obtain some x'.  We then
        compare the values of func(x) and func(x') and take whichever x is better
        within some epsilon. (More on epislon below)
    -startingX is our starting guess for what is optimal.
    -epsilon is the window for which we accept new x values.  That is, if our
        proposal function suggests an x' such that func(x') <= func(x) + epsilon
        we still accept x' as the new value.  This is an extremely important part
        of local search as it prevents us from being too committed to a particular
        valley despite there existing a more optimal valley not too far away.
    -timeThresh is how many sconds we run localSearch with the given parameters.
    '''
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
    pass


if __name__ == '__main__':
    main()
