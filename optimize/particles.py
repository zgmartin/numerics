import random
import math
import time
from matplotlib import pyplot

def potential(location_a, location_b):
    """
    The potential energy between two particles.
    """
    r = math.sqrt((location_b[0]-location_a[0])**2 + (location_b[1]-location_a[1])**2)
    return 1/r**12 - 2/r**6

def energy(locations):
    """
    The total system energy between multiple particles.
    """
    total_energy = 0

    for i in range(len(locations)):
        for location in locations[i+1:]:
            total_energy += potential(locations[i],location)

    return total_energy 

def move_particle(location,distance):
    """
    A random movement of a particle.
    """
    move = (random.uniform(-distance, distance), random.uniform(-distance, distance))
    new_location = (location[0]+move[0], location[1]+move[1]) 
    
    return new_location



locations = [(random.uniform(0,10),random.uniform(0,10)) for n in range(10)]
system_energy = energy(locations)

print 'points:', locations
print 'energy:', system_energy
coords = zip(*locations) 
pyplot.scatter(coords[0],coords[1])
pyplot.axis('off')
pyplot.show()
pyplot.clear()

for n in range(10):
    system_energy = energy(locations)

    for n in range(len(locations)):
        old_energy = energy(locations)
        location = locations.pop(n)
        new_location = move_particle(location,1)
        locations.append(new_location)
        new_energy = energy(locations)
        if new_energy > old_energy:
            locations.pop()
            locations.append(location)
            #print 'new energy:', new_energy, old_energy
            #time.sleep(1)

print 'energy:', energy(locations)
coords = zip(*locations) 
pyplot.scatter(coords[0],coords[1])

