import math
import random

from matplotlib import pyplot

def f(x, mean=1, deviation=.25):
    exponent = - float((x-mean)**2)/(2*deviation**2)
    devisor = math.sqrt(2*math.pi*deviation**2)
    return 1/devisor * math.e**exponent



initial_value = 1000000
days = [n for n in range(260)]
values = [random.uniform(-initial_value,initial_value) for n in range(260)] 

results = []
for value in values:
    prob = random.uniform(0,1)
    if prob>f(value):
        initial_value = initial_value+value
    results.append(initial_value)

pyplot.plot(days,results)

results = []
for value in values:
    prob = random.uniform(0,1)
    if prob>f(value,mean=0,deviation=.5):
        initial_value = initial_value+value
    results.append(initial_value)

pyplot.plot(days,results)

pyplot.show()


"""
info:
The stocks follow these trends because of the probability distribution that determines how 
likely the price of the stock will change within the future. 


run:
python epi_stock.py
"""