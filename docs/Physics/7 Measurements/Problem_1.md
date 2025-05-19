# A practical simulation

This experiment provides a systematic approach to measuring the acceleration due to gravity $g$ using a simple pendulum. Here is the detailed explanation of each step, along with how you can analyze uncertainties and other considerations:

Standard gravitational acceleration is approximately $9.81 , \text{m/s}^2$. Compare your calculated $g$ with this value.

[![Data captured during simulation](https://mg-2025p03.github.io/physics/_pics/m2.png)](https://mg-2025p03.github.io/physics/_pics/m2.png)

[![Data captured during simulation](https://mg-2025p03.github.io/physics/_pics/m1.png)](https://mg-2025p03.github.io/physics/_pics/m1.png)

### Procedure Details

#### 1. Materials

String: A length of 1 to 1.5 meters.
Small weight: Such as a bag of coins, a small bag of sugar, or a keychain.
Stopwatch: Or a smartphone timer.
Ruler or Measuring Tape: For measuring the length of the pendulum.

[![Data captured during simulation](https://mg-2025p03.github.io/physics/_pics/materials.jpg)](https://mg-2025p03.github.io/physics/_pics/materials.jpg)

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

$$T = \frac{\bar{T}_{10}}{10} = 2.35s$$

The period of one oscillation.

- Determine Gravitational Acceleration $g$

$$
g = \frac{4\pi^2L}{T^2} = \frac{4\pi^2(1.31m)}{2.35s^2}
$$

$$
g = 9.33 m/s^2
$$

- Propagate Uncertainties

Calculate the uncertainty in $g$ based on uncertainties in $L$ and $T$.

Step 1: Calculate the Expected Period Using the computed $g$

Calculate the New Period $T_{expected}$ with the Correct Gravity:
Using $g = 9.33 , \text{m/s}^2$:

$$
T_{expected} = 2\pi \sqrt{\frac{L}{g}} = 2\pi \sqrt{\frac{1.31m}{9.33 m/s^2}}
$$

Calculating the square root:

$$
T_{expected} = 2\pi \sqrt{0.1408} \approx 2\pi \times 0.3741 \approx 2.35 , \text{s}
$$

Thus, the period calculated using $g = 9.33 m/s^2$  confirms the expected period remains around 2.35 s.

Step 2: Uncertainty Calculation

Given previous uncertainties in $L$ and $T$:
Uncertainty in $L: \Delta L = 0.01 , \text{m}$ Uncertainty in $T: ( \Delta T = 0.05 , \text{s}$ Using the relative uncertainty in $g$:

$$
\frac{\Delta g}{g} = \sqrt{\left(\frac{\Delta L}{L}\right)^2 + \left(2 \frac{\Delta T}{T}\right)^2}
$$

Calculating:

$$
\frac{\Delta L}{L} = \frac{0.01}{1.31} \approx 0.00763
$$

$$
\frac{\Delta T}{T} = \frac{0.05}{2.35} \approx 0.02128
$$

Calculating overall uncertainty:

$$
\frac{\Delta g}{g} = \sqrt{(0.00763)^2 + (2 \times 0.02128)^2}
$$

$$
\frac{\Delta g}{g} = \sqrt{0.0000582 + 0.0003622} \approx \sqrt{0.0004204} \approx 0.0205
$$

The absolute uncertainty in ( g ):

$$
\Delta g = g \times \frac{\Delta g}{g} \approx 9.33 \times 0.0205 \approx 0.191 , \text{m/s}^2
$$

Final Result
Thus, the computed value of gravitational acceleration based on the pendulum properties is:

$$
g = 9.33 , \text{m/s}^2 \pm 0.191 , \text{m/s}^2
$$

Conclusion
This calculation shows that with the updated $g = 9.33 , \text{m/s}^2$, the period aligns closely with the provided $T$. The uncertainty calculation indicates that the value for $g$ derived from the pendulum motion is reliable within the specified experimental limits. The values confirm the functioning of the pendulum under controlled conditions, reaffirming the accuracy of measurements.