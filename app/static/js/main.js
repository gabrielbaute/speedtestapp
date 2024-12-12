document.addEventListener('DOMContentLoaded', (event) => {
    const updateChart = (url, chartElementId, datasets) => {
        const chartElement = document.getElementById(chartElementId);
        if (chartElement) {
            fetch(url)
                .then(response => {
                    if (!response.ok) {
                        throw new Error(`HTTP error! status: ${response.status}`);
                    }
                    return response.json();
                })
                .then(data => {
                    console.log('Chart data:', data); // Verificar los datos
                    const ctx = chartElement.getContext('2d');
                    new Chart(ctx, {
                        type: 'line',
                        data: {
                            labels: data.dates,
                            datasets: datasets.map(ds => ({
                                label: ds.label,
                                data: data[ds.dataKey],
                                borderColor: ds.color,
                                borderWidth: 1,
                                fill: false
                            }))
                        },
                        options: {
                            scales: {
                                x: {
                                    type: 'time',
                                    time: {
                                        unit: 'day'
                                    }
                                },
                                y: {
                                    beginAtZero: true
                                }
                            }
                        }
                    });
                })
                .catch(error => console.error('Error fetching chart data:', error));
        }
    };

    const updateSpeedChart = (timeRange) => {
        const url = `/api/speedtest_results?time_range=${timeRange}`;
        const datasets = [
            { label: 'Download Speed (Mbps)', dataKey: 'download_speeds', color: 'rgba(75, 192, 192, 1)' },
            { label: 'Upload Speed (Mbps)', dataKey: 'upload_speeds', color: 'rgba(153, 102, 255, 1)' }
        ];
        updateChart(url, 'speedChart', datasets);
    };

    const updateLatencyChart = (timeRange) => {
        const url = `/api/latency_results?time_range=${timeRange}`;
        const datasets = [
            { label: 'Latency (ms)', dataKey: 'latencies', color: 'rgba(255, 99, 132, 1)' }
        ];
        updateChart(url, 'latencyChart', datasets);
    };

    const speedChartElement = document.getElementById('speedChart');
    const latencyChartElement = document.getElementById('latencyChart');
    const timeRangeSelect = document.getElementById('timeRangeSelect');

    if (speedChartElement) {
        updateSpeedChart('24h'); // Mostrar las últimas 24 horas por defecto
    }

    if (latencyChartElement) {
        updateLatencyChart('24h'); // Mostrar las últimas 24 horas por defecto
    }

    if (timeRangeSelect) {
        timeRangeSelect.addEventListener('change', (event) => {
            const timeRange = event.target.value;
            if (speedChartElement) {
                updateSpeedChart(timeRange);
            }
            if (latencyChartElement) {
                updateLatencyChart(timeRange);
            }
        });
    }
});
