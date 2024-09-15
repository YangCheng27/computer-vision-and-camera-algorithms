import cv2
import numpy as np


def bayer_filter(img):
    # input: color RGB image
    # output: a filtered color image and a gray scaled image
    #########
    # b | g #
    # --|-- #
    # g | r #
    #########

    # Bayer Filter Mask
    bayer_mask = np.zeros_like(img)
    bayer_mask[0::2, 0::2, 2] = 1  # Blue channel
    bayer_mask[0::2, 1::2, 1] = 1  # Green channel
    bayer_mask[1::2, 0::2, 1] = 1  # Green channel
    bayer_mask[1::2, 1::2, 0] = 1  # Red channel

    # Apply Bayer Mask
    sensor_layout = img * bayer_mask

    return sensor_layout