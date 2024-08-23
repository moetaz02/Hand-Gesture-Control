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
- ## Fonctionnalités

- **Contrôle de la souris** : Déplace le curseur et effectue des clics en utilisant les gestes de la main.
- **Contrôle du volume** : Ajuste le volume du système en fonction des gestes de la main.

## Code Explicatif

### `HandTrackingModule.py`
Ce fichier contient la classe handDetector qui encapsule la détection des mains et la gestion des gestes.

- **Initialisation (__init__) :** Configure les paramètres du modèle de détection des mains de MediaPipe, y compris le nombre maximum de mains à détecter et les seuils de détection et de suivi.

- **Méthode findHands :**  Convertit l'image en RGB et traite l'image pour détecter les mains. Dessine les connexions entre les points de repère des mains si l'option draw est activée.

- **Méthode findPosition :** Extrait les coordonnées des points de repère de la main et dessine un cadre autour de la main détectée. Cette méthode retourne les positions des points de repère et les coordonnées du cadre de délimitation.

- **Méthode fingersUp :** Détermine quels doigts sont levés en comparant les positions des points de repère. Retourne une liste d'indicateurs pour chaque doigt.

- **Méthode findDistance :** Calcule la distance entre deux points de repère (par exemple, les extrémités des doigts) et dessine cette distance sur l'image.
### `MouseControl.py`
Ce script utilise la classe handDetector pour contrôler le curseur de la souris en fonction des gestes de la main.

- **Initialisation de la Webcam :** Configure la caméra pour capturer des images en temps réel.

- **Boucle Principale :**  Lit les images de la webcam, détecte les mains et les gestes, et déplace le curseur en fonction de la position des doigts. Si les deux premiers doigts sont levés et rapprochés, un clic de souris est simulé.

- **Calcul de la Position du Curseur :** Interpole les coordonnées de la main détectée pour les mapper sur la taille de l'écran et déplace le curseur en conséquence.

### `VolumeControl.py`
Ce script ajuste le volume du système en utilisant les gestes de la main.

- **Initialisation de la Webcam et de l'API de Volume :** Configure la caméra pour capturer des images en temps réel.

- **Boucle Principale :**  Lit les images de la webcam, détecte les mains, et ajuste le volume en fonction de la distance entre les doigts. Plus les doigts sont proches, plus le volume est élevé.

- **Calcul du Volume :** Utilise une interpolation pour convertir la distance entre les doigts en niveau de volume. Met à jour le volume du système en fonction de la valeur calculée
