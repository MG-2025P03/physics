# Electromagnetism

Electromagnetism is a fundamental branch of physics that deals with the study of electric and magnetic fields and their interactions with matter, particularly charged particles. Below is a detailed analysis covering various aspects, including applications, simulations, and parameter explorations:

## Applications of Electromagnetism and the Lorentz Force

### Lorentz Force in Systems

![Figure 1 - Circular Motion of a Charged Particle in a Magnetic Field](https://mg-2025p03.github.io/physics/_pics/ele01.png)

### Particle Accelerators

Particle accelerators use electromagnetic fields to accelerate charged particles to high speeds and contain them within a well-defined path. The Lorentz force is crucial in bending and focusing the particle beams using magnetic fields.

### Circular motion simulation of a charged particle under a magnetic field into a 3D visualization

![Figure 2 - Circular Motion of a Charged Particle in a Magnetic Field (3D)](https://mg-2025p03.github.io/physics/_pics/ele03.png)

To further illustrate a helical path of a charged particle in a magnetic field, we can simulate its motion when the initial velocity has components both parallel and perpendicular to the magnetic field direction. This example will focus solely on the helical trajectory caused by a magnetic field.
Here is a Python script that demonstrates this motion using 3D visualization

![Figure 3 -  Helical Motion of a Charged Particle in Crossed E and B Fields](https://mg-2025p03.github.io/physics/_pics/ele02.png)

### Mass Spectrometers

Mass spectrometers use the Lorentz force to separate ions based on their mass-to-charge ratio. When ions pass through magnetic and/or electric fields, they are deflected, allowing their trajectories to be analyzed for identification.

![Figure 4 - Mass Spectrometer: Ion Trajectories Based on Mass-to-Charge Ratio](https://mg-2025p03.github.io/physics/_pics/ele05.png)

### Plasma Confinement

In devices like tokamaks used in nuclear fusion research, magnetic fields are employed to confine plasma, relying on the Lorentz force to maintain stability and control the motion of charged particles within the plasma.

![Figure 5 - 3D Representation of Plasma Confinement in a Toroidal Field](https://mg-2025p03.github.io/physics/_pics/ele07.png)

### Control of Charged Particles

Electric Fields $E$: Electric fields exert a force on charged particles, changing their velocity linearly in the direction of the field. This is particularly useful in accelerating particles or deflecting them in devices like cathode ray tubes.
Magnetic Fields $B$: Magnetic fields exert a perpendicular force on moving charged particles, affecting their trajectory without changing their speed. This causes particles to move in circular or helical paths.

Simulating Particle Motion
To simulate the trajectory of a charged particle under different field configurations, we can consider:

### Uniform Magnetic Field

A charged particle moving perpendicular to a uniform magnetic field will undergo circular motion due to the centripetal force provided by the Lorentz force.
The radius of the circle $ r $ can be determined by the equation: $r = \frac{mv}{qB}$, where $m$ is the mass, $v$ is the velocity, $q$ is the charge, and $B$ is the magnetic field strength.

![Figure 6 - Circular Motion in a Uniform Magnetic Field](https://mg-2025p03.github.io/physics/_pics/ele08.png)

### Combined Uniform Electric and Magnetic Fields

When both fields are present, particles experience both linear acceleration (from the electric field) and circular motion or drift motion (from the magnetic field).
Depending on the orientation and magnitudes, particles may exhibit helical motion or drift in the direction perpendicular to both fields.

### Crossed Electric and Magnetic Fields

When electric and magnetic fields are perpendicular, one can observe phenomena like the Hall effect, where particles drift due to the combined effect of $\overrightarrow{E}$ and $\overrightarrow{B}$.

![Figure 7 - Particle in Electric and Magnetic Fields](https://mg-2025p03.github.io/physics/_pics/ele08.png)