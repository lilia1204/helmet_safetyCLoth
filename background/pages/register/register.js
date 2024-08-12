document.addEventListener('DOMContentLoaded', function() {
    const registerForm = document.getElementById('registerForm');
    const loginButton = document.querySelector('.text-center a');

    registerForm.addEventListener('submit', function(event) {
        event.preventDefault();
        const username = document.getElementById('username').value;
        const password = document.getElementById('password').value;
        const confirmPassword = document.getElementById('confirm-password').value;

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

        if (!confirmPassword) {
            document.getElementById('confirm-password').classList.add('is-invalid');
            document.querySelector('#confirm-password + .invalid-feedback').textContent = '确认密码不能为空。';
        } else {
            document.getElementById('confirm-password').classList.remove('is-invalid');
        }

        if (password !== confirmPassword) {
            document.getElementById('confirm-password').classList.add('is-invalid');
            alert('密码和确认密码不一致');
        } else if (username && password && confirmPassword) {
            // 发起注册请求
            fetch('http://127.0.0.1:5000/admin/register', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ userName: username, password: password })
            })
            .then(response => response.json())
            .then(data => {
                if (data.code === 0) {
                    alert('注册成功，请登录');
                    window.location.href = '/pages/login/login.html';  // 更改此路径以指向登录页面
                } else {
                    // 处理后端返回的错误代码并显示相应的中文提示
                    let errorMessage;
                    switch(data.code) {
                        case -1:
                            errorMessage = '用户名已存在。';
                            break;
                        case -98:
                        case -99:
                            errorMessage = '数据库错误，请稍后再试。';
                            break;
                        case -100:
                            errorMessage = '缺少必要的参数。';
                            break;
                        default:
                            errorMessage = '注册失败，请稍后再试。';
                    }
                    alert(`注册失败: ${errorMessage}`);
                }
            })
            .catch(error => {
                console.error('Error:', error);
                alert('注册过程中发生错误，请稍后再试。');
            });
        }
    });

    loginButton.addEventListener('click', function() {
        window.location.href = '/pages/login/login.html';  // 更改此路径以指向登录页面
    });
});
