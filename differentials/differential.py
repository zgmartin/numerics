"""
Integration Methods:

Methods:
    Euler
    Runge-Kutta
"""

def euler(inputs, initial_values, differetial):
    """
    Euler Method:
        Approximate curve by moving small steps tangential to the initial value.
    """

    outputs = []
    step = inputs[1]-inputs[0]

    #base case
    base = initial_values[1] + step * differetial(initial_values[1])
    outputs.append(base)

    for i in inputs:
        output = outputs[-1] + step * differetial(outputs[-1])
        outputs.append(output)

    return outputs

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


