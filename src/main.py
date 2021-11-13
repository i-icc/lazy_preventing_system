import cv2
import numpy as np

def main():
    # load camera
    cam = cv2.VideoCapture(0)
    if not cam.isOpened():
        print("The camera could not be loaded.")
        return

    # get Image
    while True:
        ret, frame = cam.read()
        cv2.imshow("test", frame)
        cv2.waitKey(1)
        cv2.destroyAllWindows()
    

if __name__ == "__main__":
    main()
