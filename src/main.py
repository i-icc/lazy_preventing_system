from argparse import ArgumentParser

from images import Images 

def main():
    args = get_args()
    # load camera
    images = Images(args.camera_number)
    if not images.is_cam_ok:
        print("The camera could not be loaded.")
        return

    images.show_image()
    
    
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
