# Problem 2

Theoretical Foundation
The Monte Carlo method for estimating $\pi$ relies on the geometric properties of a circle and its bounding square:

Unit Circle and Square:

Consider a unit circle centered at the origin, $0, 0$, with radius 1.
The area of this circle is $\pi r^2 = \pi \cdot 1^2 = \pi$.


Bounding Square:

The smallest square that can completely contain this unit circle has sides of length 2 (from -1 to 1 on both x and y axes).
The area of the square is $4 = 2 \cdot 2$.


Point Distribution:

If you randomly distribute points across this square, the proportion of points that fall inside the circle to the total number of points is equal to the ratio of their areas: $\frac{\text{Area of Circle}}{\text{Area of Square}} = \frac{\pi}{4}$.

Estimating (\pi):

Therefore, if $N$ total points are randomly generated in the square, and $M$ of those fall inside the circle, then $frac{M}{N} \approx \frac{\pi}{4}$.
Rearranging gives $\pi \approx 4 \times \frac{M}{N}$.

Simulation
Here's how to perform the simulation:

Generate Random Points:

For each point, generate random x and y coordinates between -1 and 1.

Calculate Inside Circle:

For each point, calculate whether it falls inside the unit circle using the condition $x^2 + y^2 \leq 1$.

Estimate (\pi):

Track how many points fall inside the circle.
Use the formula $\pi \approx 4 \times \frac{M}{N}$ to estimate $\pi$.

Visualization
To create a plot:

Generate a large number of points.
Plot these points on a 2D graph, coloring those inside the circle differently from those outside.

Analysis

Accuracy Improvement:

Generally, the accuracy of the $\pi$ approximation improves with more points, following a convergence rate of $O(\frac{1}{\sqrt{N}}$.
The Law of Large Numbers implies the estimated value will converge to the actual value of $\pi$ with more samples.

Computational Considerations:

The more points you generate, the more computational power and time required.
However, this method is embarrassingly parallel, as each point test is independent of others, allowing for parallel processing.

Buffon's Needle Problem
Buffon's Needle is a classic probability problem that estimates the value of $\pi$ based on a simple geometric experiment. The problem involves dropping a needle of length $L$ onto a plane that has parallel lines drawn on it at a distance $D$ apart. The goal is to find the probability that the needle crosses one of the lines. Through this, an estimate for $\pi$ can be obtained.
Derivation of the Formula

Assumptions:

The length of the needle, $L$, is less than or equal to the distance $D$ between the parallel lines.
The needle is dropped randomly, which means any angle $\theta$ between 0 and $\pi$ is equally likely.

Probability Calculation:

The needle crosses a line if the perpendicular distance from the needle's midpoint to the nearest line is less than or equal to $\frac{L}{2} \sin(\theta$.
The probability (P) of the needle crossing a line can be obtained by integrating over all possible positions and angles:

$$
P = \frac{2L}{\pi D} \int_0^{\pi/2} \sin(\theta) , d\theta = \frac{2L}{\pi D}
$$

Estimating (\pi):

By conducting this experiment multiple times, if we let $n$ be the total number of times the needle is dropped and $x$ be the number of times it crosses a line, we can estimate $\pi$ using the relationship:

$$
\pi \approx \frac{2L \cdot n}{x \cdot D}
$$

Simulation
To simulate the random dropping of a needle:

Setup:

Choose values for $L$ and $D$, ensuring $L \leq D$.
Drop the needle $n$ times.
For each drop, generate a random angle $\theta$ and a random position for the needle's midpoint.

Cross Detection:

Count the number of line crossings, $x$, by checking if the perpendicular distance condition is satisfied.

Estimate $\pi$:

Use the formula $\pi \approx \frac{2L \cdot n}{x \cdot D}$ to estimate $\pi$.

Visualization
To visualize the simulation:

Plot the parallel lines on a plane.
Represent needle drops as line segments, showing those that cross a line in a different color.
Illustrate multiple trials to observe the randomness and distribution of crossings.

Analysis

Number of Needle Drops:

Observe how increasing $n$ affects the accuracy of the $\pi$ estimate.
Typically, as $n$ increases, the estimate converges more closely to the true value of $\pi$.

Comparison to Circle-based Method:

The circle-based method involves inscribing a circle in a square and using random points to estimate $\pi$.
Analyze convergence rates: Buffon's Needle often converges slower than the circle method due to reliance on line intersection which is a rarer event.

The above steps provide a comprehensive framework for understanding, simulating, visualizing, and analyzing Buffon's Needle problem to estimate $\pi$. If you need further assistance with coding the simulation or creating visualizations, let me know!