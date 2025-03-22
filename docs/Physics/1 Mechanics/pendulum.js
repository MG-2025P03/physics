// Parameters
const g = 9.81; // gravity
const L = 1.0; // length of pendulum
const beta = 0.1; // damping coefficient
const F0 = 1.5; // driving force amplitude
const omegaDrive = 2.0; // driving frequency

// Time parameters
const dt = 0.01; // time step
const totalTime = 100; // total simulation time
const poincareInterval = Math.PI * 2 / omegaDrive; // interval for Poincaré section

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
