import cv2
import numpy as np
from argparse import ArgumentParser

def main():
    args = get_args()
    # load camera
    cam = cv2.VideoCapture(args.camera_number)
    if not cam.isOpened():
        print("The camera could not be loaded.")
        return

    # get Image
    while True:
        ret, frame = cam.read()
        cv2.imshow("test", frame)
        cv2.waitKey(1)
        cv2.destroyAllWindows()
    
def get_args():
    parser = ArgumentParser(description="lazy_preventing_system")
    parser.add_argument(
        "-cam",
        "--camera_number",
        type=int,
        default=0,
        help="set camera number.default=0",
    )
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    main()
