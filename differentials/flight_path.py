"""
Flight Path Trajectory Problem:
Landing a plane at an airport based on initial value conditions.

"""
import math
from matplotlib import pyplot

def trajectory(x,y):
    """
    The differential trajectory of the plane. 
    Height of plane as a function of distance.  
    """
    w = 30 
    v = 100
    k = float(w)/v

    return float(y)/x - k*math.sqrt(1+(float(y)/x)**2)


def modified_euler(step, iterations, initial_values, differetial):
    """
    Euler Method:
        Approximate curve by moving small steps tangential to the initial value.
    """
    inputs = []
    outputs = []

    #base case
    base = initial_values[1] + step * differetial(initial_values[0], initial_values[1])
    inputs.append(initial_values[0])
    outputs.append(base)

    for i in range(iterations):
        inputs.append(inputs[-1] + step)
        output = outputs[-1] + step * differetial(inputs[-1], outputs[-1])
        outputs.append(output)

    return inputs, outputs


#results
points = modified_euler(-.01, 9999, (100,0), trajectory)
print points
x = points[0]
y = points[1]

#plots
pyplot.title('Trajectory')
pyplot.xlabel('x')
pyplot.ylabel('y')
pyplot.plot(x,y)
pyplot.show()