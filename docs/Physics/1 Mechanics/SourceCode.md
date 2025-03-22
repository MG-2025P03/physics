```
function calculateRange(velocity, angle, gravity, height) {
    const angleRad = (Math.PI / 180) * angle;
    const vX = velocity * Math.cos(angleRad);
    const vY = velocity * Math.sin(angleRad);

    // Time to reach the highest point
    const tUp = vY / gravity;
    const tDown = Math.sqrt((vY ** 2 + 2 * gravity * height) / gravity ** 2);
    const totalTime = tUp + tDown;

    // Calculate range
    return vX * totalTime;
}

function plotProjectile() {
    const velocity = parseFloat(document.getElementById('velocity').value);
    const angle = parseFloat(document.getElementById('angle').value);
    const gravity = parseFloat(document.getElementById('gravity').value);
    const height = parseFloat(document.getElementById('height').value);

    const ranges = [];
    const angles = [];

    for (let a = 0; a <= 90; a += 1) {
        angles.push(a);
        ranges.push(calculateRange(velocity, a, gravity, height));
    }

    const trace = {
        x: angles,
        y: ranges,
        type: 'scatter',
        mode: 'lines+markers',
        name: 'Range vs Angle'
    };

    const layout = {
        title: 'Projectile Motion',
        xaxis: {
            title: 'Angle of Projection (degrees)'
        },
        yaxis: {
            title: 'Range (meters)'
        }
    };

    Plotly.newPlot('plot', [trace], layout);
}
```
