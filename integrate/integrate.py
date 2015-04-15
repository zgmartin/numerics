"""
A collection of methods for integrating functions.

    Methods:
        Trapezoidal 
        Monte Carlo  
"""
import random
import math
from operator import mul
from numpy import linspace


def rand(seed):
    """
    Random Number Generator:

    A uniformly distributed random number generator on a given interval. 

    Uses Linear Conguance to generate random number. 
    """
    while 0<1:
        seed = (1103515245*seed+12345) % math.pow(2,32)
        yield seed


def fast_rand(seeds):
    """
    Dang's fast random number.
    """

    x = seeds[0]
    y = seeds[1]

    while  0<1:
        temp = x
        x = (x + y) % 1.0
        y = temp
        yield x

"""
def trapezoid(function, interval):
    Trapezoidal Integration:

    
    x = linspace(interval[0], interval[1])
    h = x[1] - x[0]
    
    intersum = [f(t)*2 for t in x[1:len(x)-1]]

    area = (sum(intersum) + f(x[0]) + f(x[-1]) * h * 0.5
    
    return area  
"""

def montecarlo(function, iterations, interval):
    """
    Monte Carlo Integration:
        Uses randomness to approximate area under function.

        n/N = a/A 

        [n: number of elements under curve]
        [N: total number elements]
        [a: area under curve]
        [A: total area]
    """

    in_count = 0 

    for i in range(iterations):
        x = random.uniform(interval[0],interval[1])
        y = random.uniform(interval[0],interval[1])

        if function(x) <= y:
            in_count += 1

    total_area = pow(interval[1]-interval[0],2)

    area = float(in_count/iterations) * total_area

    return area

    


