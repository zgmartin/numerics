import random
import math
import time
from matplotlib import pyplot, animation


def energy(location_a, location_b):
    """
    Lennard-Jones energy between two particles.

    """
    r = math.sqrt((location_b[0]-location_a[0])**2 + (location_b[1]-location_a[1])**2)
    return 1/r**12 - 2/r**6

def system_energy(particles):
    """
    The total system energy between multiple particles.
    """
    total_energy = 0

    for i in range(len(particles)):
        for location in particles[i+1:]:
            total_energy += energy(particles[i],location)

    return float(total_energy)/2 

def move(location,distance):
    """
    A random movement of a particle.
    """
    move = (random.uniform(-distance, distance), random.uniform(-distance, distance))
    new_location = (location[0]+move[0], location[1]+move[1]) 
    
    return new_location



#particle initialization
#particles = [(random.uniform(0,10),random.uniform(0,10)) for n in range(10)]
particles = [(3,0),(3,1),(3,2),(3,3),(3,4),(3,5),(2,6),(4,6)]
system_energy = system_energy(particles)

#results
print 'points:', particles
print 'system_energy:', system_energy
coords = zip(*particles) 
pyplot.scatter(coords[0],coords[1])
pyplot.axis('off')
pyplot.show()

#simulation 
for time_step in range(100):
    system_energy = system_energy(particles)
    
    #change position of particles
    for n in range(len(particles)):     
        old_energy = system_energy(particles)
        particle = particles.pop(n)
        new_particle = move(particle,1)
        particles.append(new_particle)
        new_energy = system_energy(particles)
        if new_energy > old_energy:
            particles.pop()
            particles.append(particle)
#results
print 'system_energy:', system_energy(particles)
coords = zip(*particles) 
pyplot.scatter(coords[0],coords[1])
pyplot.axis('off')
pyplot.show()