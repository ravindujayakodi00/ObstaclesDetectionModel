from ultralytics import YOLO

# Load a model
model = YOLO("yolov8n.yaml")

# Use the model
model.train(data="data.yaml", epochs=1)
