"""
A collection of methods for integrating functions.

    Methods:
        Trapezoidal 
        Monte Carlo  
"""
import random
from operator import mul

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
        
        #multiplication ends when end of 2nd matrix column is reached
        for column in range(matrix.columns):
            
            #gets row from 1st matrix
            for row in range(self.rows):
                self_row = self.data[row]
                
                #gets column form 2nd matrix
                matrix_column = []
                for r in range(matrix.rows):
                    matrix_column.append(matrix.data[r][column])
                
                #sum(multiplication) 1st matrix row and 2nd matrix column 
                product = map(mul, self_row, matrix_column)
                sumation = sum(product)

                result.data[row][column] = sumation

        return result

    def __str__(self):
        result = ''

        for row in range(self.rows):
            result = result + str(self.data[row])+'\n'

        return result 


