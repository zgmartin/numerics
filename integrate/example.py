"""
Random Number Problem:

Test random number generator's randomness 


Integration Problem:

integrate f(x) = sin(x)/x using Monte Carlo and Quad

"""

import time
import integrate 
from matplotlib import pyplot
from math import sin, e
import numpy
import random

"""
#uniform random numbers
pyplot.title('Deng Fast Random Numbers')
pyplot.ylabel('frequency')
pyplot.xlabel('intervals')

generator = integrate.deng_random([time.time(),time.time()])
x = [generator.next() for i in range(20000000)]
print 'Deng Random Numbers:',x[0:100]
results = pyplot.hist(x,20)
pyplot.show()
pyplot.close()

results = results[0]
n = 20000000.0
percentages = map(lambda x: x/n, results)
n = len(percentages)
average = sum(percentages)/n
print 'percent average:', average

#sum subset 20 random numbers in list
subsets = [sum(x[i:i+20]) for i in xrange(0,len(x),20)]
print 'subsets:', subsets[0:10]
print 'subset max:', max(subsets)
pyplot.title('Sum 20 Subset')
pyplot.ylabel('frequency')
pyplot.xlabel('sums')
results = pyplot.hist(subsets,200)
pyplot.show()


#scatter plot
generator = integrate.deng_fast([time.time(),time.time()])
x = [10*generator.next() for i in range(10000)]
y = [10*generator.next() for i in range(10000)]
colors = [generator.next() for i in range(10000)]

pyplot.scatter(x, y, c=colors, alpha=.3)
pyplot.axis('off')
pyplot.show()
"""




#functions
def f(x):
    return sin(x)/x
def ex(x):
    return pow(e,x)

#random numbers
inputs = [random.uniform(-10,10) for x in range(100000)]
outputs = [random.uniform(-10,10) for x in range(100000)]
points = zip(inputs,outputs)
#area
area = integrate.montecarlo(f, inputs, outputs)
print 'monte carlo:', area
area = integrate.trapezoid(ex, [0,10])
print 'trapezoid:', area

in_points = [ (i,j) for i,j in points if j<=f(i) and j>=0] 
in_points = zip(*in_points)

#plots
x = numpy.linspace(-10,10)
y = map(f,x)
pyplot.plot(x,y)
outs = map(f, inputs)
pyplot.scatter(in_points[0], in_points[1], c=in_points[1], alpha=.3)
pyplot.axis('off')
pyplot.show()