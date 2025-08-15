# 🎨 Real-Time Color Detector using Python & OpenCV

This project is a **real-time color detection tool** that uses a webcam or an image to identify the color of any object you point to.  
It also displays **RGB values**, the closest **color name**, and can show **histogram/graph analysis** of the frame.

---

## 📌 Features

- **Real-time color detection** using webcam feed
- **Image analysis mode** for static color detection
- **RGB value display** with precise color coordinates
- **Color name identification** using comprehensive color database
- **Interactive click-to-detect** functionality
- **Histogram analysis** showing color distribution
- **Hue distribution graphs** for advanced color analysis
- **Dual mode operation** (Image/Video switching)
- **Cross-platform compatibility** (Windows, macOS, Linux)

---

## 🛠️ Requirements

Make sure you have **Python 3.7+** installed.

### 1. Install Python  
[Download Python](https://www.python.org/downloads/)

### 2. Install Required Packages
Open a terminal or command prompt and run:
```bash
pip install opencv-python numpy matplotlib
```

### 3. Optional Dependencies
`tkinter` is included by default in most Python installations, but if missing:

**Windows/macOS:** Pre-installed with Python  
**Linux (Debian/Ubuntu):**
```bash
sudo apt-get install python3-tk
```

---

## 📂 Project Structure

```
color-detector/
├── color_detector.py        # Main application script
├── rgbToName.txt            # RGB-to-color name mapping database
├── sample_images/           # Test images directory
│   ├── red.jpg             # Sample red object
│   ├── blue.jpg            # Sample blue object
│   └── multi_color.jpg     # Multi-colored test image
├── requirements.txt         # Python dependencies
├── README.md               # This documentation
└── LICENSE                 # License file
```

### Color Database Format
**rgbToName.txt** should contain lines in the format:
```
255,0,0:Red
0,255,0:Green
0,0,255:Blue
128,0,128:Purple
255,165,0:Orange
255,255,0:Yellow
0,255,255:Cyan
255,192,203:Pink
```

---

## ⚡ Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/color-detector.git
cd color-detector
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Application
```bash
python color_detector.py
```

---

## 🎮 Controls & Usage

### Keyboard Controls
| Key | Action |
|-----|--------|
| **G** | Show hue graph & RGB histogram |
| **I** | Switch to Image Mode (select file) |
| **V** | Switch to Video Mode (webcam) |
| **S** | Save current frame |
| **H** | Show/Hide help overlay |
| **Space** | Pause/Resume video |
| **ESC** | Exit application |

### Mouse Controls
- **Move cursor** → Real-time color detection under mouse pointer
- **Left click** → Capture and display color information
- **Right click** → Show detailed color analysis popup

### Interface Elements
- **Color preview box** → Shows detected color sample
- **RGB values** → Displays exact Red, Green, Blue values (0-255)
- **Color name** → Shows closest matching color name
- **Coordinates** → Mouse position (x, y)
- **Mode indicator** → Current operation mode (Image/Video)

---

## 📊 Advanced Features

### Histogram Analysis
Press **G** to display:
- **RGB Histogram**: Shows distribution of Red, Green, and Blue channels
- **Hue Distribution**: Displays color hue spread across the image
- **Color Statistics**: Mean, median, and standard deviation values

### Color Accuracy
The tool uses **Euclidean distance** calculation to find the closest matching color name from the database, ensuring high accuracy in color identification.

### Supported Image Formats
- JPEG (.jpg, .jpeg)
- PNG (.png)
- BMP (.bmp)
- TIFF (.tiff, .tif)
- WebP (.webp)

---

## 🔧 Configuration

### Customizing Color Database
Edit `rgbToName.txt` to add custom colors:
```
R,G,B:ColorName
```

### Camera Settings
Modify these variables in `color_detector.py`:
```python
CAMERA_WIDTH = 640    # Camera resolution width
CAMERA_HEIGHT = 480   # Camera resolution height
FPS = 30             # Frames per second
```

---

## 🚀 Performance Tips

- **Good lighting** improves color detection accuracy
- **Stable camera** reduces detection fluctuations  
- **High contrast backgrounds** help with object identification
- **Close-up detection** provides more precise results
- **Update color database** for specialized color needs

---

## 🔍 Troubleshooting

### Common Issues

**Camera not detected:**
```bash
# Check available cameras
python -c "import cv2; print([i for i in range(10) if cv2.VideoCapture(i).read()[0]])"
```

**Low detection accuracy:**
- Ensure good lighting conditions
- Check camera focus and resolution
- Update or expand the color database
- Clean camera lens

**Installation issues:**
```bash
# Upgrade pip
pip install --upgrade pip

# Install with specific versions
pip install opencv-python==4.8.1.78 numpy==1.24.3 matplotlib==3.7.1
```

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

### Development Setup
```bash
git clone https://github.com/yourusername/color-detector.git
cd color-detector
pip install -r requirements.txt
```

### Adding Features
- Fork the repository
- Create a feature branch (`git checkout -b feature/new-feature`)
- Commit changes (`git commit -am 'Add new feature'`)
- Push to branch (`git push origin feature/new-feature`)
- Create a Pull Request

---



## ⚠️ Notes & Limitations

- **Webcam access** must be granted for live detection mode
- **Color accuracy** depends on lighting conditions and camera quality
- **Database completeness** affects color name recognition
- **Performance** may vary on older hardware
- **Resolution** impacts detection precision

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- **OpenCV** community for computer vision tools
- **NumPy** for numerical computing capabilities  
- **Matplotlib** for visualization features
- Color theory references and RGB databases

---

## 📞 Support

For questions, issues, or suggestions:
- **GitHub Issues**: [Report a bug](https://github.com/techoflassh/color-detector/issues)
- **Email**: coderakshit11@gmail.com
---


**⭐ If this project helped you, please give it a star on GitHub!**
