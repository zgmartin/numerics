Minimization:
-------------

![min](./min.gif)

The goal of minimization is to search for the smallest value over the global space. Selecting the right direction to move is important in finding the minimum value. 

Localized search can be performed to move towards selecting a minimum, but has the problem of getting stuck in local pockets.

A global transition can be applied to break out from the localized position with the hope of finding a global minimum. 

Thats all we can do is hope. Hope that we chose the right path and the smallest value will be found within a a sea of points.

Annealing:
----------

>When I first heard about simulated annealing it caused me to think about how I solved problems, rarely through a rationally deductive process. Instead I value a free association of ideas, a jumble of three or four ideas bouncing around in my head. As the urge for resolution increases, the bouncing around stops and I settle on just one idea or strategy as the best. Likewise when I feel my actions are in a rut, I introduce a chaotic element - undertake a random action, like seeking out a new person, group, or meeting, without trying to justify it in terms of my existing values. It is usually a learning experience, if for no other reason than to show me that I am not in a rut after all. Adopting metaphors from science for our own life can change the way we think and act.

>Heinz Pagels- [Dreams of Reason](http://www.goodreads.com/book/show/694929.The_Dreams_of_Reason)

The ideas within annealing were first proposed by [Metropolis](http://en.wikipedia.org/wiki/Nicholas_Metropolis) as he was trying understanding energy state changes of particle systems while working on the [Manhattan Project](http://en.wikipedia.org/wiki/Manhattan_Project). 

* Algorithm:
    * guess a solution 
    * initialize temperature
    * iterate 
        * random change from solution
        * if change less than old:
            * change solution
        * else if p = e^(energy_change/temperature) grater than random number:
            * change solution
        * reduce temperature

Within annealing, the idea is to take a greedy approach to the problem by accepting smaller energy state transitions, while leaving the possibility of accepting a worse state to find the overall smallest value. The hope is that the worse state will result in a smaller energy than the previous.

The temperature decrease reduces our chances of transitioning to a new position. So as the temperature cools down so does the movement or energy of the particles hence the name annealing.




Energy Minimization:
--------------------

![particles](./particle.gif)

Energy minimization of particle systems is the standard way for understanding how optimization problems work. The particles represent collection of combinatorial points, and the energy function represents the cost function we need to minimize for moving the points towards a lower energy. 

In energy minimization the goal is to find the minimum energy of a collection of particles in space. The energy of the collection is computed by the total energy of the each particle relative to its neighbors. 

`v = 1/r^12 - 2/r^16`

The Lenard-Jones potential is a mathematical model that approximates the movement between pairs of neutral atoms. Where r is the distance between two particles and v is the potential movement of the particle.  

`E = 1/2 * sum(v)`

The energy is the total sum of all the potential movements of each particle relative to its neighbors. Each particle uses the Lenard-Jones potential to calculate its movement. The neighboring particles have greater influence on the movement because the short distance carries more weight than particles further away.

The goal is to move the particles towards a direction of minimal energy. This movement towards minimum energy is chosen by selecting random positions to move the particles. The problem with selecting random points is that there are a lot of bad decisions to make and few good ones, so most likely you will be waisting time searching the space for bad results.

To solve the problem of waisted time in searching the space of bad results. 