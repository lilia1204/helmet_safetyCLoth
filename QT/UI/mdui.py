# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mdui.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1320, 817)
        Dialog.setStyleSheet("")
        self.title = QtWidgets.QLabel(Dialog)
        self.title.setGeometry(QtCore.QRect(370, 70, 581, 91))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(24)
        self.title.setFont(font)
        self.title.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.title.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(500, 460, 81, 51))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.confrim_2 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.confrim_2.setFont(font)
        self.confrim_2.setObjectName("confrim_2")
        self.verticalLayout_4.addWidget(self.confrim_2)
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(500, 270, 81, 51))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.username_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.username_2.setFont(font)
        self.username_2.setObjectName("username_2")
        self.verticalLayout_5.addWidget(self.username_2)
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(590, 460, 219, 51))
        self.lineEdit_3.setBaseSize(QtCore.QSize(0, 6))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("background-color: rgba(255, 255, 255, 60);")
        self.lineEdit_3.setText("")
        self.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.Login = QtWidgets.QPushButton(Dialog)
        self.Login.setGeometry(QtCore.QRect(760, 650, 121, 51))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.Login.setFont(font)
        self.Login.setObjectName("Login")
        self.register_2 = QtWidgets.QPushButton(Dialog)
        self.register_2.setGeometry(QtCore.QRect(430, 650, 121, 51))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.register_2.setFont(font)
        self.register_2.setObjectName("register_2")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(500, 360, 81, 51))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.password_2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.password_2.setFont(font)
        self.password_2.setObjectName("password_2")
        self.verticalLayout_6.addWidget(self.password_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(590, 360, 219, 51))
        self.lineEdit_2.setBaseSize(QtCore.QSize(0, 6))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("background-color: rgba(255, 255, 255, 60);")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(590, 270, 219, 51))
        self.lineEdit.setBaseSize(QtCore.QSize(0, 6))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color: rgba(255, 255, 255, 60);")
        self.lineEdit.setText("")
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(390, 180, 531, 381))
        self.label.setStyleSheet("background-color: rgba(197, 197, 197, 60);\n"
"border-radius:15px; ")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(100, 40, 1051, 731))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgba(255, 255, 255, 70);\n"
"border-radius:25px;     ")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(600, 270, 211, 49))
        self.label_3.setStyleSheet("background-color: rgba(255, 255, 255, 60);\n"
"color:grey;    ")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(600, 360, 211, 49))
        self.label_4.setStyleSheet("background-color: rgba(255, 255, 255, 60);\n"
"color:grey;    ")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(600, 460, 211, 49))
        self.label_5.setStyleSheet("background-color: rgba(255, 255, 255, 60);\n"
"color:grey;    ")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.listView = QtWidgets.QListView(Dialog)
        self.listView.setGeometry(QtCore.QRect(0, 0, 1331, 911))
        self.listView.setStyleSheet("background-image: url(\"./background.jpg\");\n"
"object-fit:cover;")
        self.listView.setObjectName("listView")
        self.listView.raise_()
        self.label_2.raise_()
        self.label.raise_()
        self.title.raise_()
        self.verticalLayoutWidget_3.raise_()
        self.verticalLayoutWidget.raise_()
        self.Login.raise_()
        self.register_2.raise_()
        self.verticalLayoutWidget_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.lineEdit_3.raise_()
        self.lineEdit_2.raise_()
        self.lineEdit.raise_()

        self.retranslateUi(Dialog)
        self.register_2.clicked.connect(Dialog.goin_register) # type: ignore
        self.Login.clicked.connect(Dialog.goin_login) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.title.setText(_translate("Dialog", "安全眼——工地防护装备检测系统"))
        self.confrim_2.setText(_translate("Dialog", "确认:"))
        self.username_2.setText(_translate("Dialog", "账号："))
        self.lineEdit_3.setPlaceholderText(_translate("Dialog", "请确认密码"))
        self.Login.setText(_translate("Dialog", "登录"))
        self.register_2.setText(_translate("Dialog", "注册"))
        self.password_2.setText(_translate("Dialog", "密码:"))
        self.lineEdit_2.setPlaceholderText(_translate("Dialog", "请输入密码"))
        self.lineEdit.setPlaceholderText(_translate("Dialog", "请输入账号"))
