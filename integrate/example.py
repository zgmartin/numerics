"""
Random Number Problem:

Test random number generator's randomness 


Integration Problem:

integrate f(x) = sin(x)/x using Monte Carlo and Quad

"""

import time
from integrate import deng_fast
from matplotlib import pyplot
from math import sin

#uniform random numbers
pyplot.title('Deng Fast Random Numbers Distribution')
pyplot.ylabel('frequency')
pyplot.xlabel('intervals')

generator = deng_fast([time.time(),time.time()])
x = [10*generator.next() for i in range(20000000)]
print x[0:100]
results = pyplot.hist(x,20)
pyplot.show()

"""
n = 20000000.0
percentages = map(lambda x: x/n, results)
n = len(percentages)
average = sum(percentages)/n
print 'percent average:', average

#sum subset 20 random numbers in list
subsets = [sum(x[i:i+20]) for i in xrange(0,len(x),20)]
results = pyplot.hist(subsets,200)
pyplot.show()


#integration problem
def function(x):
    return sin(x)/x

"""