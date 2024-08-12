import datetime

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QDialog, QMessageBox
import requests
import winsound
from UI.mflogin import Ui_LoginDialog
from Video import Video


class LoginDialog(QDialog):
    def __init__(self, parent=None):
        super(LoginDialog, self).__init__(parent)
        self.ui = Ui_LoginDialog()
        self.ui.setupUi(self)

        # 初始化视频路径和模型路径
        self.video_path = ''
        self.model_path = 'asset/best.pt'  # 设置模型路径，这里使用了固定的路径
        self.video = Video(self.video_path, self.model_path)
        self.video.frameChanged.connect(self.display_frame)
        self.video.statsChanged.connect(self.update_stats)
        self.record_flag = False
        self.monitorID = None

        # 和后端交互，获取下拉框内容并设置视频路径
        try:
            monitors = self.get_all_monitors()
            if monitors:
                self.populate_combobox(monitors)


        except Exception as e:
            QMessageBox.warning(self, '错误', f'获取监控器信息失败: {e}')

        # 初始闹钟控制
        self.alarm_active = False
        self.enable_alarm = True
        self.ui.teralarm.clicked.connect(self.alarm_disable)

        # 连接下拉框的选择改变信号到槽函数
        self.ui.comboBox.currentIndexChanged.connect(self.on_combobox_index_changed)

    def populate_combobox(self, monitors):
        self.ui.comboBox.clear()
        for monitor in monitors:
            monitor_name = monitor.get('monitorName', '')
            self.ui.comboBox.addItem(monitor_name, monitor)  # 存储整个监控器信息，方便后续使用

    # 变换视频路径
    def update_video(self):
        self.video.set_video_path(self.video_path)
        self.enable_alarm = True

    # 获取监控器信息
    def get_all_monitors(self):
        url = 'http://127.0.0.1:5000/monitor/getAll'
        try:
            response = requests.get(url)
            response_data = response.json()

            if response_data['code'] == 0:
                return response_data['data']
            elif response_data['code'] == -98:
                raise Exception('数据错误')
            elif response_data['code'] == -100:
                raise Exception('参数不完整')
            else:
                raise Exception('未知错误')

        except requests.RequestException as e:
            raise Exception(f'请求异常: {e}')
        except Exception as e:
            raise Exception(f'获取监控器信息失败: {e}')

    # 下拉框选择触发
    def on_combobox_index_changed(self, index):

        selected_monitor = self.ui.comboBox.itemData(index)
        self.monitorID = selected_monitor['monitorID']
        if selected_monitor:

            monitor_id = selected_monitor.get('monitorID', '')
            print(monitor_id)

            current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(current_time)
            self.video_path = selected_monitor.get('source', '')
            print(self.video_path)
            self.update_video()

            if not self.record_flag:
                self.record_flag = True
                return
            else:
                # 构造请求数据
                data = {
                    'monitorID': monitor_id,
                    'timestamp': current_time,
                }

                url = 'http://127.0.0.1:5000/record/addRecord'  # 替换为实际的接口地址

                try:
                    response = requests.post(url, json=data)
                    response_data = response.json()

                    if response_data['code'] == 0:
                        QMessageBox.information(self, '成功', '记录上传成功！')
                    elif response_data['code'] == -98:
                        QMessageBox.warning(self, '错误', '数据错误')
                    elif response_data['code'] == -100:
                        QMessageBox.warning(self, '错误', '参数不完整')
                    else:
                        QMessageBox.warning(self, '错误', '未知错误')

                except requests.RequestException as e:
                    QMessageBox.warning(self, '错误', f'请求异常: {e}')
                except Exception as e:
                    QMessageBox.warning(self, '错误', f'记录上传失败: {e}')

    def display_frame(self, frame):
        pixmap = QPixmap.fromImage(frame)
        self.ui.Video.setPixmap(pixmap.scaled(self.ui.Video.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))

    def update_stats(self, stats):
        # 打印接收到的统计结果用于调试
        print(f"接收到的统计结果: {stats}")

        # 更新界面上的标签
        self.ui.safetynum.setText(f"{stats['安全穿戴人数']}")
        self.ui.nonhelnum.setText(f"{stats['未佩戴头盔人数']}")
        self.ui.nonerelnum.setText(f"{stats['未穿反光服人数']}")
        self.ui.nonebothnum.setText(f"{stats['未佩戴头盔、未穿反光服人数']}")

        # 检查是否需要报警
        if stats['未穿反光服人数'] > 0 or stats['未佩戴头盔、未穿反光服人数'] > 0 or stats['未佩戴头盔人数'] > 0:
            if not self.alarm_active and self.enable_alarm:
                self.start_alarm()
        else:
            self.enable_alarm = True
            if self.alarm_active:
                self.stop_alarm()

        # 界面刷新
        self.ui.safetynum.repaint()
        self.ui.nonhelnum.repaint()
        self.ui.nonerelnum.repaint()
        self.ui.nonebothnum.repaint()

    def start_alarm(self):
        self.alarm_active = True
        winsound.PlaySound("asset/alarm.wav", winsound.SND_ASYNC | winsound.SND_LOOP)  # Replace with your alarm sound path
        current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(current_time)
        data = {
            'monitorID': self.monitorID,
            'timestamp': current_time,
        }

        url = 'http://127.0.0.1:5000/alert/addOne'  # 替换为实际的接口地址

        try:
            response = requests.post(url, json=data)
            response_data = response.json()
        except requests.RequestException as e:
            QMessageBox.warning(self, '错误', f'请求异常: {e}')
        except Exception as e:
            QMessageBox.warning(self, '错误', f'记录上传失败: {e}')

    def stop_alarm(self):
        self.alarm_active = False
        winsound.PlaySound(None, winsound.SND_PURGE)

    def alarm_disable(self):
        self.enable_alarm = False
        QMessageBox.information(self, "提示", "报警已停止")
        self.stop_alarm()

    def close(self):
        del self.video
        self.stop_alarm()
