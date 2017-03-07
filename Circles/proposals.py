#proposals
import random

def swapRandom(points):
    proxy = points[:]
    length = len(points)
    i = random.randint(0,length-1)
    j = random.randint(0,length-1)
    proxy[i],proxy[j] = proxy[j],proxy[i]
    return proxy

def randomNoise(points):
    proxy = []
    for point in points:
        proxy += [(point[0] + random.random()*100 - 50,point[1]+ random.random()*100 - 50)]
    return proxy

def shufflePoints(points):
    proxy = points[:]
    random.shuffle(proxy)
    return proxy
