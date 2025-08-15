🎨 Real-Time Color Detector using Python & OpenCV

This project is a real-time color detection tool that uses a webcam or an image to identify the color of any object you point to. It also displays RGB values, the closest color name, and can show histogram/graph analysis of the frame.

📌 Features

Detects color name and RGB values in real time using a webcam.

Works with both images and live video.

Can capture text color from clicked position.

Histogram and hue distribution graph generation.

Supports switching between image mode and video mode.

🛠️ Requirements

Make sure you have Python 3.7+ installed.

1. Install Python

Download from: https://www.python.org/downloads/

2. Install Required Packages

Open a terminal or command prompt and run:

pip install opencv-python numpy matplotlib


tkinter is included by default in most Python installations, but if missing:

Windows/macOS: It comes pre-installed.

Linux (Debian/Ubuntu):

sudo apt-get install python3-tk

📂 Project Structure
color-detector/
│── color_detector.py        # Main Python script
│── rgbToName.txt            # RGB-to-color name mapping file
│── red.jpg                  # Sample image for initial testing
│── README.md                # Documentation


▶️ How to Run

Clone or download the repository

git clone https://github.com/yourusername/color-detector.git
cd color-detector


Ensure the mapping file exists
Make sure rgbToName.txt is present in the same directory as the Python script.

Run the program

python color_detector.py

🎮 Controls

Mouse → Move cursor over object to detect its color.

G → Show hue graph & RGB histogram.

I → Switch to Image Mode (select an image file).

V → Switch to Video Mode (webcam).

Space / ESC → Exit the program.

⚠️ Notes

Webcam access must be allowed for live mode.

The accuracy of color names depends on the rgbToName.txt file.

If your webcam resolution is low, detection accuracy might decrease.

📜 License

This project is free to use for learning and personal projects.