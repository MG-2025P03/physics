function simulate() {
    // Retrieve parameters from inputs
    const g = parseFloat(document.getElementById('g').value);
    const L = parseFloat(document.getElementById('L').value);
    const beta = parseFloat(document.getElementById('beta').value);
    const F0 = parseFloat(document.getElementById('F0').value);
    const omegaDrive = parseFloat(document.getElementById('omegaDrive').value);
    const dt = parseFloat(document.getElementById('dt').value);
    const totalTime = parseFloat(document.getElementById('totalTime').value);

    // Initialize variables
    let theta = 0.1; // initial angle
    let omega = 0.0; // initial angular velocity
    let time = 0.0;

    // Data arrays for phase diagram and Poincaré section
    let phaseData = [];
    let poincareData = [];

    // Simulation loop
    while (time < totalTime) {
        // Calculate angular acceleration
        const alpha = -(g / L) * Math.sin(theta) - beta * omega + (F0 / L) * Math.cos(omegaDrive * time);

        // Update angular velocity and angle
        omega += alpha * dt;
        theta += omega * dt;

        // Record phase data
        phaseData.push({ x: theta, y: omega });

        // Record Poincaré section data at driving period intervals
        const poincareInterval = Math.PI * 2 / omegaDrive;
        if (Math.abs((time % poincareInterval) - poincareInterval) < dt) {
            poincareData.push({ x: theta, y: omega });
        }

        // Increment time
        time += dt;
    }

    // Plot phase diagram using Plotly
    Plotly.newPlot('phaseDiagram', [{
        x: phaseData.map(point => point.x),
        y: phaseData.map(point => point.y),
        mode: 'lines',
        name: 'Phase Diagram'
    }], {
        title: 'Phase Diagram',
        xaxis: { title: 'Theta (rad)' },
        yaxis: { title: 'Omega (rad/s)' }
    });

    // Plot Poincaré section using Plotly
    Plotly.newPlot('poincareSection', [{
        x: poincareData.map(point => point.x),
        y: poincareData.map(point => point.y),
        mode: 'markers',
        name: 'Poincaré Section'
    }], {
        title: 'Poincaré Section',
        xaxis: { title: 'Theta (rad)' },
        yaxis: { title: 'Omega (rad/s)' }
    });
}

// Initial simulation on page load
simulate();
