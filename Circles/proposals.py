#proposals
import random
import numpy as np

def swapAdjacent(points):
    proxy = points[:]
    length = len(points)
    i = random.randint(0,length-2)
    proxy[i],proxy[i+1] = proxy[i+1],proxy[i]
    return proxy

def wideScaleRandomNoise(points):
    radius = 10 ** (random.random() * -6 + 2)
    random_numbers = np.random.normal(0,1,[len(points),2])
    proxy = []
    for i,point in enumerate(points):
        proxy += [(point[0] + random_numbers[i][0]*radius, point[1] + random_numbers[i][1]*radius)]
    return proxy


def wideScaleRandomNoisePair(points):
    indices = [i for i in range(len(points))]
    first = random.randint(0,len(indices) - 1)
    del indices[first]
    second = random.choice(indices)

    radius = 10 ** (random.random() * -6 + 1)
    random_numbers = np.random.normal(0,1,[2,2])

    proxy = points[:]
    proxy[first] = tuple([proxy[first][i] * random_numbers[0][i]*radius for i in range(2)])
    proxy[second] = tuple([proxy[second][i] * random_numbers[1][i]*radius for i in range(2)])

    if(first == second):
        print "first == second"

    return proxy

def singleRandomNoise(points):
    index = random.randint(0,len(points) - 1)

    radius = 10 ** (random.random() * -6 + 1)
    random_numbers = np.random.normal(0,1,2)

    proxy = points[:]
    proxy[index] = tuple([proxy[index][i] * random_numbers[i]*radius for i in range(2)])
    
    return proxy


def wideScaleRandomNoiseSingleCoordinate(points):
        radius = 10 ** (random.random() * -6 + 2)
        random_numbers = np.random.normal(0,1,len(points))
        proxy = []
        if(random.randint(0,1) != 0):
            for i,point in enumerate(points):
                proxy += [(point[0] + random_numbers[i]*radius, point[1])]
        else:
            for i,point in enumerate(points):
                proxy += [(point[0], point[1] + random_numbers[i]*radius)]
        return proxy

def shufflePoints(points):
    proxy = points[:]
    random.shuffle(proxy)
    return proxy
