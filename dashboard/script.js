async function loadCharts() {

    const response = await fetch("/metrics/history");
    const data = await response.json();

    const timestamps = data.map(item => item.timestamp);
    const cpu = data.map(item => item.cpu);
    const memory = data.map(item => item.memory);

    new Chart(document.getElementById("cpuChart"), {
        type: "line",
        data: {
            labels: timestamps,
            datasets: [{
                label: "CPU %",
                data: cpu,
                borderColor: "red",
                fill: false
            }]
        }
    });

    new Chart(document.getElementById("memoryChart"), {
        type: "line",
        data: {
            labels: timestamps,
            datasets: [{
                label: "Memory %",
                data: memory,
                borderColor: "blue",
                fill: false
            }]
        }
    });
}

loadCharts();
