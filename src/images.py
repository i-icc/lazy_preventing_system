import cv2
import numpy as np

class Images:
    def __init__(self,cam_num):
        self.cam = cv2.VideoCapture(cam_num)
        self.is_cam_ok = self.cam.isOpened()

    def get_image(self):
        ret, frame = self.cam.read()
        return frame

    def show_image(self):
        # get Image
        while True:
            ret, frame = self.cam.read()
            cv2.imshow("test", frame)
            cv2.waitKey(1)
            cv2.destroyAllWindows()

    def human_perception(self):
        image = self.get_image()
        
        pass