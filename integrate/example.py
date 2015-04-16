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

"""
#uniform random numbers
pyplot.title('Deng Fast Random Numbers')
pyplot.ylabel('frequency')
pyplot.xlabel('intervals')

generator = integrate.deng_fast([time.time(),time.time()])
x = [10*generator.next() for i in range(20000000)]
print 'Deng Random Numbers:',x[0:100]
results = pyplot.hist(x,20)
pyplot.close()
#pyplot.show()

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


#integration problem
def function(x):
    return sin(x)/x

def ex(x):
    return pow(e,x)

#monte carlo
area = integrate.montecarlo(function, 10000, [0,2])
print 'monte carlo:', area

area = integrate.trapezoid(ex, [0,10])
print 'trapezoid:', area