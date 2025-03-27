function calculateTrajectory(velocity, angle, gravity, height) {
    const angleRad = (Math.PI / 180) * angle;
    const vX = velocity * Math.cos(angleRad);
    const vY = velocity * Math.sin(angleRad);

    const flightTime = (vY + Math.sqrt(vY * vY + 2 * gravity * height)) / gravity;
    const deltaTime = flightTime / 100; // divide flight time into small increments

    const xValues = [];
    const yValues = [];

    for (let t = 0; t <= flightTime; t += deltaTime) {
        const x = vX * t;
        const y = height + vY * t - 0.5 * gravity * t * t;

        xValues.push(x);
        yValues.push(y);
    }

    return { xValues, yValues };
}

function plotProjectile() {
    const velocity = parseFloat(document.getElementById('velocity').value);
    const angle = parseFloat(document.getElementById('angle').value);
    const gravity = parseFloat(document.getElementById('gravity').value);
    const height = parseFloat(document.getElementById('height').value);

    const { xValues, yValues } = calculateTrajectory(velocity, angle, gravity, height);

    const trace = {
        x: xValues,
        y: yValues,
        type: 'scatter',
        mode: 'lines',
        name: 'Trajectory'
    };

    const layout = {
        title: 'Projectile Motion: Range vs Height',
        xaxis: {
            title: 'Range (meters)'
        },
        yaxis: {
            title: 'Height (meters)'
        }
    };

    Plotly.newPlot('plot', [trace], layout);
}
