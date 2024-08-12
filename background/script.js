document.addEventListener('DOMContentLoaded', function() {
    const sidebarLinks = document.querySelectorAll('.sidebar a');
    const mainContentContainer = document.getElementById('main-content-container');
    const logoutButton = document.getElementById('logoutButton');

    sidebarLinks.forEach(link => {
        link.addEventListener('click', function(event) {
            event.preventDefault();
            sidebarLinks.forEach(link => link.classList.remove('active'));
            link.classList.add('active');
            const content = link.getAttribute('data-content');
            loadContent(content);
        });
    });

    logoutButton.addEventListener('click', function() {
        window.location.href = 'pages/login/login.html';  // 更改此路径以指向您的登录页面
    });

    function loadContent(content) {
        const url = `pages/${content}/${content}.html`;
        console.log(`Loading content from: ${url}`);
        fetch(url)
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.text();
            })
            .then(data => {
                mainContentContainer.innerHTML = data;
                console.log(`Content loaded for: ${content}`);
                loadPageScriptsAndStyles(content);
            })
            .catch(error => {
                console.error('Error loading content:', error);
                mainContentContainer.innerHTML = '<p>无法加载内容，请稍后再试。</p>';
            });
    }

    function loadPageScriptsAndStyles(content) {
        const styleUrl = `pages/${content}/${content}.css`;
        const scriptUrl = `pages/${content}/${content}.js`;

        console.log(`Loading styles from: ${styleUrl}`);
        console.log(`Loading scripts from: ${scriptUrl}`);

        // Remove existing page-specific styles and scripts
        removePageSpecificElements();

        // Load the new styles
        if (!document.querySelector(`link[href="${styleUrl}"]`)) {
            const link = document.createElement('link');
            link.rel = 'stylesheet';
            link.href = styleUrl;
            link.className = 'page-specific';
            document.head.appendChild(link);
        }

        // Load the new scripts
        if (!document.querySelector(`script[src="${scriptUrl}"]`)) {
            const script = document.createElement('script');
            script.src = scriptUrl;
            script.className = 'page-specific';
            script.onload = function() {
                console.log(`Script ${scriptUrl} loaded`);
                if (content === 'monitoring-settings' && typeof initMonitoringPage === 'function') {
                    console.log('Initializing monitoring settings page');
                    initMonitoringPage();
                }
                if (content === 'view-records' && typeof initViewRecordsPage === 'function') {
                    console.log('Initializing view records page');
                    initViewRecordsPage();
                }
                if (content === 'data-statistics' && typeof initDataStatisticsPage === 'function') {
                    console.log('Initializing data statistics page');
                    initDataStatisticsPage();
                }
            };
            document.body.appendChild(script);
        } else {
            // If the script is already loaded, directly call the initialization function
            console.log(`Script ${scriptUrl} already loaded`);
            if (content === 'monitoring-settings' && typeof initMonitoringPage === 'function') {
                console.log('Initializing monitoring settings page');
                initMonitoringPage();
            }
            if (content === 'view-records' && typeof initViewRecordsPage === 'function') {
                console.log('Initializing view records page');
                initViewRecordsPage();
            }
            if (content === 'data-statistics' && typeof initDataStatisticsPage === 'function') {
                console.log('Initializing data statistics page');
                initDataStatisticsPage();
            }
        }
    }

    function removePageSpecificElements() {
        // Remove existing page-specific styles and scripts
        document.querySelectorAll('.page-specific').forEach(el => el.remove());
    }
});
