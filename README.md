# Eye Detection Using Haar Cascade

## Overview
This project implements a real-time eye detection system using OpenCV and Haar Cascade. It processes frames from a webcam feed to detect eyes and visualizes the detection by drawing circles around the eyes.

## Features
- Real-time eye detection from webcam feed.
- Optimized for performance by resizing frames and processing alternate frames.
- Uses Haar Cascade for robust eye detection.

## Prerequisites
Ensure you have the following installed on your system:
- Python 3.x
- OpenCV library
- A webcam connected to your computer

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/SaiTejaTummoju/Eye-Detection-using-OpenCv.git
   cd Eye-Detection-using-OpenCv
   ```

2. Install the required dependencies:
   ```bash
   pip install opencv-python
   ```

3. Verify that OpenCV's Haar Cascade files are available. These are typically bundled with OpenCV and can be found at:
  added already in my files,check and download it.

## Usage
1. Run the Python script:
   ```bash
   python eyedetection.py
   ```

2. The webcam feed will open in a new window with circles around detected eyes.

3. Press `q` to exit the application.

## Code Explanation
- **Initialization**:
  - The webcam is accessed using `cv2.VideoCapture(0)`.
  - The Haar Cascade classifier is loaded for eye detection.

- **Frame Processing**:
  - Frames are resized to 320x240 for faster processing.
  - Only alternate frames are processed to reduce lag.
  - Detected eyes are visualized with circles drawn on the frame.

- **Real-time Display**:
  - The processed frame is displayed using `cv2.imshow`.
  - The loop exits when the `q` key is pressed.


## Troubleshooting
1. **Cascade Classifier Error**:
   - Ensure the `haarcascade_eye.xml` file exists in the `cv2.data.haarcascades` directory.

2. **Webcam Not Detected**:
   - Verify that your webcam is connected and accessible.

3. **Lag in Detection**:
   - Adjust the frame size or the frame processing frequency by modifying `frame = cv2.resize(frame, (320, 240))` and `if frame_count % 2 == 0`.

## Contributing
Feel free to fork this repository, submit issues, and propose improvements via pull requests.

## Author
Tummoju Sai Teja

