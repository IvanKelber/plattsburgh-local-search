# Stencil Created by Ivan Kelber, March 2017
# Completed by <Your Name Here>, <Date Here>


def gradientDescent(func, startX, step, epsilon, deltaThresh):
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

    -Returns the x and func(x) of the best found.


    NOTE:  This is an extremely basic version of gradient descent.  Gradient descent
    on it's own could be the subject of many talks.  I strongly encourage anyone
    who is interested to read more about it.  Specifically more about
    Stochastic Gradient Descent and applications in machine learning.
    '''


    return None


def main():
    parabola = lambda x: x**2
    startX = "FILL IN"
    step = "THESE PARAMETERS."
    epsilon = "DON'T FORGET"
    deltaThresh = "TO EXPERIMENT"

    print gradientDescent(parabola, startX, step, epsilon, deltaThresh)

if __name__ == '__main__':
    main()
