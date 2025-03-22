function calculateRange(v0, angle) {
    const g = 9.81; // acceleration due to gravity (m/s^2)
    return (v0 ** 2 * Math.sin(2 * angle * Math.PI / 180)) / g;
}

function plotProjectileMotion() {
    const initialVelocity = parseFloat(document.getElementById("initialVelocity").value);
    const canvas = document.getElementById("motionCanvas");
    const ctx = canvas.getContext("2d");
    
    // Clear the canvas
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    ctx.beginPath();
    
    const angles = Array.from({length: 91}, (_, i) => i); // angles from 0 to 90
    const ranges = angles.map(angle => calculateRange(initialVelocity, angle));

    // Plotting
    ctx.moveTo(50, canvas.height - 50); // move to the starting point
    angles.forEach((angle, index) => {
        const x = angle * (canvas.width - 100) / 90 + 50; // Scale x to canvas width
        const y = canvas.height - (ranges[index] * (canvas.height - 100) / Math.max(...ranges)); // Scale y to canvas height
        ctx.lineTo(x, y);
    });

    ctx.strokeStyle = "blue";
    ctx.stroke();
    
    // Axes
    ctx.beginPath();
    ctx.moveTo(50, 350);
    ctx.lineTo(50, 50);
    ctx.lineTo(750, 350);
    ctx.stroke();
    
    // Labels
    ctx.fillStyle = "black";
    ctx.fillText("Angle of Projection (degrees)", 350, 380);
    ctx.fillText("Range (m)", 10, 20);
}
