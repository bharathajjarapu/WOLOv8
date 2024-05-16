# YOLOv8 API WebKit 🤖

YOLOv8 project! Whether you're a coding ninja 💻 or just getting started, this repo is your ticket to the world of object detection, segmentation, classification, and pose estimation. Let's dive in! 🌊

## Features 🚀

- 🎯 Object Detection: Spot objects like a hawk in images, videos, YouTube, and RTSP streams.
- 🎨 Object Segmentation: Separate objects from their backgrounds with surgical precision.
- 📚 Object Classification: Identify objects and label them like a pro.
- 🕺 Pose Estimation: Detect and track human poses in real-time, perfect for those TikTok dance challenges.

## Installation 💿

1. Clone this repo to your local machine.
2. Install the required dependencies by running:

```
pip install -r requirements.txt
```

## Usage 🚀

### Object Detection 🔍

```
python app.py
```

### Object Segmentation 🖼️

```
python app.py --weights yolov8s-seg.pt
```

### Object Classification 🏷️

```
python app.py --weights yolov8s-cls.pt
```

### Pose Estimation 🕺

```
python app.py --weights yolov8s-pose.pt
```

### CPU Mode 💻

If your GPU is taking a break, run the app on your CPU:

```
python app.py --device cpu
```

## License ⚖️

This project is licensed under the MIT License. Feel free to use, modify, and distribute it as you please.
