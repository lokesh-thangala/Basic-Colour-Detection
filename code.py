import cv2
import numpy as np

def detect_color(rgb):
    if rgb[0] > 200 and rgb[1] < 50 and rgb[2] < 50:
        return "Red"
    elif rgb[0] < 50 and rgb[1] > 200 and rgb[2] < 50:
        return "Green"
    elif rgb[0] < 50 and rgb[1] < 50 and rgb[2] > 200:
        return "Blue"
    else:
        return "Unknown color"

print(detect_color([255, 0, 0]))  # Example input (Red)
