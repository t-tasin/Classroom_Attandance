Classroom Attendance Documentation

Project Name: Classroom Attendance

1. Overview

Classroom Attendance is a Python-based application that uses face recognition to monitor the attendance of students in a classroom setting. The application processes the video feed from a camera, detects and identifies the students' faces, and logs their attendance with a timestamp in a CSV file.

2. Modules and Dependencies

Classroom Attendance relies on the following modules and libraries:

- OpenCV (cv2): For video processing, image manipulation, and rendering.
- NumPy (np): For numerical operations.
- face_recognition: For face detection and recognition.
- os: For file and directory operations.
- datetime: For handling date and time.

3. Files and Functions

The project consists of a single file:

- main.py: The main file that processes the video input and logs the attendance.

4. main.py

The main.py file captures video input from a camera, detects and recognizes students' faces, and logs their attendance in a CSV file.

Key features:
- Reads images of students from the 'Member' directory.
- Processes video input from a camera.
- Detects and recognizes students' faces.
- Logs the students' attendance in a CSV file ('WhenYouShowUp.csv') with a timestamp.

5. Usage

To run the Classroom Attendance application, execute the main.py file:

```
python main.py
```

The application will process the video input from the camera and log the attendance of recognized students in the 'WhenYouShowUp.csv' file.

6. Customization

To use the Classroom Attendance application with a different set of students, replace the images in the 'Member' directory with the desired images. Ensure that the new images are clear, frontal pictures of the students' faces, and follow the naming convention of using the student's name as the file name (e.g., 'JohnDoe.jpg').

To adjust the face recognition threshold, modify the value (e.g., 0.50) in the following line:

```python
if faceDistance[matchIndex] < 0.50:
```

A lower value will make the recognition more strict, while a higher value will make it more lenient.

7. License

Classroom Attendance is an open-source project. Feel free to use, modify, and distribute the code as needed, following the terms and conditions of the license.
