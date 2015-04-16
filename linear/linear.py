"""
A collection of linear algebra methods and objects.
    
    Contents:
        Matrix
"""

import random

class Matrix:
    """
    Matrix:

    A randomly generated matrix. 
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
        for c in range(matrix.columns):
             
            #gets column from 2nd matrix
            column = [matrix.data[r][c] for r in range(matrix.rows)]

            #gets row from 1st matrix
            for r in range(self.rows):
                row = self.data[r]

                #sum(multiplication) 1st matrix row and 2nd matrix column 
                product = map(mul, row, column)
                sumation = sum(product)

                result.data[r][c] = sumation

        return result

    def __str__(self):
        result = ''

        for row in self.data:
            result = result + str(row) + '\n'

        return result 

