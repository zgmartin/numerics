"""
Integration Methods:
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

