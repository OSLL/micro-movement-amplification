import numpy as np
import argparse
import cv2
import os


def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", default=None, help="path to video")
    parser.add_argument("--length", default=3, help="Length of frame sequence")
    parser.add_argument("--dir", default="data", help="destination for dataset")
    return parser


def generate(parser):
    if not parser.file:
        return
    cap = cv2.VideoCapture(parser.file)

    if not cap.isOpened():
        print("Error opening video stream or file")

    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            cv2.imshow('Frame', frame)
            # Press Q on keyboard to  exit
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
        else:
            break
    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    parser = get_parser()
    generate(parser)
