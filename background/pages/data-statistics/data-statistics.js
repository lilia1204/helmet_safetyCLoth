(function() {
    document.title = '数据统计';
    console.log('Data statistics script loaded');
    let statisticsInitialized = false;

    function initDataStatisticsPage() {
        if (statisticsInitialized) return;
        statisticsInitialized = true;

        console.log('Data statistics page loaded');

        // 发起请求获取数据
        fetch('http://127.0.0.1:5000/alert/monthly')
            .then(response => response.json())
            .then(data => {
                if (data.code === 0) {
                    console.log('Data fetched successfully:', data.data);
                    renderCharts(data.data);
                } else {
                    console.error('Error fetching data:', data.message);
                }
            })
            .catch(error => console.error('Error fetching data:', error));
    }

    function renderCharts(data) {
        console.log('Rendering charts with data:', data);
        const lineChartCtx = document.getElementById('line-chart').getContext('2d');
        const pieChartCtx = document.getElementById('pie-chart').getContext('2d');

        // 提取所有日期并排序
        const allDates = Array.from(new Set(data.flatMap(item => item.dates))).sort();

        // 生成线状图数据
        const lineChartData = {
            labels: allDates,
            datasets: data.map((item, index) => ({
                label: item.name,
                data: allDates.map(date => item.counts[date] || 0),
                borderColor: `hsl(${index * 60}, 70%, 50%)`,
                backgroundColor: `hsla(${index * 60}, 70%, 50%, 0.5)`,
                fill: false
            }))
        };

        // 渲染线状图
        new Chart(lineChartCtx, {
            type: 'line',
            data: lineChartData,
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: {
                        position: 'top',
                    },
                    title: {
                        display: true,
                        text: '每天警报次数'
                    }
                },
                scales: {
                    y: {
                        beginAtZero: true
                    }
                }
            }
        });

        // 生成饼状图数据，不包括 "all"
        const pieChartData = {
            labels: data.filter(item => item.name !== 'all').map(item => item.name),
            datasets: [{
                data: data.filter(item => item.name !== 'all').map(item => item.count),
                backgroundColor: data.map((_, index) => `hsl(${index * 60}, 70%, 50%)`)
            }]
        };

        // 渲染饼状图
        new Chart(pieChartCtx, {
            type: 'pie',
            data: pieChartData,
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: {
                        position: 'top',
                    },
                    title: {
                        display: true,
                        text: '每个监控警报总次数'
                    }
                }
            }
        });
    }

    // 直接调用初始化函数以在页面加载时发起请求
    initDataStatisticsPage();
})();
