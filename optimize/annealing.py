"""
Simulated Annealing:

Developed by Metropolis at Los Alamos for the Manhattan project.
"""

import math
from scipy import constants
import random
import time

def distace(location_a, location_b):
    """
    A measure of distance.
    """
    dist = math.sqrt((location_b[0]-location_a[0])**2 + (location_b[1]-location_a[1])**2)
    
    return dist


def cost(cities):
    """
    The energy of a state.
    """
    total_cost = 0

    for index in range(len(cities)-1):
        total_cost+=distace(cities[index],cities[index+1])

    return total_cost

def change(solution):
    """
    Makes random local change in solution.
    """
    i = random.randint(0,len(solution)-1)
    j = (i+1)%len(solution)

    temp = solution[j]
    solution[j]=solution[i]
    solution[i]=temp 

    return solution 

def sample(space,size):
    """
    Random sample from the space.
    """
    sample = []
    
    for n in range(size):
        choice = random.choice(space)
        sample.append(choice)
    
    return sample

def probability(solution, new_solution, temperature):
    """
    Acceptance function for transition between two energy states.

    p = e^(-delta/temp)
    """
    delta = cost(solution) - cost(new_solution)
    boltzmann = constants.k

    return math.e**(-delta/boltzmann*temperature)

def anneal(space, size, temperature=1, decrement=.01, iterations=100):
    """
    Simulates the annealing process of a cooling metal.
    
        Algorithm:
            create solution 
            initialize temp
                iterate 
                    random change from solution
                    if change less than old:
                        change solution
                    else if p = e^(-delta/temp)>rand:
                        change solution
                reduce temp
    """

    solution = sample(space,size)

    while(temperature>=0):
        for n in range(iterations):
            new_solution = change(solution)
            if new_solution<solution:
                solution = new_solution
            elif probability(solution, new_solution, temperature)>random.uniform(0,1):
                solution = sample(space,size)

        print 'temp:', temperature, cost(solution)
        temperature= temperature-decrement

    return solution



space = [(6.623123,2.253046),(4.723182,1,949215),(2.346305,4.202261),(7.069488,6.151476),
        (0.415793,1.353737),(7.485281,7.505212),(7.901073,8.858949),(6.386353,7.223111)]

anneal(space, 3)