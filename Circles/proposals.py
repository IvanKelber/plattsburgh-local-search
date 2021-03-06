# Created by Ivan Kelber, March 2017

import random
import numpy as np


def swapAdjacent(points):
    '''
    Swaps two adjacent circles randomly.
    '''
    proxy = points[:]
    length = len(points)
    i = random.randint(0,length-2)
    proxy[i],proxy[i+1] = proxy[i+1],proxy[i]
    return proxy

def wideScaleRandomNoise(points):
    '''
    Generates a random scale in [.001,100].
    Adds random noise on the magnitude of the generated scale to each component
    of each circle.
    '''
    scale = 10 ** (random.random() * -6 + 2)
    random_numbers = np.random.normal(0,1,[len(points),2])
    proxy = []
    for i,point in enumerate(points):
        proxy += [(point[0] + random_numbers[i][0]*scale, point[1] + random_numbers[i][1]*scale)]
    return proxy


def wideScaleRandomNoisePair(points):
    '''
    Generates a random scale in [.001,100].
    Chooses two circles at random.
    Adds random noise on the magnitude of the generated scale to each component
    of each circle.
    '''
    indices = [i for i in range(len(points))]
    first = random.randint(0,len(indices) - 1)
    del indices[first]
    second = random.choice(indices)

    scale = 10 ** (random.random() * -6 + 1)
    random_numbers = np.random.normal(0,1,[2,2])

    proxy = points[:]
    proxy[first] = tuple([proxy[first][i] * random_numbers[0][i]*scale for i in range(2)])
    proxy[second] = tuple([proxy[second][i] * random_numbers[1][i]*scale for i in range(2)])

    return proxy

def singleRandomNoise(points):
    '''
    Chooses a random circle.
    Generates a random scale in [.001,100].
    Adds random noise on the magnitude of the generated scale to each component.
    '''
    index = random.randint(0,len(points) - 1)

    scale = 10 ** (random.random() * -6 + 1)
    random_numbers = np.random.normal(0,1,2)

    proxy = points[:]
    proxy[index] = tuple([proxy[index][i] * random_numbers[i]*scale for i in range(2)])

    return proxy


def wideScaleRandomNoiseSingleCoordinate(points):
    '''
    Generates a random scale in [.001,100].
    Adds random noise on the magnitude of the generated scale to a randomly
    chosen component of each circle.
    '''
    scale = 10 ** (random.random() * -6 + 2)
    random_numbers = np.random.normal(0,1,len(points))
    proxy = []
    if(random.randint(0,1) != 0):
        for i,point in enumerate(points):
            proxy += [(point[0] + random_numbers[i]*scale, point[1])]
    else:
        for i,point in enumerate(points):
            proxy += [(point[0], point[1] + random_numbers[i]*scale)]
    return proxy

def shufflePoints(points):
    '''
    Randomly shuffles the locations of all of the circles.
    '''
    proxy = points[:]
    random.shuffle(proxy)
    return proxy
