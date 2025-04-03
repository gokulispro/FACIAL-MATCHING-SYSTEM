# Facial Matching and Best Image Selection System

## Project Overview
This project is a **Real-Time Facial Matching and Best Image Selection System** developed as part of an internship project at **Sri Sairam Techno Incubator Foundation**. It involves capturing images from multiple cameras, grouping images by individual persons, selecting the best image for each person, and matching the best images across different camera locations.

## Features
- **Real-time Image Capture**: Captures burst images when a person enters the frame.
- **Face Detection & Grouping**: Groups images of the same person.
- **Best Image Selection**: Chooses the best quality image for each person.
- **Facial Matching Across Locations**: Matches the best-selected images with images captured at another camera or location.
- **Multi-Camera Support**: Scalable to multiple cameras at different locations.

---

## Project Structure
```
|── Source Code/ 
|   ├── main.py                 # Main script to initialize and run the system
|   ├── camera_capture.py       # Handles image capture from cameras
|   ├── image_processing.py     # Processes images for face recognition
├── requirements.txt        # Dependencies and required libraries
└── README.md               # Project documentation
```

---

## Installation
### Prerequisites
Ensure you have the following installed:
- Python 3.7+
- OpenCV
- dlib
- face_recognition
- NumPy
- Two connectable cameras


### Setup Instructions
1. Clone the repository:
   ```sh
   git clone https://github.com/your-repo/facial-matching-system.git
   cd facial-matching-system
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
 3.Download and set up the `shape_predictor_68_face_landmarks.dat` model:
   - Download from: [dlib.net](http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2)
   - Extract using:
     ```sh
     bzip2 -d shape_predictor_68_face_landmarks.dat.bz2
     ```
   - Place the extracted `.dat` file inside the `models/` folder.
   
4. Run the system:
   ```sh
   python main.py
   ```

---

## Code Breakdown
### `main.py`
- Imports necessary modules.
- Initializes cameras and image processing modules.
- Runs the facial matching pipeline in real time.

### `camera_capture.py`
- Captures images from multiple cameras.
- Uses burst shots when motion is detected.
- Passes images to the processing module.

### `image_processing.py`
- Detects and recognizes faces using `face_recognition` and `dlib`.
- Groups images based on unique facial features.
- Selects the best image for each person based on clarity and face position.
- Matches best images with previously stored faces from another camera location.

---

## Usage
1. **Start the System**: Run `main.py` to begin capturing images.
2. **Image Processing**: The system detects and processes faces in real time.
3. **Facial Matching**: The best-selected images are matched across different locations.
4. **Display Matches**: Matched results are displayed with relevant information.

---

## Future Enhancements
- **Increase Accuracy**: Implement deep learning-based face recognition.
- **Scalability**: Add support for more cameras and cloud-based processing.
- **Database Storage**: Store images and metadata in a database for historical tracking.

---

## Contributors
- **Gali Yaswanth Sai** (Intern, Sri Sairam Techno Incubator Foundation)
- **GokulKrishnan Saravanan** (Intern, Sri Sairam Techno Incubator Foundation )  https://github.com/gokulispro

---

## License
This project is licensed under the MIT License.




   
