import cv2
import numpy as np

def main():
    cam = cv2.VideoCapture(0)
    if not cam.isOpened():
        print("The camera could not be loaded.")
        return
    print("test")

if __name__ == "__main__":
    main()
