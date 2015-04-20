"""
Integration Methods:

Methods:
    Euler
    Runge-Kutta
"""

def euler(step, iterations, initial_values, differetial):
    """
    Euler Method:
        Approximate curve by moving small steps tangential to the initial value.
    """
    inputs = []
    outputs = []

    #base case
    base = initial_values[1] + step * differetial(initial_values[1])
    inputs.append(initial_values[0])
    outputs.append(base)

    for i in range(iterations):
        inputs.append(inputs[-1]+step)
        output = outputs[-1] + step * differetial(outputs[-1])
        outputs.append(output)

    return inputs, outputs

def runge_kutta(step, y, differetial):
    """
    Runge-Kutta Method:
        Based off the Taylor series
    """

    k0 = step*differetial(y)
    k1 = step*differetial(y + k0/2.0)
    k2 = step*differetial(y + k1/2.0)
    k3 = step*differetial(y + k2)

    return (k0 + 2*k1 + 2*k2 + k3)/6.0


def runge_integral(step, initial_values, stop, differetial):

    inputs = []
    outputs = []
    x = initial_values[0]
    y = initial_values[1]

    while x <= stop:
        inputs.append(x)
        outputs.append(y)
        x = x+step
        y = y + runge_kutta(step, y, differetial)
        
    return inputs, outputs


def list_sum(lis):
    """
    Generates a sum of a list of values based off the previous values.
    """
    transforms = [lis.pop(0)]

    for item in lis:
        transforms.append(transforms[-1]+item)
    
    return transforms


def find_index(number, lis):
    """
        Finds closest positive index value in a list. 
    """
    closest = lis[0]
    index = 0

    for n in range(len(lis)):
        if lis[n]>=0 and abs(lis[n] - number) < abs(closest - number):
            closest = lis[n]
            index = n
    print closest
    return index