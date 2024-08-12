import cv2
from PyQt5.QtCore import QObject, pyqtSignal, QTimer
from PyQt5.QtGui import QImage
from ultralytics import YOLO


class Video(QObject):
    frameChanged = pyqtSignal(QImage)  # 用于发送处理后的帧
    statsChanged = pyqtSignal(dict)  # 用于发送统计结果

    def __init__(self, video_path, model_path, parent=None):
        super(Video, self).__init__(parent)
        self.video_path = video_path
        self.model_path = model_path
        self.cap = cv2.VideoCapture(video_path)  # 视频文件路径
        self.model = YOLO(model_path)  # 初始化 YOLO 模型
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        # 初始时不启动定时器
        self.timer.stop()

    def update_frame(self):
        ret, frame = self.cap.read()
        if ret:
            # 执行检测
            results = self.model(frame)

            # 初始化统计计数
            counts = {'未穿反光服人数': 0, '未佩戴头盔、未穿反光服人数': 0, '安全穿戴人数': 0, '未佩戴头盔人数': 0}

            # 遍历检测结果
            for result in results:
                for box in result.boxes:
                    cls = self.model.names[int(box.cls)]
                    if cls == 'hat':
                        counts['未穿反光服人数'] += 1
                    elif cls == 'nothing':
                        counts['未佩戴头盔、未穿反光服人数'] += 1
                    elif cls == 'vest_hat':
                        counts['安全穿戴人数'] += 1
                    elif cls == 'vest':
                        counts['未佩戴头盔人数'] += 1

            # 打印统计结果用于调试
            print(f"统计结果: {counts}")

            # 发送统计结果
            self.statsChanged.emit(counts)

            # 在帧上绘制检测结果
            annotated_frame = results[0].plot()  # 使用 plot 方法获取带注释的帧

            # 将 BGR 转换为 RGB
            frame = cv2.cvtColor(annotated_frame, cv2.COLOR_BGR2RGB)

            # 转换为 QImage
            h, w, ch = frame.shape
            bytesPerLine = ch * w
            convertToQtFormat = QImage(frame.data, w, h, bytesPerLine, QImage.Format_RGB888)
            self.frameChanged.emit(convertToQtFormat)
        else:
            self.timer.stop()
            self.cap.release()

    def set_video_path(self, video_path):
        # 释放当前视频捕捉对象

        if self.cap.isOpened():
            self.cap.release()

        # 更新视频路径
        self.video_path = video_path
        self.cap = cv2.VideoCapture(video_path)

        # 启动定时器
        self.timer.start(30)

    def stopTimer(self):
        self.timer.stop()
