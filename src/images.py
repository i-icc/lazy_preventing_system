import cv2
import numpy as np

class Images:
    def __init__(self,cam_num):
        self.cam = cv2.VideoCapture(cam_num)
        self.is_cam_ok = self.cam.isOpened()
        self.cascade = cv2.CascadeClassifier('../model/haarcascade_fullbody.xml')

    def get_image(self):
        ret, frame = self.cam.read()
        return frame

    def show_image(self):
        # get Image
        while True:
            ret, frame = self.cam.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            p1 , p2 = 20, 20
            hlower = self.cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=2, minSize=(p1, p2))
            for (x, y, w, h) in hlower:
                cv2.rectangle(frame, (x, y), (x + w, y+h), (255,0,0), 3)
            cv2.imshow("test", frame)
            cv2.waitKey(1)
            cv2.destroyAllWindows()

    def human_perception(self,image):
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        hlower = self.cascade.detectMultiScale(gray)
        return hlower

if __name__ == "__main__":
    images = Images(0)
    a = cv2.imread("./test.jpeg")
    h = images.human_perception(a)
    for (x, y, w, h) in h:
        cv2.rectangle(a, (x, y), (x + w, y+h), (255,0,0), 3)
    cv2.imshow("test", a)
    cv2.waitKey(0)
    cv2.destroyAllWindows()