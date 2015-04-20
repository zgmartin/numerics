"""
Ballistics Problem:


"""
import numpy
import differential
from matplotlib import pyplot
import bisect


def force(velocity):
    """
    Models the movement of a bullet moving in space.
    """

    mass = .01 
    gravity = 9.8
    friction = .001

    if velocity>=0: 
        return -gravity - friction/mass*velocity

    else:
        return -(gravity - friction/mass*velocity)




points = differential.euler(.001, 1000000, (0,300),force)

#results
times = points[0]
velocities = points[1]
zero_index = differential.find_index(0,velocities)
time_up = times[zero_index]
print 'up time:', time_up

distances = differential.list_sum(velocities)
zero_index = differential.find_index(0, distances)
distances = distances[:zero_index+1]
times = times[:zero_index+1]
velocities = velocities[:zero_index+1]
print 'distance:', times[-1], distances[-1]
print 'down time:', times[-1] - time_up
print 'down velocity:', velocities[-1]

#plots
pyplot.title('Ballistics')
pyplot.ylabel('distance')
pyplot.xlabel('time')
pyplot.plot(times, distances)
pyplot.show()
pyplot.close()

pyplot.title('Ballistics')
pyplot.ylabel('velocity')
pyplot.xlabel('time')
pyplot.plot(times, velocities)
pyplot.show()
