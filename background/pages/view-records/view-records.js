(function() {
    document.title = '查看记录';
    let recordsInitialized = false;
    let monitorNameToID = {};

    window.initViewRecordsPage = function() {
        if (recordsInitialized) return;
        recordsInitialized = true;

        console.log('View records page loaded');
        const recordsList = document.getElementById('records-list');
        const searchButton = document.getElementById('button-search-records');
        const searchInput = document.getElementById('search-records');
        const dateFilter = document.getElementById('filter-date');
        const errorMessage = document.getElementById('error-message');  // 错误信息元素

        let recordsData = [];

        function renderRecordsList(data) {
            recordsList.innerHTML = '';
            data.forEach((item) => {
                const row = document.createElement('tr');
                row.innerHTML = `
                    <td>${item.monitorName}</td>
                    <td>${item.timestamp}</td>
                `;
                recordsList.appendChild(row);
            });
        }

        function fetchRecords() {
            fetch('http://127.0.0.1:5000/record/getAll')
                .then(response => response.json())
                .then(data => {
                    if (data.code === 0) {
                        recordsData = data.data;
                        monitorNameToID = {};
                        recordsData.forEach(item => {
                            monitorNameToID[item.monitorName] = item.monitorID;
                        });
                        renderRecordsList(recordsData);
                    } else {
                        console.error('Error fetching records:', data.message);
                    }
                })
                .catch(error => console.error('Error fetching records:', error));
        }

        function fetchFilteredRecords(url, payload) {
            fetch(url, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(payload)
            })
            .then(response => response.json())
            .then(data => {
                if (data.code === 0) {
                    if (data.data.length === 0) {
                        new bootstrap.Modal(document.getElementById('noResultsModal')).show();
                    } else {
                        renderRecordsList(data.data);
                    }
                } else {
                    console.error('Error fetching filtered records:', data.message);
                }
            })
            .catch(error => console.error('Error fetching filtered records:', error));
        }

        searchButton.addEventListener('click', function() {
            const searchValue = searchInput.value.trim();
            const dateValue = dateFilter.value;

            if (searchValue && monitorNameToID[searchValue]) {
                const monitorID = monitorNameToID[searchValue];
                if (dateValue) {
                    fetchFilteredRecords('http://127.0.0.1:5000/record/filterByTime', { timestamp: dateValue });
                }
                fetchFilteredRecords('http://127.0.0.1:5000/record/filterByMonitor', { monitorID: monitorID });
                if (errorMessage) errorMessage.style.display = 'none';
            } else if (dateValue) {
                fetchFilteredRecords('http://127.0.0.1:5000/record/filterByTime', { timestamp: dateValue });
                if (errorMessage) errorMessage.style.display = 'none';
            } else {
                if (searchValue && !monitorNameToID[searchValue]) {
                    if (errorMessage) {
                        errorMessage.textContent = '监控名不存在，请输入正确的监控名';
                        errorMessage.style.display = 'block';
                    }
                } else {
                    console.log('No filters applied, fetching all records');
                    fetchRecords();
                }
            }
        });

        fetchRecords();
    };
})();
