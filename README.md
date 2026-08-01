# STOP Sign Detection with OpenCV

## Project Description

This project was developed as part of the **Python and OpenCV Image Processing** assignment.

The objective is to detect **STOP traffic signs** in images using color-based image processing techniques. The algorithm detects the red color of the STOP sign, determines its location, draws a bounding box around the detected object, calculates the center pixel coordinates, and saves the processed image.

An improved version of the algorithm also performs **octagon shape analysis** to reduce false detections.

---

## Features

* Detects STOP signs using HSV color segmentation.
* Applies morphological operations to remove image noise.
* Finds object contours.
* Draws a bounding box around the detected STOP sign.
* Calculates and prints the center pixel coordinates.
* Saves processed images automatically.
* Includes an improved version using octagon shape detection.

---

## Technologies Used

* Python 3.x
* OpenCV
* NumPy

---

## Project Structure

```text
STOP-Sign-Detection/
│
├── README.md
├── requirements.txt
├── stop_detection.py
├── stop_detection_octagon.py
├── stop_sign_dataset/
├── output_color/
├── output_octagon/
└── screenshots/
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/USERNAME/STOP-Sign-Detection.git
```

Install the required libraries:

```bash
pip install -r requirements.txt
```

---

## Usage

Place the image dataset inside the `stop_sign_dataset` folder.

Run the basic color-based detection algorithm:

```bash
python stop_detection.py
```

Or run the improved version with octagon shape analysis:

```bash
python stop_detection_octagon.py
```

The processed images will be saved automatically in the corresponding output folder.

---

## Output

For each detected STOP sign, the program:

* Detects the red traffic sign.
* Draws a green bounding box.
* Marks the center point.
* Prints the center coordinates in the terminal.
* Saves the processed image.

Example terminal output:

```text
image01.jpg --> Center = (356, 214)
image02.jpg --> Center = (481, 179)
```

---

## Dataset

The project uses the provided **stop_sign_dataset** image dataset.

---

## Future Improvements

* Deep learning-based detection (YOLOv8)
* Haar Cascade classifiers
* Faster R-CNN
* SSD object detector
* Real-time webcam support
* ROS integration for autonomous robots

---

## Author

**Ad Soyad:** <Adınızı Yazınız>

**University:** <Üniversiteniz>

**Course:** Python and OpenCV Image Processing

**Year:** 2026
