import time
"""
Numerical methods for finding roots of functions.

Problem:
Finds solutions x such that f(x) = 0 
"""

def bisection(function, interval, tolerance):
    """
    Splits interval in half and choses side of root until f(x) gets close to zero.   
    """
    x = float(interval[0] + interval[1]) / 2
    
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


