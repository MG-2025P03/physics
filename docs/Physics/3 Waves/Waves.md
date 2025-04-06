# Analysis of Wave Interference Patterns Formed by Point Sources at the Vertices of a Square

1. Parameters - Square as a regular polygon

A square has four equal sides and four vertices. For this analysis, we'll consider a square lying on a plane with vertices positioned at:

Vertex A (0, 0)<br/>
Vertex B (d, 0)<br/>
Vertex C (d, d)<br/>
Vertex D (0, d)

where $d$ is the side length of the square.

2. Position the Sources
Place point wave sources at each of the vertices (A, B, C, and D) of the square. Each source will emit circular wave fronts.

3. Wave Equations
Assuming a simple harmonic wave emitted from each source with the same frequency and amplitude, the wave equation from a point source located at position $x_0, y_0$ can be described by:

$$
\psi(x, y, t) = A \cos(kr - \omega t + \phi)
$$

where:

$ \psi $ is the wave displacement

$ A $ is the amplitude

$ k $ is the wave number, given by $ k = \frac{2\pi}{\lambda} $

$ \omega $ is the angular frequency, given by $ \omega = 2\pi f $

$ r = \sqrt{(x - x_0)^2 + (y - y_0)^2} $ is the distance from the source to the point $x, y$

$ \phi $ is the phase constant

$ \lambda $ is the wavelength

$ f $ is the frequency

For our four point sources:

$$
\psi_A(x, y, t) = A \cos(k\sqrt{x^2 + y^2} - \omega t)
$$

$$
\psi_B(x, y, t) = A \cos(k\sqrt{(x - d)^2 + y^2} - \omega t)
$$

$$
\psi_C(x, y, t) = A \cos(k\sqrt{(x - d)^2 + (y - d)^2} - \omega t)
$$

$$
\psi_D(x, y, t) = A \cos(k\sqrt{x^2 + (y - d)^2} - \omega t)
$$

4. Superposition of Waves
The principle of superposition states that the resultant wave displacement at any point on the water surface is the sum of the displacements due to each individual wave. Therefore, the total wave displacement $\Psi(x, y, t$ is given by:

$$
\Psi(x, y, t) = \psi_A(x, y, t) + \psi_B(x, y, t) + \psi_C(x, y, t) + \psi_D(x, y, t)
$$

This equation represents the interference pattern on the water surface.

5. Interference Patterns

Constructive Interference: Occurs at points where the path difference between waves from two or more sources is an integer multiple of the wavelength $ m\lambda $, where $ m $ is an integer. At these points, the waves reinforce each other, resulting in larger amplitudes.

Destructive Interference: Occurs at points where the path difference is an odd multiple of half wavelengths $m + \frac{1}{2})\lambda$. Here, the waves cancel each other, resulting in nodes or points of no displacement.

## Combined Displacement Function

The resultant wave displacement at a point ((x, y)) at time (t) is given by:

$$
\Psi(x, y, t) = \psi_A(x, y, t) + \psi_B(x, y, t) + \psi_C(x, y, t) + \psi_D(x, y, t)
$$

where each $ \psi $ is the wave equation from an individual source.

## Interference Pattern Analysis

1. Expression in Simplified Terms:
For simplicity, assume all waves have the same amplitude (A), wave number (k), and frequency (\omega). Let:

$$r_A = \sqrt{x^2 + y^2}$$
$$r_B = \sqrt{(x - d)^2 + y^2}$$
$$r_C = \sqrt{(x - d)^2 + (y - d)^2}$$
$$r_D = \sqrt{x^2 + (y - d)^2}$$

The total displacement becomes:

$$
\Psi(x, y, t) = A [\cos(kr_A - \omega t) + \cos(kr_B - \omega t) + \cos(kr_C - \omega t) + \cos(kr_D - \omega t)]
$$

2. Constructive Interference (Amplification):
Constructive interference occurs where waves meet in phase, i.e., their peaks and troughs align. This happens when the path difference between any pair of waves is an integral multiple of the wavelength ((n\lambda)):

$$r_i - r_j = n \lambda$$

These points are where the displacement $\Psi$ achieves its maximum, resulting in amplification.
3. Destructive Interference (Cancellation):
Destructive interference occurs when waves meet out of phase, i.e., the peak of one wave aligns with the trough of another. This occurs when the path difference is an odd multiple of half the wavelength $n + \frac{1}{2})\lambda$:

$$
r_i - r_j = (n + \frac{1}{2}) \lambda
$$

These points are where the displacement $\Psi$ is minimized or nullified.
4. Spatial Patterns:

Constructive Zones: Form a lattice of high-amplitude nodes where constructive interference dominates.
Destructive Zones: Occur as a grid-like pattern of nodal lines between the constructive nodes.

5. Temporal Analysis:
The time-dependent factor $-\omega t$ governs the oscillation of patterns, ensuring that regions of constructive and destructive interference fluctuate over time, causing the interference pattern to move dynamically on the water surface. However, the general stationary pattern remains the same.

## Conclusion

The superposition of waves from the four point sources will create a complex pattern of interference, characterized by alternating areas of constructive and destructive interference, forming a lattice-like pattern on the water surface. The symmetries of the square and the coherent nature of the wave sources determine the regularity of these interference patterns.
To visualize the detailed interference pattern, numerical simulation or graphical representation can be employed to reveal the specific constructive and destructive zones across the water surface.

The interference patterns on the water surface will consist of alternating regions of constructive and destructive interference. These patterns manifest as a regular grid-like structure due to the symmetry of the square arrangement of point sources, with moving wave fronts creating dynamic shifts over time.