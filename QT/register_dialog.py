import requests
from PyQt5 import QtWidgets
from UI.mfregister import Ui_RegisterDialog

class RegisterDialog(QtWidgets.QDialog):
    def __init__(self, main_dialog):
        super().__init__()
        self.ui = Ui_RegisterDialog()
        self.ui.setupUi(self)
        self.setWindowTitle("注册窗口")
        self.main_dialog = main_dialog

        self.ui.register_2.clicked.connect(self.register)

    def register(self):
        # 注册过程，这里添加实际的注册逻辑
        username = self.ui.lineEdit.text()
        password = self.ui.lineEdit_2.text()
        confirm_password = self.ui.lineEdit_3.text()

        # 检查密码是否匹配
        if password != confirm_password:
            QtWidgets.QMessageBox.warning(self, "注册失败", "密码不匹配，请重试。")
            return

        # 构建请求数据
        url = 'http://127.0.0.1:5000/admin/register'
        data = {
            'userName': username,
            'password': password
        }

        try:
            # 发送注册请求
            response = requests.post(url, json=data)
            response_data = response.json()

            # 根据接口返回的code处理不同情况
            if response_data['code'] == 0:
                self.show_registration_result("注册成功！")
                self.close()  # 关闭当前窗口
                self.main_dialog.show()  # 显示主对话框
            elif response_data['code'] == -1:
                QtWidgets.QMessageBox.warning(self, "注册失败", "用户名已存在，请尝试其他用户名。")
            elif response_data['code'] == -98 or response_data['code'] == -99:
                QtWidgets.QMessageBox.warning(self, "注册失败", "数据库错误，请稍后再试。")
            elif response_data['code'] == -100:
                QtWidgets.QMessageBox.warning(self, "注册失败", "缺少必要的参数，请检查输入。")
            else:
                QtWidgets.QMessageBox.warning(self, "注册失败", "未知错误，请联系管理员。")

        except requests.exceptions.RequestException as e:
            QtWidgets.QMessageBox.warning(self, "注册失败", f"请求异常: {e}")
        except Exception as e:
            QtWidgets.QMessageBox.warning(self, "注册失败", f"发生异常: {e}")

    def show_registration_result(self, message):
        QtWidgets.QMessageBox.information(self, "注册结果", message)
