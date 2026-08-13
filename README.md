# Can YOLO Separate Three Puppies?

A simple experiment comparing YOLOv8n and YOLOv8x on a crowded object detection scenario.

---
![YOLOv8x](comparison/ult.jpg

> YOLOv8n detected three puppies as one object, while YOLOv8x successfully separated all three puppies.
## Background

The test image contains three puppies positioned very close to each other.

The objective was to investigate whether a lightweight YOLO model can correctly distinguish adjacent objects and compare the result with a larger model.

---

## First Attempt: YOLOv8n

### Model

YOLOv8n

### Expected Result

- 3 puppies
- 3 detections

### Actual Result

- 3 puppies
- 1 detection

YOLOv8n merged all three puppies into a single object.

### Detection Result

comparison/yolov8n_result.jpg

---

## Why Did This Happen?

Possible reasons:

- The puppies are positioned very close together
- Bounding boxes overlap significantly
- YOLOv8n prioritizes speed over detailed scene understanding
- The model capacity may be insufficient for crowded object separation

---

## Second Attempt: YOLOv8x

### Model

YOLOv8x

### Expected Result

- 3 puppies
- 3 detections

### Actual Result

- Puppy 1 detected
- Puppy 2 detected
- Puppy 3 detected

The larger model successfully separated all puppies into individual detections.

### Detection Result

comparison/yolov8x_result.jpg

---

## Before vs After

| Model | Detection Result |
|---------|---------|
| YOLOv8n | 1 dog |
| YOLOv8x | 3 dogs |

---

## Key Takeaway

This experiment shows that model size can significantly affect object separation performance.

YOLOv8n is lightweight and fast, but struggled when objects were densely packed together.

YOLOv8x required more computation but successfully distinguished adjacent objects that YOLOv8n merged into a single detection.

---

## Benchmark

| Model | Dogs Detected | Inference Time |
|---------|---------|---------|
| YOLOv8n | 1 | TBD |
| YOLOv8s | TBD | TBD |
| YOLOv8m | TBD | TBD |
| YOLOv8l | TBD | TBD |
| YOLOv8x | 3 | TBD |

---

## Future Work

- Compare YOLOv8n, YOLOv8s, YOLOv8m, YOLOv8l, and YOLOv8x
- Measure inference speed
- Measure GPU memory usage
- Compare detection accuracy
- Test crowded real-world photographs
- Evaluate performance on street scenes containing multiple objects

---

## Repository Structure

```text
YOLO-Object-Recognition-Test
│
├── images
│   └── sample.jpg
│
├── comparison
│   ├── yolov8n_result.jpg
│   └── yolov8x_result.jpg
│
├── src
│   └── image_detection.py
│
└── README.md
```
