import random

def swapRandom(points):
    proxy = points[:]
    length = len(points)
    i = random.randint(0,length-1)
    j = random.randint(0,length-1)
    proxy[i],proxy[j] = proxy[j],proxy[i]
    return proxy


#Doesn't seem to work that well
def swapBeginning(points):
    proxy = points[:]
    length = len(points)
    i = random.randint(1,length-1)
    proxy[0],proxy[i] = proxy[i],proxy[0]
    return proxy


def shuffle(points):
    proxy = points[:]
    random.shuffle(proxy)
    return proxy

def swapLocal(points):
    proxy = points[:]
    i = random.randrange(0,len(points)-1) #randrange doesn't include upper bound
    proxy[i],proxy[i+1] = proxy[i+1],proxy[i]
    return proxy

def shiftRight(points):
    proxy = points[1:] + [points[0]]
    return proxy
