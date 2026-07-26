# Face Mood Detection Using Artificial Intelligence

## Overview
Face Mood Detection Using Artificial Intelligence is a web-based application that detects human emotions using Artificial Intelligence, Computer Vision, and Deep Learning.

## Features
- Secure Login and Signup using Firebase Authentication
- User Profile Creation
- Browser Camera, Webcam, and Image Upload
- Face Detection using OpenCV
- Emotion Prediction using CNN
- Confidence Score Display
- AI-generated Emotional Insights

## Technologies Used
- Python
- Streamlit
- OpenCV
- TensorFlow/Keras
- Firebase Authentication
- Firebase Realtime Database
- NumPy
- Pillow (PIL)

## How to Run
1. Install the required libraries:
   ```
   pip install -r requirements.txt
   ```
2. Run the application:
   ```
   streamlit run login.py
   ```

## Project Structure
- `login.py` – Login and Signup
- `pages/profile.py` – User Profile Creation
- `pages/app.py` – Face Mood Detection Application
- `emotion_model.h5` – Trained CNN Model
