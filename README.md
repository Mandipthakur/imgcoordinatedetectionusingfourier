# 🌀 Image Coordinate Detection Using Fourier

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.x-critical.svg)](https://opencv.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-3.x-orange.svg)](https://matplotlib.org/)

This project demonstrates how **image contours** can be extracted and **reconstructed using Fourier epicycles**. It provides tools to analyze image shapes and visualize them using **Fourier series-based drawing** techniques.

---

## 📂 Project Structure

.
├── ball3x3.jpg
├── elephant3x3.png
├── polar3x3.jpg
├── tennis3x3.jpg
├── contourdetection.py
├── epycycle_draw.py
├── imgcoordinates.txt

yaml
Copy
Edit

- `contourdetection.py` – Detects image contours and extracts their coordinates.
- `epycycle_draw.py` – Visualizes contours using Fourier epicycles.
- `imgcoordinates.txt` – Stores extracted `(x, y)` coordinates.
- `*.jpg/*.png` – Sample images for analysis and reconstruction.

---

## 📸 Example Output

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/f1/Fourier_series_square_wave_circles_animation.gif/640px-Fourier_series_square_wave_circles_animation.gif" width="500">

> *Above: Example of epicycle-based shape reconstruction using Fourier series.*

---

## 🛠 How It Works

### 🔍 Step 1: Contour Detection

Run `contourdetection.py` with your image file:

```bash
python contourdetection.py <input_image>
Example:

bash
Copy
Edit
python contourdetection.py ball3x3.jpg
This appends the main contour's (x, y) points to imgcoordinates.txt.

📈 Step 2: Fourier Epicycle Visualization
Reconstruct the contour using Fourier rotating vectors:

bash
Copy
Edit
python epycycle_draw.py
This reads the contour points from imgcoordinates.txt and animates the shape using Fourier series.

📦 Requirements
Make sure the following libraries are installed:

bash
Copy
Edit
pip install opencv-python numpy matplotlib
📄 File Descriptions
File	Description
contourdetection.py	Extracts contour coordinates from the input image
epycycle_draw.py	Reads coordinates and visualizes them using Fourier series
imgcoordinates.txt	Stores (x, y) contour points for Fourier input
*.jpg/png	Sample input images for demonstration

🔁 Example Workflow
Detect contours:

bash
Copy
Edit
python contourdetection.py tennis3x3.jpg
Visualize using epicycles:

bash
Copy
Edit
python epycycle_draw.py
🎓 License
This project is licensed under the MIT License.
For educational and research purposes only.

👤 Author
Mandip Thakur
