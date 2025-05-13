# 2. Monte Carlo Simulations

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

The Monte Carlo method converges at a rate proportional to $\frac{1}{\sqrt{N}}$, where $N$ is the number of points. This means that to improve accuracy by a factor of 10, you need 100 times more points.Efficiency: Although Monte Carlo methods are relatively simple and versatile, they can require a large number of points for high accuracy due to their slow convergence rate.

### Computational Considerations

#### Trade-off

There is a trade-off between computational time and accuracy. More points yield better estimates but require more computational resources and time.

#### Performance

Modern computers can handle millions of points quickly, but efficient implementations and optimizations (e.g., vectorized operations in NumPy) are crucial for performance.

## Other Aplications

Monte Carlo simulations can be applied to a wide range of problems involving uncertainty and variability. Here are several examples of simulations that could be conducted using Monte Carlo methods alongside a regional map of Poland:

#### 1. Economic Activity Simulation

Objective: Simulate the variation in economic output, such as GDP per capita or total GDP by region.Data Needed: Historical economic data, growth rates, inflation rates.Analysis: Visualize potential economic outcomes for different regions based on varying growth assumptions.

#### 2. Population Growth Forecast

Objective: Model the population growth trends for each region up to a future year (e.g., 2030), taking into account factors such as birth rates, death rates, and migration.Data Needed: Current population, birth/death rates, migration trends.Analysis: Assess the impacts on infrastructure, housing needs, and service demands.

#### 3. Healthcare Resource Allocation

Objective: Evaluate the distribution of healthcare resources under varying demand scenarios, influenced by factors like disease outbreak or an aging population.Data Needed: Current healthcare resources, historical usage data, demographic trends.Analysis: Optimize resource allocation strategies to cope with uncertain demand peaks.

#### 4. Infrastructure Development Risk Assessment

Objective: Assess the potential financial and scheduling risks involved in large infrastructure projects across regions.Data Needed: Projected costs, timelines, and historical risk factors impacting infrastructure projects.Analysis: Identify high-risk areas and strategize mitigation efforts.

#### 5. Environmental and Climate Impact Projections

Objective: Predict environmental impacts, such as pollution or climate change effects, under different scenarios.Data Needed: Historical environmental data, emission rates, and climate model predictions.Analysis: Use scenarios to develop regional climate action plans or pollution control measures.

#### 6. Transportation and Traffic Flow Modelling

Objective: Simulate traffic patterns and regional transportation demand to aid in planning and resource allocation.Data Needed: Traffic data, road network information, public transport usage.Analysis: Improve infrastructure planning and prioritize future transport projects.

#### 7. Agricultural Yield Prediction

Objective: Estimate variability in agricultural output due to changing weather patterns, input costs, and market conditions.Data Needed: Historical yield data, weather forecasts, market trends.Analysis: Plan supply chains and pricing to optimize profitability under uncertain conditions.

#### 8. Educational Outcomes Estimation

Objective: Predict educational achievements and demands based on demographic trends, investment levels, and policy changes.Data Needed: Current educational data, population trends, policy parameters.Analysis: Develop policies to improve educational outcomes and resource distribution.

### Specific Simulation (a) Education, (b) Population Forecast

[![2021 Enrollees vs 2026 Graduates (Approx)](https://mg-2025p03.github.io/physics/_pics/P2.7.png)](https://mg-2025p03.github.io/physics/_pics/P2.7.png)

[![2050 Poland Population by Region (Forecast)](https://mg-2025p03.github.io/physics/_pics/P2.3.png)](https://mg-2025p03.github.io/physics/_pics/P2.3.png)

[![2026 Masovian Region Population by Age group (Forecast)](https://mg-2025p03.github.io/physics/_pics/P2.6.png)](https://mg-2025p03.github.io/physics/_pics/P2.6.png)

[![Masovian Region Population by Age 13-18 (Forecast)](https://mg-2025p03.github.io/physics/_pics/P2.8.png)](https://mg-2025p03.github.io/physics/_pics/P2.8.png)

[![Probability breakdown](https://mg-2025p03.github.io/physics/_pics/P2.8.1.png)](https://mg-2025p03.github.io/physics/_pics/P2.8.1.png)