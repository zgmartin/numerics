"""
Root Finding Problem:
Finding roots of specific function. 
"""

from roots import bisection, newton
from math import sin, cos, exp

#test function
def f(x):
    return pow(2.015, -pow(x,3)) - pow(x,4)*sin(pow(x,3)) - 1.984

#methods performed on function
print bisection(f,[1.5,1.6],.0001)
print newton(f,1.6,.0001)


