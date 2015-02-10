from roots import bisection, newton
from math import sin, cos, exp
from matplotlib import pyplot
import numpy


def f(x):
    return pow(2.015, -pow(x,3)) - pow(x,4)*sin(pow(x,3)) - 1.984
def df(x):
    return pow(x,2)*(-2.10186*exp(-0.700619*pow(x,3)) - 4*x*sin(pow(x,3)) - 3*pow(x,4)*cos(pow(x,3)))

print bisection(f,[1.5,1.6],.001)
print newton(f,df,1.6,.001)


x = numpy.linspace(0,2)
y = map(f, x)

pyplot.figure()
pyplot.plot(x,y)
pyplot.title('Finding Roots x : f(x)=0')
pyplot.scatter(1.5191,0, s=80, facecolor='none', edgecolors='r')
pyplot.annotate('here it is', xy=(1.5191,0), xytext=(.5,.5), arrowprops=dict(facecolor='black',shrink=0.05))
pyplot.grid(True)
pyplot.savefig('root.png')

