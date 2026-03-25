let historyData = [];
let anomalies = [];
let charts = {};

async function loadCharts() {

    // fetch data
    const historyResponse = await fetch("/metrics/history");
    historyData = await historyResponse.json();

    const anomalyResponse = await fetch("/metrics/anomalies");
    anomalies = await anomalyResponse.json();

    const timestamps = historyData.map(item => item.timestamp);
    const cpu = historyData.map(item => item.cpu);
    const memory = historyData.map(item => item.memory);
    const disk = historyData.map(item => item.disk);

    // Convert ANY timestamp format to: YYYY-MM-DD HH:MM:SS
    function normalize(ts) {
        const d = new Date(ts);
        return (
            d.getFullYear() + "-" +
            String(d.getMonth()+1).padStart(2,'0') + "-" +
            String(d.getDate()).padStart(2,'0') + " " +
            String(d.getHours()).padStart(2,'0') + ":" +
            String(d.getMinutes()).padStart(2,'0') + ":" +
            String(d.getSeconds()).padStart(2,'0')
        );
    }

    // generate anomaly dataset aligned with history
    function getAnomalyPoints(metricValues) {

        return historyData.map((item, index) => {

            const itemTime = normalize(item.timestamp);

            const match = anomalies.find(a =>
                normalize(a.timestamp) === itemTime
            );

            return match ? metricValues[index] : null;
        });
    }

    function createChart(canvasId, label, dataValues, anomalyValues, color) {

        if (charts[canvasId]) {
            charts[canvasId].destroy();
        }

        const ctx = document.getElementById(canvasId).getContext("2d");

        const gradient = ctx.createLinearGradient(0, 0, 0, 300);
        gradient.addColorStop(0, color + "55");
        gradient.addColorStop(1, color + "00");

        charts[canvasId] = new Chart(ctx, {
            type: "line",
            data: {
                labels: timestamps,
                datasets: [
                    {
                        label: label,
                        data: dataValues,
                        borderColor: color,
                        backgroundColor: gradient,
                        fill: true,
                        tension: 0.4,
                        pointRadius: 2
                    },
                    {
                        label: "Anomaly",
                        data: anomalyValues,
                        borderColor: "#990000",
                        backgroundColor: "#fa0b0b",
                        pointStyle: "rectRot",
                        pointRadius: 6,
                        pointHoverRadius: 8,
                        showLine: false
                    }
                ]
            },
            options: {
                responsive: true,
                interaction: {
                    mode: "index",
                    intersect: false
                },
                plugins: {
                    legend: {
                        labels: { color: "white" }
                    },
                    tooltip: {
                        backgroundColor: "#1e293b",
                        titleColor: "white",
                        bodyColor: "white",
                        borderColor: "#334155",
                        borderWidth: 1
                    }
                },
                scales: {
                    x: {
                        ticks: { color: "white" },
                        grid: { color: "#334155" },
                        title: {
                            display: true,
                            text: "Timestamp",
                            color: "#94a3b8"
                        }
                    },
                    y: {
                        ticks: { color: "white" },
                        grid: { color: "#334155" },
                        beginAtZero: false,
                        title: {
                            display: true,
                            text: "Usage %",
                            color: "#94a3b8"
                        }
                    }
                }
            }
        });
    }

    createChart("cpuChart", "CPU Usage %", cpu, getAnomalyPoints(cpu), "#78433f");
    createChart("memoryChart", "Memory Usage %", memory, getAnomalyPoints(memory), "#3b82f6");
    createChart("diskChart", "Disk Usage %", disk, getAnomalyPoints(disk), "#22c55e");
}

loadCharts();
setInterval(loadCharts, 10000);