# mainframe.py
import requests
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QMessageBox

from UI.mdui import Ui_Dialog
from register_dialog import RegisterDialog
from login_dialog import LoginDialog


class MainDialog(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainDialog, self).__init__()
        self.setup_ui()
        self.loginDialog = None  # 初始化LoginDialog为None

    def setup_ui(self):
        self.setWindowTitle("Main Dialog")
        self.setGeometry(100, 100, 800, 600)
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(0, 0, 800, 600))

        self.pixmap = QtGui.QPixmap("asset/background.jpg")
        self.label.setPixmap(self.pixmap.scaled(self.size(), aspectRatioMode=QtCore.Qt.IgnoreAspectRatio,
                                                transformMode=QtCore.Qt.SmoothTransformation))
        self.label.setScaledContents(True)

        self.resizeEvent = self.on_resize
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # 绑定槽函数
        self.ui.register_2.clicked.connect(self.goin_register)
        self.ui.Login.clicked.connect(self.goin_login)

    def on_resize(self, event):
        self.label.setGeometry(0, 0, self.width(), self.height())
        self.label.setPixmap(self.pixmap.scaled(self.size(), aspectRatioMode=QtCore.Qt.IgnoreAspectRatio,
                                                transformMode=QtCore.Qt.SmoothTransformation))
        super(MainDialog, self).resizeEvent(event)

    def goin_register(self):
        self.registerDialog = RegisterDialog(self)
        self.registerDialog.show()
        self.close()

    def goin_login(self):
        username = self.ui.lineEdit.text()  # 获取用户名
        password = self.ui.lineEdit_2.text()  # 获取密码
        confirm_password = self.ui.lineEdit_3.text()  # 获取确认密码

        # 检查两次输入的密码是否一致
        if password != confirm_password:
            QMessageBox.warning(self, '错误', '两次输入的密码不一致，请重新输入。')
            return

        url = 'http://127.0.0.1:5000/admin/login'  # 本地服务器地址
        data = {
            'userName': username,
            'password': password
        }

        try:
            # 发送POST请求
            response = requests.post(url, json=data)
            response_data = response.json()

            # 处理响应数据
            if response_data['code'] == 0:
                if not self.loginDialog:  # 如果LoginDialog不存在，创建并显示
                    self.loginDialog = LoginDialog(self)
                    self.loginDialog.finished.connect(self.quit_application)  # 连接信号处理
                self.loginDialog.show()
                self.hide()  # 隐藏主对话框
            elif response_data['code'] == -1:
                QMessageBox.warning(self, '错误', '用户不存在。')
            elif response_data['code'] == -2:
                QMessageBox.warning(self, '错误', '密码错误。')
            elif response_data['code'] == -100:
                QMessageBox.warning(self, '错误', f"参数不完整: {response_data['message']}")
            else:
                QMessageBox.warning(self, '错误', f"登录失败: {response_data['message']}")
        except requests.exceptions.RequestException as e:
            QMessageBox.warning(self, '错误', f'请求异常: {e}')
        except Exception as e:
            QMessageBox.warning(self, '错误', f'发生异常: {e}')

    def quit_application(self):
        print(1)
        self.show()
        self.loginDialog.close()
        self.loginDialog = None
