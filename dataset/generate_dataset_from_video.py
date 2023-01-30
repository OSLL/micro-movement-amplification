from collections import deque
from time import sleep
import numpy as np
import argparse
import shutil
import cv2
import sys
import os


def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", default=None, help="path to video")
    parser.add_argument("--maxlen", default=3, help="Length of frame sequence")
    parser.add_argument("--dir", default="data", help="destination for dataset")
    return parser.parse_args()


def generate(parser):
    if not parser.file:
        return
    deque_frames = deque(maxlen=int(parser.maxlen))
    cap = cv2.VideoCapture(parser.file)

    if not cap.isOpened():
        print("Error opening video stream or file")

    # remove and create directory of dataset
    if os.path.exists(os.path.join(os.getcwd(), parser.dir)):
        shutil.rmtree(parser.dir)
    os.mkdir(parser.dir)

    idx = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            deque_frames.append(frame)
            if len(deque_frames) == deque_frames.maxlen:
                idx += 1
                path_element = f"{os.getcwd()}/{parser.dir}/imgs{idx}"
                os.mkdir(path_element)
                # frame{chr(65+)}
                for index, frame in enumerate(deque_frames):
                    filename = f"{path_element}/frame{chr(65 + index)}.jpg"
                    status = cv2.imwrite(filename, frame)
                    print(f"Image {filename} to file-system : {status}")
                # save_element(idx, deque_frames.copy())
        else:
            break
    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    parser = get_parser()
    generate(parser)
