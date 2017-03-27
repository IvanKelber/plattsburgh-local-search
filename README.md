# Local Search

This repository contains two examples of local search applications written in python.  

The first is Circle Packing: Given n circles of increasing radii, what is the best way to arrange them such that:
1. No two circles overlap.
2. We can fit them in the smallest possible bounding square.

![The result of circle packing](http://i.imgur.com/RRGpYMk.png)

The second is the infamous Travelling Salesman Problem: Given n points, what is the shortest possible path that visits each point exactly once?

![Local Search Hard at Work Approximating TSP](http://i.imgur.com/KWKT6iH.png)

# To Run

Before running, you'll need to install the python libraries matplotlib, scipy, and numpy.

Assuming that you have pip installed (it comes pre-installed with python 2.79+) you can open a terminal and type:

```
pip install scipy
pip install numpy
pip install matplotlib
```
Once you clone you can run `cd` into `Circles/` or `TSP/` and run `python circleRunner.py` or `python tspRunner.py <locus>`, respectively where options for `locus` are "circle", "sin", or "random"

# Stencils

I've included various stencils that can be used for educational purposes.  The general order that I suggest filling them out goes like this:

1. Stencils/gradientDescent.py (optional)
2. Stencils/localSearch.py
3. Stencils/circlePacking/proposals.py
4. Stencils/circlePacking/circleRunner.py
5. Stencils/travellingSalesman/proposals.py
6. Stencils/travellingSalesman/tspRunner.py

Each of these files has some description of the task, and `TODO`s wherever your input is necessary.  You should be able to fill out just those sections and get similar results to mine.
You shouldn't need to worry about graphics at all and instead can focus purely on local search.

Of course you are free to change whatever you like.  Enjoy.
