import random

def swapRandom(points):
    proxy = points[:]
    length = len(points)
    i = random.randint(0,length-1)
    j = random.randint(0,length-1)
    proxy[i],proxy[j] = proxy[j],proxy[i]
    return proxy

def reverse(points):
    return points[::-1]

def swapPairs(points):
    i = random.randrange(0,len(points)-1) #randrange doesn't include upper bound
    j = random.randrange(0,len(points)-1) #randrange doesn't include upper bound
    proxy = points[:]
    proxy[i:i+1],proxy[j:j+1] = proxy[j:j+1], proxy[i:i+1]
    return proxy

def insertion(points):
    proxy = points[:]
    length = len(points)
    i = random.randrange(0,length-1) #randrange doesn't include upper bound
    j = random.randint(0,length-1) #randint includes upper bound
    toInsert = proxy[j]
    del proxy[j]
    proxy = proxy[:i+1] + [toInsert] + proxy[i+1:]
    if(len(proxy) != length):
        print "ERROR: %d != %d" % (len(proxy),length)
    return proxy

def cutCards(points):
    i = random.randint(0,len(points)-1)
    proxy = points[i:] + points[:i]
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
