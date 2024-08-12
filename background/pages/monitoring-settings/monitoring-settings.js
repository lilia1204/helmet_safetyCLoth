(function() {
    document.title = '监控设置';
    let monitoringInitialized = false;

    window.initMonitoringPage = function() {
        if (monitoringInitialized) return;
        monitoringInitialized = true;

        console.log('Monitoring page loaded');
        const monitoringList = document.getElementById('monitoring-list');
        const addMonitoringForm = document.getElementById('add-monitoring-form');
        const noResultsModalElement = document.getElementById('noResultsModal');
        const confirmDeleteModalElement = document.getElementById('confirmDeleteModal');
        const confirmStatusModalElement = document.getElementById('confirmStatusModal');
        const confirmDeleteButton = document.getElementById('confirm-delete');
        const confirmStatusChangeButton = document.getElementById('confirm-status-change');
        const cancelStatusChangeButton = document.getElementById('cancel-status-change');

        let noResultsModal;
        let confirmDeleteModal;
        let confirmStatusModal;

        if (noResultsModalElement) {
            noResultsModal = new bootstrap.Modal(noResultsModalElement);
        }
        if (confirmDeleteModalElement) {
            confirmDeleteModal = new bootstrap.Modal(confirmDeleteModalElement);
        }
        if (confirmStatusModalElement) {
            confirmStatusModal = new bootstrap.Modal(confirmStatusModalElement);
        }

        let monitoringData = [];
        let currentIndex;
        let currentID;
        let initialStatus;

        function fetchMonitoringData() {
            fetch('http://127.0.0.1:5000/monitor/getAll')
                .then(response => response.json())
                .then(data => {
                    if (data.code === 0) {
                        monitoringData = data.data;
                        renderMonitoringList(monitoringData);
                    } else {
                        console.error('Error fetching monitoring data:', data.message);
                    }
                })
                .catch(error => console.error('Error fetching monitoring data:', error));
        }

        function renderMonitoringList(data) {
            monitoringList.innerHTML = '';
            data.forEach((item, index) => {
                const row = document.createElement('tr');
                row.innerHTML = `
                    <td>${item.monitorName}</td>
                    <td>
                        <div class="form-check form-switch">
                            <input class="form-check-input toggle-monitoring" type="checkbox" id="monitoring-${index}" data-index="${index}" data-id="${item.monitorID}" ${item.isActive ? 'checked' : ''}>
                            <label class="form-check-label" for="monitoring-${index}"></label>
                        </div>
                    </td>
                    <td>
                        <button class="btn btn-danger btn-sm" data-index="${index}" data-id="${item.monitorID}">删除</button>
                    </td>
                `;
                monitoringList.appendChild(row);
            });

            // Add event listeners for the toggles and delete buttons after rendering
            document.querySelectorAll('.toggle-monitoring').forEach(toggle => {
                toggle.addEventListener('change', handleToggleChange);
            });

            document.querySelectorAll('.btn-danger').forEach(button => {
                button.addEventListener('click', handleDeleteClick);
            });
        }

        function handleToggleChange(event) {
            console.log('Toggle change detected');
            currentIndex = event.target.getAttribute('data-index');
            currentID = event.target.getAttribute('data-id');
            initialStatus = event.target.checked; // 记录初始状态
            console.log(`Initial status: ${initialStatus}`);
            if (confirmStatusModal) {
                confirmStatusModal.show();
            }
        }

        function handleDeleteClick(event) {
            console.log('Delete button clicked');
            currentIndex = event.target.getAttribute('data-index');
            currentID = event.target.getAttribute('data-id'); // 获取监控项ID
            if (confirmDeleteModal) {
                confirmDeleteModal.show();
            }
        }

        confirmDeleteButton.addEventListener('click', function() {
            const monitorID = currentID;
            console.log(monitorID)
            fetch('http://127.0.0.1:5000/monitor/delete', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ monitorID })
            })
            .then(response => response.json())
            .then(data => {
                if (data.code === 0) {
                    console.log('Delete successful:', data.message);
                    fetchMonitoringData(); // 重新获取监控数据
                } else {
                    console.error('Delete failed:', data.message);
                }
            })
            .catch(error => console.error('Error deleting monitoring item:', error));

            if (confirmDeleteModal) {
                confirmDeleteModal.hide();
            }
        });

        confirmStatusChangeButton.addEventListener('click', function() {
            const monitorID = currentID;
            const isActive = initialStatus ? 1 : 0;
            fetch('http://127.0.0.1:5000/monitor/setting', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ monitorID, isActive })
            })
            .then(response => response.json())
            .then(data => {
                if (data.code === 0) {
                    toggleMonitoringStatus(currentIndex);
                    console.log('Status update successful:', data.message);
                } else {
                    console.error('Status update failed:', data.message);
                }
            })
            .catch(error => console.error('Error updating monitoring status:', error));

            if (confirmStatusModal) {
                confirmStatusModal.hide();
            }
        });

        cancelStatusChangeButton.addEventListener('click', function() {
            // 恢复开关到初始状态
            console.log(`Restoring initial status: ${initialStatus}`);
            document.getElementById(`monitoring-${currentIndex}`).checked = !initialStatus;
            if (confirmStatusModal) {
                confirmStatusModal.hide();
            }
        });

        function deleteMonitoring(index) {
            monitoringData.splice(index, 1);
            renderMonitoringList(monitoringData);
        }

        function toggleMonitoringStatus(index) {
            monitoringData[index].isActive = !monitoringData[index].isActive;
            renderMonitoringList(monitoringData);
        }

        document.getElementById('button-search').addEventListener('click', function() {
            const searchValue = document.getElementById('search-monitoring').value.toLowerCase();
            const filteredData = monitoringData.filter(item => item.monitorName.toLowerCase().includes(searchValue));
            if (filteredData.length === 0) {
                if (noResultsModal) {
                    noResultsModal.show();
                }
            } else {
                renderMonitoringList(filteredData);
            }
        });

        addMonitoringForm.addEventListener('submit', function(event) {
            event.preventDefault();
            const monitorName = document.getElementById('monitoring-name').value.trim();
            const source = document.getElementById('monitoring-source').value.trim();
            const isActive = 0; // 默认值为0

            fetch('http://127.0.0.1:5000/monitor/add', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ monitorName, source, isActive })
            })
            .then(response => response.json())
            .then(data => {
                if (data.code === 0) {
                    fetchMonitoringData(); // 重新获取监控数据
                    console.log('Add successful:', data.message);
                } else {
                    console.error('Add failed:', data.message);
                }
            })
            .catch(error => console.error('Error adding monitoring item:', error));

            addMonitoringForm.reset();
            const addMonitoringModal = bootstrap.Modal.getInstance(document.getElementById('addMonitoringModal'));
            if (addMonitoringModal) {
                addMonitoringModal.hide();
            }
        });

        // Fetch monitoring data from backend on page load
        fetchMonitoringData();
    };
})();
