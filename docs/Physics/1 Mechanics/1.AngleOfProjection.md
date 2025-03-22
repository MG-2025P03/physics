# Range as a Function of the Angle of Projection

[Range vs. Angle of Projection](index.html)

The angle of projection in projectile motion is a critical parameter that affects the trajectory, range, time of flight, and maximum height of a projectile. The angle of projection, combined with initial velocity, gravitational acceleration, and launch height, determines the path followed by the projectile. Let's break down how these parameters interact and the different sets of solutions that can arise:
1. Initial Velocity (v₀):

Definition: The speed at which the projectile is launched.
Impact: Affects the range and maximum height. For a given angle, increasing the initial velocity increases both the range and the height of the projectile.

2. Gravitational Acceleration (g):

Definition: The acceleration due to gravity, typically (9.81 , \text{m/s}^2) on Earth.
Impact: Acts downward, affecting the time of flight and the shape of the trajectory. It pulls the projectile downward, creating a parabolic path.

3. Launch Height (h):

Definition: The height from which the projectile is launched relative to the landing point.
Impact: Influences the time the projectile stays in the air and the range. A higher launch point allows for a longer flight time and potentially greater range, depending on the angle of projection.



Scripts/Codes
    <script>
        // Constants
        const g = 9.81; // acceleration due to gravity in m/s^2
        const v0 = 20; // initial velocity in m/s

        // Generate angles from 0 to 90 degrees
        const angles = [];
        for (let i = 0; i <= 90; i++) {
            angles.push(i);
        }

        // Calculate ranges for each angle
        const ranges = angles.map(angle => {
            const radians = angle * Math.PI / 180;
            return (Math.pow(v0, 2) * Math.sin(2 * radians)) / g;
        });

        // Plot data
        const trace = {
            x: angles,
            y: ranges,
            type: 'scatter',
            mode: 'lines+markers',
            name: 'Range'
        };

        const layout = {
            title: 'Projectile Range vs. Angle of Projection',
            xaxis: { title: 'Angle of Projection (degrees)' },
            yaxis: { title: 'Range (meters)' }
        };

        Plotly.newPlot('plot', [trace], layout);
    </script>



