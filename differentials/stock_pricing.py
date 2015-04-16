"""
Stock Pricing Problem: 
A competition model between two companies.
"""

from matplotlib import pyplot

def company_a(x, y):
    a = 0.222
    b = -0.0011

    return a*x + b*x*y

def company_b(x, y):
    c = -1.999
    e = 0.010

    return c*y + e*x*y

def euler(step, start, end, initial_values, diffs):
    """
    Euler method for two variable dependent differentials.
    """
   
    outputs = []

    #base
    base_x = initial_values[0] - step * diffs[0](initial_values[0], initial_values[1])
    base_y = initial_values[1] - step * diffs[1](initial_values[0], initial_values[1])
    outputs.append((base_x, base_y))
    
    while start < end:
        tup = outputs[-1]
        x = tup[0] - step * diffs[0](tup[0], tup[1])
        y = tup[1] - step * diffs[1](tup[0], tup[1])
        outputs.append((x,y))
        start += step

    return outputs


#results
outputs = euler(.0001, 0, 10, (199,21), (company_a,company_b))
x = [output[0] for output in outputs]
y = [output[1] for output in outputs]

#fist instance y>=x
for output in outputs:
    if output[0]<output[1]:
        print 'y>=x:', output
        break

#phase plot
pyplot.title('Phase Diagram')
pyplot.ylabel('y')
pyplot.xlabel('x')
pyplot.plot(x,y)
pyplot.show()
