# Stencil Created by Ivan Kelber, March 2017
# Completed by <Your Name Here>, <Date Here>
import random
import time

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

    -Returns the x that yields the most optimal func(x)
    '''

    return None


def main():
    # Note that we are optimizing a convex function.  This is to compare local search
    # to gradient descent.  We will attempt more interesting problems in other stencils.
    parabola = lambda x: x**2
    proposalFunc = lambda x: x + (random.random() - .5)/10 #randomly add [-.05,.05] to x
    startingX = "FILL IN"
    epsilon = "THESE PARAMETERS"
    timeThresh = "EXPERIMENT!"

    print localSearch(parabola,proposalFunc,startingX,epsilon,timeThresh)

if __name__ == '__main__':
    main()
