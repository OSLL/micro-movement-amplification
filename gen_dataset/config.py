class Config(object):
    OUTPUT_DIR = "./result"
    FRAME_POSTFIXES = "AB"
    AMP_FRAME_POSTFIX = "AMP"
    LABELS_FILENAME = "labels.txt"

    MIN_NUM_OBJECTS = 4
    MAX_NUM_OBJECTS = 10

    TRAIN_DATASET_SIZE = 10
    TEST_DATASET_SIZE = 10#int(TRAIN_DATASET_SIZE * 0.2)
    # WxH
    WIDTH = 540
    HEIGHT = 540