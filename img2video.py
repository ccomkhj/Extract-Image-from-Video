# Importing all necessary libraries
import cv2
import os
import argparse
from pathlib import Path

def img_to_video(img_path:str, path_output_dir:str, frame_rate:int, format:str):
    size = (1280, 720)
    out = cv2.VideoWriter(os.path.join(path_output_dir,'project.mp4'),cv2.VideoWriter_fourcc('m', 'p', '4', 'v'), frame_rate, size)
    filenames = sorted(Path(img_path).glob(f'*.{format}'))

    for filename in filenames :
        img = cv2.imread(filename.__str__())
        img = cv2.resize(img, size)
        out.write(img)        

    out.release()

if __name__ == "__main__":
    parser = argparse.ArgumentParser("Collect images from a video clip")
    parser.add_argument("--img", help="location of img files")
    parser.add_argument("--save", default="video", help="location of directory to save output images")
    parser.add_argument("--frame",  default=5, help="frame frequency how often to collect images.")
    parser.add_argument("--format",  default="png", help="format of image files")
    args = parser.parse_args()

    args.img = "/home/hexaburbach/codes/hexa_img/output"
    img_to_video(args.img, args.save, args.frame, args.format)