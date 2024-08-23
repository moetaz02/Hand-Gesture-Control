# Hand Gesture Control with MediaPipe and OpenCV

This project enables you to control your computer's mouse and adjust the system volume using hand gestures detected via your webcam. The project uses MediaPipe for hand tracking and OpenCV for video processing.
## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Modules Overview](#modules-overview)


## Features

- **Hand Gesture Detection**: Detects various hand gestures such as finger pinches to control mouse actions and adjust volume.
- **Mouse Control**: Move the cursor, click, and drag using hand gestures.
- **Volume Control**: Adjust the system volume by changing the distance between your thumb and index finger.

## Installation
### Step-by-Step Guide

1. **Clone the repository**:
   ```bash
   git clone https://github.com/ton-utilisateur/Hand-Gesture-Control.git
   cd Hand-Gesture-Control
2. **install the following Python packages** 
    ```bash
   pip install mediapipe opencv-python autopy numpy pycaw comtypes

## Usage 
1. **Run the Mouse Control Script:**:
   ```bash
   python MouseControl.py
 - **Control Mouse :** Move your hand to control the cursor position. Pinch your thumb and index finger to click.
2. **Run the Volume Control Script:**:
   ```bash
   python VolumeControl.py
 - **Control Volume :** Adjust the system volume by varying the distance between your thumb and index finger.
3. **Exit the Application :**:

 - **Press the 'q' key to stop the script.** 
## How It Works
1. **Hand Detection :**
- **HandTrackingModule.py :** Utilizes MediaPipe to detect and track hand landmarks. The handDetector class provides methods to find hand positions, detect which fingers are up, and calculate distances between points.
 
2. **Mouse Control :**

 - **MouseControl.py :** Captures video from the webcam, processes hand gestures to move the mouse cursor, and performs clicks. The position of the index finger is mapped to screen coordinates.
3. **Volume Control :**
 - **VolumeControl.py :** Uses hand gestures to adjust the system volume. Measures the distance between the thumb and index finger and translates it into volume changes using the pycaw library.

## Files Overview
 - **HandTrackingModule.py :** Contains the handDetector class for hand tracking and gesture recognition.
 - **MouseControl.py :** Script for controlling the mouse using hand gestures.
- **VolumeControl.py :** Script for adjusting system volume based on hand gestures.