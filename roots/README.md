###Finding Roots
![root] (./root.png?raw=true)

####Bisection Method:

`x = (x_0 + x_1)/2`

The initial interval is partitioned into two intervals.

`midpoint = interval/2`

Depending on the location of the root, either the right or left side of the partitioned interval is chosen to be the new interval. The process is iterated until the tolerance for f(x) is met.

`0 < f(x) < tolerance`

 The bisection method coverages slowly at a `quadratic rate`, but the method has the advantage of guaranteeing correctness on non smooth and ill behaved functions.

####Newton Method:

`x_n+1 = x_n - f(x_n)/f'(x_n)`

A value is chosen close to the root, then a closer value is calculated by using the ratio of the function and its derivative evaluated at the initial value. Newton method converges quickly at a `linear rate`, but falls short on non smooth functions, looping, and divergence intervals.   


#####Method Comparison:
|        |Bisection| Newton|
|--------|---------|-------|
| speed  | quadratic| linear|
| converge| always | sometimes|

####Example:

![plot] (./plot.png?raw=true)

By inspection of the graph, the root of the function is approximately at the location x = 1.55.

####Results:
|         |Bisection| Newton|
|---------|---------|---------|
|interval | [1.5,1.6]| 1.6|
|iterations| 8       | 3|
|root      | 1.5191  | 1.5191|

#####Run:
```
python example.py
```