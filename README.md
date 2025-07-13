These repo contains two projects related to color detection using OpenCV and object detection using HuskyLens.


# Projects
## 1. [OpenCV Color Detection](./opencv/README.md)
   - This project uses OpenCV to detect colors in images and includes a Dockerfile for environment setup.
     ### Setup Instructions
   - Ensure you have Docker installed.
   - Build the Docker image using:
     ```bash
     docker build -t opencv-color-detection .
     ```
   - Run the container:
     ```bash
     docker run --rm opencv-color-detection
     ```
    
        ```console

        =================================================== test session starts ====================================================
        platform win32 -- Python 3.11.2, pytest-8.4.1, pluggy-1.6.0 -- C:\Users\nafaa\projects\sm-tasks\color-recognition\venv\Scripts\python.exe
        cachedir: .pytest_cache
        rootdir: C:\Users\nafaa\projects\sm-tasks\color-recognition
        collected 1 item

        opencv/tests.py::test_color_detection PASSED                                                                          [100%]

        ==================================================== 1 passed in 0.16s =====================================================
        
        ```

## 2. [HuskyLens Object Detection](./huskylens/README.md)
   - This project uses the HuskyLens AI camera to detect objects and print their IDs.
        ### Setup Instructions
    - Ensure you have the HuskyLens library installed in your Arduino IDE.
    - Upload the `src.ino` sketch to your HuskyLens device.
    - Open the Serial Monitor to view detected object IDs.
    
        ```console
        HuskyLens ready in Object Recognition mode
        Object ID: 1, X: 100, Y: 150, Width: 50, Height: 50
        Object ID: 2, X: 200, Y: 250, Width: 60, Height: 60
        ```
