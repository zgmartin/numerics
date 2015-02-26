"""
A collection of methods for integrating functions.

    Methods:
        Trapezoidal 
        Monte Carlo  
"""
import random

def generator(seed, size, interval):
    """
    Generates a list of random numbers.

    inputs:
        seed: random seed value
        size: the number of elements in the list

    """
    
    numbers = []

    for n in range(size):
        seed = random_uniform(seed,interval)
        numbers.append(seed)

    return numbers


def random_uniform(number, interval):
    """
    A uniformly distributed random number on a given interval. 
    """

    return (7 * number) % 2.0*interval - interval


def trapezoid(function):
    pass


def montecarlo(function):
    pass



class Matrix:
    """
    A random matrix object. 
    """

    def __init__(self, rows, columns):
        self.data = []
        self.rows = rows
        self.columns = columns

        for row in range(rows):
            self.data.append([])
            for column in range(columns):
                self.data[row].append(random.uniform(-1,1))
    
    def __mul__(self, matrix):
        result = Matrix(self.rows, matrix.columns)
        
        return result

    def __str__(self):
        result = ''

        for row in range(self.rows):
            result = result + str(self.data[row])+'\n'

        return result 


