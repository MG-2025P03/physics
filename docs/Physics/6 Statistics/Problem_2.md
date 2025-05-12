# 1. Monte Carlo Simulations

Monte Carlo simulations are a computational technique used to estimate mathematical expressions and solve problems that might be deterministic in principle. In this context, we'll use Monte Carlo simulations to estimate the value of π by simulating random points in a square and determining how many fall inside a quarter circle.

## Concept

### Formula Derivation

A unit circle is defined by the equation $x^2 + y^2 = 1$, which describes a circle with radius 1 centered at the origin (0, 0).To estimate π using Monte Carlo simulation, consider a quarter circle (since our computations will be easier with positive x and y).

![Estimating Pi](https://mg-2025p03.github.io/physics/_pics/P2.1.png)

### Geometric Insight

Inside a square of side length 2, draw a quarter of a unit circle with radius 1.The area of the square is $1 \times 1 = 1$.The area of the quarter circle is $\frac{1}{4}\pi$.

### Monte Carlo Simulation

Randomly generate points within the square.Count the number of points that fall within the quarter circle using $x^2 + y^2 \leq 1$.The ratio of points inside the circle to the total number of points approximates the area of the quarter circle. Thus, the formula for π is derived as $\pi \approx 4 \times (\text{points inside the circle} / \text{total points})$.

To analyze how the accuracy of the π estimate improves with an increasing number of points, we can perform multiple Monte Carlo simulations with different numbers of points and observe the convergence of the estimated π value. The more points used, the closer the estimate should approach the true value of π due to the law of large numbers.

### Convergence Rate

#### Convergence

The Monte Carlo method converges at a rate proportional to $\frac{1}{\sqrt{N}}$, where $N$ is the number of points. This means that to improve accuracy by a factor of 10, you need 100 times more points.Efficiency: Although Monte Carlo methods are relatively simple and versatile, they can require a large number of points for high accuracy due to their slow convergence rate.Computational Considerations

#### Trade-off

There is a trade-off between computational time and accuracy. More points yield better estimates but require more computational resources and time.Performance: Modern computers can handle millions of points quickly, but efficient implementations and optimizations (e.g., vectorized operations in NumPy) are crucial for performance.

### Other simulation

![2021 Enrollees vs 2026 Graduates (Approx)](https://mg-2025p03.github.io/physics/_pics/P2.7.png)

![2050 Poland Population by Region (Forecast)](https://mg-2025p03.github.io/physics/_pics/P2.3.png)

![2026 Masovian Region Population by Age group (Forecast)](https://mg-2025p03.github.io/physics/_pics/P2.6.png)