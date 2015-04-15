import time
from integrate import generator
from matplotlib import pyplot
from math import sin

#uniform random numbers
r = rand(time.time())
x = [r.next() for i in range(20000000)]
print x[0:100]
results = pyplot.hist(x,20)
results = results[0]

n = 20000000.0
percentages = map(lambda x: x/n, results)
n = len(percentages)
average = sum(percentages)/n
print 'percent average:', average

#sum subset 20 random numbers in list
subsets = [sum(x[i:i+20]) for i in xrange(0,len(x),20)]
results = pyplot.hist(subsets,200)
pyplot.show()


#integration 
def function(x):
    return sin(x)/x