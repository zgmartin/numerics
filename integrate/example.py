import time
from integrate import generator
from matplotlib import pyplot

#uniform random numbers
x = generator(time.time(),  20000000, 10)
results = pyplot.hist(x,20)
results = results[0]

n = 20000000.0
percentages = map(lambda x: x/n, results)
print percentages
n = len(percentages)
average = sum(percentages)/n
print 'percent average:', average





#matrix




#integration 

