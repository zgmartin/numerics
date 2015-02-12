"""
Numerical methods for finding roots of functions.

Problem:
Finds solutions x such that f(x) = 0 
"""

def bisection(function, interval, tolerance):
    """
    Splits interval in half and choses side of root until f(x) gets close to zero.   
    """
    x = (interval[0] + interval[1]) / 2.0
    
    #checks which side the root lies on 
    if function(interval[0])*function(x)<0:
        interval[1] = x
    else:
        interval[0] = x

    #recursive base tolerance 
    if abs(function(x)) <= tolerance:
        return x
    else:
        return bisection(function, interval, tolerance)


def derivative(function, x, tolerance):
    """
    Numerically computes derivative at specific location. 
    """
    return (function(x+tolerance/2) - function(x-tolerance/2)) / tolerance 

def newton(function, x, tolerance):
    """
    Moves x back towards root based on the derivative of the function. 
    """
    x = x - function(x)/derivative(function, x, tolerance)

    #recursive base tolerance 
    if abs(function(x)) <= tolerance:
        return x
    else:
        return newton(function, x, tolerance)
