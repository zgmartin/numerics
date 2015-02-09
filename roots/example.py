from roots import bisection, newton
from math import sin, cos, exp

def f(x):
    return pow(2.015, -pow(x,3)) - pow(x,4)*sin(pow(x,3)) - 1.984
def df(x):
    return pow(x,2)*(-2.10186*exp(-0.700619*pow(x,3)) - 4*x*sin(pow(x,3)) - 3*pow(x,4)*cos(pow(x,3)))

print bisection(f,[1.5,1.6],.001)
print newton(f,df,1.6,.001)

