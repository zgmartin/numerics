"""
Flight Path Trajectory Problem:
Landing a plane at an airport based on initial value conditions.

"""
import math
from matplotlib import pyplot

def trajectory(x,y):
    """
    The differential trajectory of the plane. 
    Height of plane as a function of its distance.  
    """
    w = 30
    v = 100
    k = float(w)/v

    return float(y)/x - k*math.sqrt(1+(float(y)/x)**2)

def traj_heun(x,y):
    """
    The differential trajectory of the plane. 
    Height of plane as a function of its distance.  
    """
    w = 150
    v = 150
    k = float(w)/v

    return float(y)/x - k*math.sqrt(1+(float(y)/x)**2)

def traj_rung(x,y):
    """
    The differential trajectory of the plane. 
    Height of plane as a function of its distance.  
    """
    w = 150
    v = 120
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


def modified_heun(step, iterations, initial_values, differetial):
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
        aproximation = outputs[-1] + step * differetial(inputs[-1], outputs[-1])
        output = outputs[-1] + step/2 * differetial(inputs[-1], outputs[-1] + aproximation)
        outputs.append(output)

    return inputs, outputs


def modified_runge_kutta(step, x, y, differetial):
    """
    Runge-Kutta Method:
        Based off the Taylor series
    """

    k0 = step*differetial(x,y)
    k1 = step*differetial(x,y + k0/2.0)
    k2 = step*differetial(x,y + k1/2.0)
    k3 = step*differetial(x,y + k2)

    return (k0 + 2*k1 + 2*k2 + k3)/6.0


def mod_runge(step, iterations, initial_values, differetial):

    inputs = []
    outputs = []
    x = initial_values[0]
    y = initial_values[1]

    for i in range(iterations):
        inputs.append(x)
        outputs.append(y)
        x = x+step
        y = y + modified_runge_kutta(step, x, y, differetial)
        
    return inputs, outputs

#results
pyplot.title('Trajectory')
pyplot.xlabel('distance')
pyplot.ylabel('height')

#euler
points = modified_euler(-.01, 9999, (100,0), trajectory)
pyplot.plot(points[0],points[1])
#heun
points = modified_heun(-.01, 9999, (100,0), traj_heun)
pyplot.plot(points[0],points[1])
#rung
points = mod_runge(-.01, 9999, (100,0), traj_rung)
pyplot.plot(points[0],points[1])


pyplot.show()