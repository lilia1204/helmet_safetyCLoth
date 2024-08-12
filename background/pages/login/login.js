document.addEventListener('DOMContentLoaded', function() {
    const loginForm = document.getElementById('loginForm');
    const registerButton = document.querySelector('.text-center a');

    loginForm.addEventListener('submit', function(event) {
        event.preventDefault();
        const username = document.getElementById('username').value;
        const password = document.getElementById('password').value;

        if (!username) {
            document.getElementById('username').classList.add('is-invalid');
            document.querySelector('#username + .invalid-feedback').textContent = '用户名不能为空。';
        } else {
            document.getElementById('username').classList.remove('is-invalid');
        }

        if (!password) {
            document.getElementById('password').classList.add('is-invalid');
            document.querySelector('#password + .invalid-feedback').textContent = '密码不能为空。';
        } else {
            document.getElementById('password').classList.remove('is-invalid');
        }

        if (username && password) {
            // 发起登录请求
            fetch('http://127.0.0.1:5000/admin/login', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ userName: username, password: password })
            })
            .then(response => response.json())
            .then(data => {
                if (data.code === 0) {
                    window.location.href = '/index.html';  // 更改此路径以指向你的首页
                } else {
                    // 处理后端返回的错误代码并显示相应的中文提示
                    let errorMessage;
                    switch(data.code) {
                        case -1:
                            errorMessage = '用户不存在。';
                            break;
                        case -2:
                            errorMessage = '密码错误。';
                            break;
                        case -98:
                            errorMessage = '数据错误。';
                            break;
                        case -100:
                            errorMessage = '缺少必要的参数。';
                            break;
                        default:
                            errorMessage = '登录失败，请稍后再试。';
                    }
                    alert(`登录失败: ${errorMessage}`);
                }
            })
            .catch(error => {
                console.error('Error:', error);
                alert('登录过程中发生错误，请稍后再试。');
            });
        }
    });

    registerButton.addEventListener('click', function() {
        window.location.href = '/pages/register/register.html';  // 更改此路径以指向注册页面
    });
});
