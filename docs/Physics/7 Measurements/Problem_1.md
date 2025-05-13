# A practical simulation

This experiment provides a systematic approach to measuring the acceleration due to gravity $g$ using a simple pendulum. Here is the detailed explanation of each step, along with how you can analyze uncertainties and other considerations:

### Analysis

- Compare with Standard Value

Standard gravitational acceleration is approximately $9.81 , \text{m/s}^2$. Compare your calculated $g$ with this value.

[![Data captured during simulation](https://mg-2025p03.github.io/physics/_pics/m2.png)](https://mg-2025p03.github.io/physics/_pics/m2.png)

[![Data captured during simulation](https://mg-2025p03.github.io/physics/_pics/m1.png)](https://mg-2025p03.github.io/physics/_pics/m1.png)

### Procedure Details

#### 1. Materials

String: A length of 1 to 1.5 meters.
Small weight: Such as a bag of coins, a small bag of sugar, or a keychain.
Stopwatch: Or a smartphone timer.
Ruler or Measuring Tape: For measuring the length of the pendulum.

#### 2. Setup

Pendulum Assembly: Attach the weight to the string and secure the other end to a stable support, allowing it to swing freely.
Measurement of Length $L$: Use a ruler or tape to measure the pendulum length from the fixed point to the weight’s center. Record the resolution of your measuring tool, e.g., ±0.1 cm for a tape measure, translating to an uncertainty of half the resolution $±0.05 cm$.

#### 3. Data Collection

Displacement and Release: Displace the pendulum by less than 15° to minimize non-linear effects and release it.
Timing Oscillations: Use the stopwatch to measure the time for 10 complete oscillations. Repeat this measurement 10 times to account for variability. Record all measurements.
Calculate the Mean Time $\bar{T}_{10}$: Find the average time for 10 oscillations.
Standard Deviation $\sigma$: Calculate to understand variability in the timing.
Uncertainty in Mean Time $\sigma_{\bar{T}}$: Determined using $\frac{\sigma}{\sqrt{N}}$ where $N = 10$.

### Calculations

- Calculate the Period $T$

$$T = \frac{\bar{T}_{10}}{10}$$

The period of one oscillation.

- Determine Gravitational Acceleration $g$

$$g = \frac{4\pi^2L}{T^2}$$

- Propagate Uncertainties

Use error propagation methods to calculate the uncertainty in $g$ based on uncertainties in $L$ and $T$.