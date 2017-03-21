# Created by Ivan Kelber, March 2017

import random

def swapRandom(points):
    '''
    Randomly chooses two points and swaps them.
    '''
    proxy = points[:]
    length = len(points)
    indices = [i for i in range(len(points))]
    i = random.randint(0,length-1)
    del indices[i]
    j = random.choice(indices)
    proxy[i],proxy[j] = proxy[j],proxy[i]
    return proxy


def swapPairs(points):
    '''
    Randomly chooses two pairs of adjacent points and swaps them.
    '''
    i = random.randrange(0,len(points)-1) #randrange doesn't include upper bound
    j = random.randrange(0,len(points)-1) #randrange doesn't include upper bound
    proxy = points[:]
    proxy[i:i+1],proxy[j:j+1] = proxy[j:j+1], proxy[i:i+1]
    return proxy

def insertion(points):
    '''
    Randomly chooses a point, removes it from the list and then inserts it into
    a random location.
    '''
    proxy = points[:]
    length = len(points)
    i = random.randrange(0,length-1) #randrange doesn't include upper bound
    j = random.randint(0,length-1) #randint includes upper bound
    toInsert = proxy[j]
    del proxy[j]
    proxy = proxy[:i+1] + [toInsert] + proxy[i+1:]

    return proxy

def cutCards(points):
    '''
    Splits the list into two at a randomly chosen index.  Then rearranges the
    two lists.
    '''
    i = random.randint(0,len(points)-1)
    proxy = points[i:] + points[:i]
    return proxy


def swapBeginning(points):
    '''
    Swap the beginning with another random point
    '''
    proxy = points[:]
    length = len(points)
    i = random.randint(1,length-1)
    proxy[0],proxy[i] = proxy[i],proxy[0]
    return proxy


def shuffle(points):
    '''
    Randomly shuffle the order of points visited.
    '''
    proxy = points[:]
    random.shuffle(proxy)
    return proxy

def swapLocal(points):
    '''
    Chooses a random point and swaps it with it's neighbor
    '''
    proxy = points[:]
    i = random.randrange(0,len(points)-1) #randrange doesn't include upper bound
    proxy[i],proxy[i+1] = proxy[i+1],proxy[i]
    return proxy

def shiftLeft(points):
    '''
    Shifts the entire order one to the left, causing the first point to be the end.
    '''
    proxy = points[1:] + [points[0]]
    return proxy
