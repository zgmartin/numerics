Integration:
------------

Random Numbers:
--------------

Deng Fast:

`n = (n-1 + n-2) mod 1`

Generates random numbers based on the remainder between two seeds. How fast is that? That's [Deng](http://en.wikipedia.org/wiki/Yuefan_Deng) fast!

Testing Randomness :

What does it mean to be random? The answer is relative to your information. The weather may seem like a random event, but when more information is known the predictability of the event becomes more likely. Atmospheric noise is at the end of the random spectrum because there is an information set the size of the universe to account for.

 Randomness is not a well defined concept. The only way to judge randomness is through a relative comparison of numbers based on statistical analysis. Below are some statistical tests performed on Deng's fast random number generator. 

![deng](./deng.png)

![sum](./sum.png)


Integration:
------------

Quadrature: 
The trapezoidal method partitions the space under the curve into little trapezoids and sums the area for each to generate the total area under the curve. 


Monte Carlo:
The Monte Carlo uses random numbers to chose the positions within the space. The relation between the area under the curve is `n/N = a/A`


Results:

| Method      |      time          |      area            |
|-------------|--------------------|----------------------|
| Quadrature  | 14.844221105527637 | 0.080136379072063391 |
| Monte Carlo | 14.844221105527637 | 0.080136379072063391 |