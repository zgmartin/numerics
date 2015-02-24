"""
A collection of methods for integrating functions.

    Methods:
    Trapezoidal 
    Monte Carlo  
"""

def generator(seed, size):
    """
    Generates a list of random numbers.

    inputs:
        seed: random seed value
        amount: 

    """
    
    numbers = []

    for n in range(size):
        seed = random_uniform(seed)
        numbers.append(seed)

    return numbers


def random_uniform(number):
    """
    A uniformly distributed random number generator on interval [-10,10]. 
    """

    return (7 * number) % 20.0 - 10
