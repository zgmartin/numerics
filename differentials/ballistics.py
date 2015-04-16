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






#Ballistics Problem
def force(velocity):
    """
    Models the movement of a bullet moving in space.
    """
    mass = .1 
    gravity = 9.8
    friction = 0.001

    if velocity>0:
        return -gravity - friction/mass*velocity**1.5

    else:
        return -(gravity - friction/mass*velocity)


#results
pyplot.title('Ballistics')
pyplot.ylabel('velocity')
pyplot.xlabel('time')

#generates plots for different initial velocities
plots = [runge_integral(1, (0,v), 50, force) for v in range(300,550,50)]

distances = []
for plot in plots:
    distance = 0
    for d in plot[1]:
        if d < 0: 
            break
        else:
            distance += d 
    distances.append(distance)
print distances


