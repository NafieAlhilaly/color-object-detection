import pytest
from ..main import create_test_image, detect_colors, generate_report

def test_color_detection():
    """Test basic color detection functionality"""
    # ِArrange
    test_image = create_test_image()
    expected_colors = {"Red", "Green", "Blue", "Yellow"}
    
    # Act
    detected = detect_colors(test_image)
    detected_colors = set(detected.keys())

    
    # Assert
    assert detected_colors == expected_colors
