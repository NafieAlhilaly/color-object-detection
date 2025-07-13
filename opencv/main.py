import cv2
import numpy as np

def create_test_image(width=600, height=600):
    """Create a test image with various colored shapes (in memory only)"""
    img = np.full((height, width, 3), 255, dtype=np.uint8)
    
    # Draw colored shapes (BGR format)
    cv2.rectangle(img, (50, 50), (250, 250), (0, 0, 255), -1)  # Red
    cv2.circle(img, (450, 150), 100, (0, 255, 0), -1)           # Green
    cv2.ellipse(img, (300, 400), (100, 50), 0, 0, 360, (255, 0, 0), -1)  # Blue
    cv2.rectangle(img, (400, 400), (550, 550), (0, 255, 255), -1)  # Yellow
    return img

def detect_colors(image, color_ranges=None, min_pixels=500):
    """Detect colors in image and return dictionary of detected colors with pixel counts"""
    if color_ranges is None:
        color_ranges = {
            "Red": ([0, 120, 70], [10, 255, 255]),
            "Green": ([40, 70, 50], [80, 255, 255]),
            "Blue": ([100, 70, 50], [130, 255, 255]),
            "Yellow": ([20, 70, 50], [40, 255, 255])
        }
    
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    detected = {}
    
    for color_name, (lower, upper) in color_ranges.items():
        lower = np.array(lower, dtype=np.uint8)
        upper = np.array(upper, dtype=np.uint8)
        mask = cv2.inRange(hsv, lower, upper)
        pixels = cv2.countNonZero(mask)
        
        if pixels >= min_pixels:
            detected[color_name] = pixels
    
    return detected

def generate_report(detected_colors):
    """Generate text report of detected colors"""
    if not detected_colors:
        return "No colors detected"
    
    report = ["Color Detection Report:"]
    total_pixels = sum(detected_colors.values())
    
    for color, pixels in detected_colors.items():
        percentage = (pixels / total_pixels) * 100 if total_pixels > 0 else 0
        report.append(f"- {color}: {pixels} pixels ({percentage:.1f}%)")
    
    return "\n".join(report)