from ultralytics import YOLO

model = YOLO("yolov8x.pt")

model.predict(
    source="images/sample.jpg",
    save=True,
    project="results"
)

print("Done")