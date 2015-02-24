import time
from integrate import generator
from matplotlib import pyplot
from operator import div


#uniform random numbers
x = generator(time.time(), 20000000)
results = pyplot.hist(x,20)
results = results[0]
n =  len(results)
presentages = map()