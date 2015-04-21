Differential Equations:
-----------------------


Euler's Method:
-------------

![euler](./euler.png)

```
y' = [y(t+h) - y(t)] / h
y(t+h) = y(t) + h * y'
```

Approximate curve by moving small steps tangential to the initial value.

Heun's Method:
--------------

`y(t+h) = y(t) + h * (1/2) y'+ ~y'`

The average between two tangent lines to approximate the function more accurately

Runge-Kutta:
------------

A more generalized form of Heun's Method for solving differential equations. Many averages between multiple partitions of the tangent lines. 


Ballistics:
-----------------

Calculate the total time the bullet is in the air.

`dv/dt = g + (a/m)*v`

![dist](./distance.png)

Results:

| direction   |      time          |      velocity        |
|-------------|--------------------|----------------------|
| up          | 14.013             | 0.00141630056777     |
| down        | 14.014             |  -299.97252056       |



Stock Market:
-------------

Modeling competition between stock prices.

```
x' = (a)x + (b)xy
y' = (c)y + (e)xy
```

![phase](./phase.png)


Results:

| stock       |      time          |      value           |    y>=x            |
|-------------|--------------------|----------------------|--------------------|
| x           |         4          | 77.8889199659        | 112.86717730768805 |
| y           |         4          | 479.212120381        | 112.86559624322435 |


Flight Path:
------------

Landing a plane at an airport based on initial value conditions.

`y' = y/x - w/v*sqrt(1 + (x/y)^2)`

![trag](./trajectory.png)

