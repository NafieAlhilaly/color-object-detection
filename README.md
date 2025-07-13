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