async function loadCharts() {

    const response = await fetch("/metrics/history");
    const data = await response.json();

    const timestamps = data.map(item => item.timestamp);
    const cpu = data.map(item => item.cpu);
    const memory = data.map(item => item.memory);
    const disk = data.map(item => item.disk);

    function createChart(canvasId, label, dataValues, color) {

        const ctx = document.getElementById(canvasId).getContext("2d");

        const gradient = ctx.createLinearGradient(0, 0, 0, 300);
        gradient.addColorStop(0, color + "55");
        gradient.addColorStop(1, color + "00");

        new Chart(ctx, {
            type: "line",
            data: {
                labels: timestamps,
                datasets: [{
                    label: label,
                    data: dataValues,
                    borderColor: color,
                    backgroundColor: gradient,
                    fill: true,
                    tension: 0.4,
                    pointRadius: 2
                }]
            },
            options: {
                responsive: true,
                plugins: {
                    legend: {
                        labels: {
                            color: "white"
                        }
                    }
                },
                scales: {
                    x: {
                        ticks: { color: "white" },
                        grid: { color: "#334155" }
                    },
                    y: {
                        ticks: { color: "white" },
                        grid: { color: "#334155" },
                        beginAtZero: false   // 🔥 this removes flat-line effect
                    }
                }
            }
        });
    }

    createChart("cpuChart", "CPU %", cpu, "#ef4444");
    createChart("memoryChart", "Memory %", memory, "#3b82f6");
    createChart("diskChart", "Disk %", disk, "#22c55e");
}

loadCharts();