from ultralytics import YOLO
import time

model = YOLO("yolov8x.pt")

start = time.time()

results = model.predict(
    source="images/sample.jpg",
    save=True,
    project="results"
)

end = time.time()

print("Detected Objects:", len(results[0].boxes))
print("Inference Time:", round(end - start, 3), "seconds")
