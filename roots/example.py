"""
Root Finding Problem:
Finding roots of a function. 
"""

from roots import bisection, newton
from math import sin, cos, exp
from matplotlib import pyplot
from numpy import linspace

#test function
def f(x):
    return pow(2.015, -pow(x,3)) - pow(x,4)*sin(pow(x,3)) - 1.984

#results
bisect = bisection(f,[1.5,1.6],.0001)
newt = newton(f,1.6,.0001)
print 'bisection:', bisect
print 'newton', newt

#plots
x = linspace(0,2)
y = map(f, x)
pyplot.scatter(bisect, 0, s=80, facecolors='none', edgecolors='r')
pyplot.annotate('here it is', xy=(bisect,0), xytext=(1,1), arrowprops=dict(facecolor='black', shrink=0.05))
pyplot.xlim(0,2)
pyplot.plot(x,y)
pyplot.axis('off')
pyplot.show() 