"""
Ballistics Problem:
"""
import numpy
import differential
from matplotlib import pyplot


def force(velocity):
    """
    Models the movement of a bullet moving in space.
    """

    mass = .01 
    gravity = 9.8
    friction = .001

    return -gravity - friction/mass*velocity

def force_down(velocity):
    """
    Models the movement of a bullet moving in space.
    """

    mass = .01 
    gravity = 9.8
    friction = .001

    return gravity - friction/mass*velocity


#results
pyplot.title('Ballistics')
pyplot.ylabel('velocity')
pyplot.xlabel('time')

#plot
x = numpy.linspace(1,20, 200)
y = differential.euler(x,(0,300),force)

absolutes = [abs(a) for a in y]
index = absolutes.index(min(absolutes))

print 'zero: ' + str(x[index]) + ',' + str(y[index])

pyplot.scatter(x[index],y[index], s=80, facecolors=None, edgecolors='r')
pyplot.plot(x,y[1:])

#plot 2
y = differential.euler(x,(0,0),force_down)

absolutes = [abs(a) for a in y]
index = absolutes.index(min(absolutes))

print 'zero: ' + str(x[index]) + ',' + str(y[index])

pyplot.scatter(x[index],y[index], s=80, facecolors=None, edgecolors='r')
pyplot.plot(x,y[1:])

pyplot.show()