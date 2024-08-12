from ultralytics import YOLO

# 加载YOLOv8模型
model = YOLO('yolov8n.pt')  # 使用YOLOv8 nano模型作为基准模型

# 训练模型
model.train(data='../dataset/data.yaml', epochs=200, imgsz=640,batch=16)

# 验证模型
metrics = model.val(data='../dataset/data.yaml')




