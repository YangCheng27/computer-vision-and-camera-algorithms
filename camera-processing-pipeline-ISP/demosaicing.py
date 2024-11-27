import cv2
import numpy as np
import matplotlib.pyplot as plt
import sys

def rggb_demosaicing(img_gray):
    # input: gray bayer image
    # output: recovered image
    rows, cols = img_gray.shape
    
    # 1. recover filter's color
    bayer_mask = np.zeros((rows, cols, 3))
    bayer_mask[0::2, 0::2, 0] = 1  # Red channel
    bayer_mask[0::2, 1::2, 1] = 1  # Green channel
    bayer_mask[1::2, 0::2, 1] = 1  # Green channel
    bayer_mask[1::2, 1::2, 2] = 1  # Blue channel
    new_img = np.stack((img_gray,) * 3, axis = -1)
    new_img = new_img * bayer_mask

    # 2. interpolation
    for row in range(rows):
        mask_row = row%2
        for col in range(cols):
            mask_col = col%2

            # green mask location get other two color
            if mask_row != mask_col:
                if mask_row == 1:
                    new_img[row, col, 0] = top_bottom_avg(img_gray, row, col) # red
                    new_img[row, col, 2] = left_right_avg(img_gray, row, col) # blue
                else:
                    new_img[row, col, 0] = left_right_avg(img_gray, row, col) # red
                    new_img[row, col, 2] = top_bottom_avg(img_gray, row, col) # blue
            else:
                # red mask location get other two color
                if mask_row == 0:
                    new_img[row, col, 1] = four_neighbors_avg(img_gray, row, col) # green
                    new_img[row, col, 2] = four_corners_avg(img_gray, row, col) # blue

                # blue mask location get other two color
                if mask_row == 1:
                    new_img[row, col, 1] = four_neighbors_avg(img_gray, row, col) # green
                    new_img[row, col, 0] = four_corners_avg(img_gray, row, col) # red

    return new_img / 255


def four_neighbors_avg(img_gray, row, col):
    avg = None
    right = (row, col + 1)
    left =  (row, col - 1)
    top = (row - 1, col)
    bottom = (row + 1, col)

    # 1. corners or edges
    row_len, col_len = img_gray.shape
    if row == 0:
        if col == 0:
            avg = img_gray[right] / 2 + img_gray[bottom] / 2
        elif col == (col_len - 1):
            avg = img_gray[left] / 2 + img_gray[bottom] / 2
        else:
            avg = img_gray[left] / 3 + img_gray[bottom] / 3 + img_gray[right] / 3
    elif row == (row_len - 1):
        if col == 0:
            avg = img_gray[top] / 2 + img_gray[right] / 2
        elif col == (col_len - 1):
            avg = img_gray[top] / 2+ img_gray[left] / 2
        else:
            avg = img_gray[left] / 3+ img_gray[top] / 3+ img_gray[right] / 3
    elif col == 0:
        avg = img_gray[top] / 3 + img_gray[right] / 3 + img_gray[bottom] / 3
    elif col == (col_len - 1):
        avg = img_gray[top] / 3+ img_gray[left] / 3 + img_gray[bottom] / 3

    # 3. normal case
    else:
        avg = img_gray[top] / 4 + img_gray[left] / 4 + img_gray[bottom] / 4 + img_gray[right] / 4

    return avg


def four_corners_avg(img_gray, row, col):
    avg = None

    left_top =  (row - 1, col - 1)
    left_bottom= (row + 1, col - 1)
    right_top = (row - 1, col + 1)
    right_bottom = (row + 1, col + 1)

    # 1. corners or edges
    row_len, col_len = img_gray.shape
    if row == 0:
        if col == 0:
            avg = img_gray[right_bottom]
        elif col == (col_len - 1):
            avg = img_gray[left_bottom]
        else:
            avg = img_gray[left_bottom] / 2 + img_gray[right_bottom] / 2
    elif row == (row_len - 1):
        if col == 0:
            avg = img_gray[right_top]
        elif col == (col_len - 1):
            avg = img_gray[left_top]
        else:
            avg = img_gray[left_top] / 2 + img_gray[right_top] / 2
    elif col == 0:
        avg = img_gray[right_top] / 2 + img_gray[right_bottom] / 2
    elif col == (col_len - 1):
        avg = img_gray[left_top] / 2 + img_gray[left_bottom] / 2

    # 3. normal case
    else:
        avg = img_gray[left_top] / 4 + img_gray[left_bottom] / 4 + img_gray[right_top] / 4 + img_gray[right_bottom] / 4

    return avg


def top_bottom_avg(img_gray, row, col):
    avg = None
    top = (row - 1, col)
    bottom = (row + 1, col)
    row_len, col_len = img_gray.shape
    if row == 0:
        avg = img_gray[bottom]
    elif row == (row_len - 1):
        avg = img_gray[top]
    else:
        avg = img_gray[top] / 2 + img_gray[bottom] / 2
    return avg


def left_right_avg(img_gray, row, col):
    avg = None
    left = (row, col - 1)
    right = (row, col + 1)
    row_len, col_len = img_gray.shape
    if col == 0:
        avg = img_gray[right]
    elif col == (col_len - 1):
        avg = img_gray[left]
    else:
        avg = img_gray[left] / 2 + img_gray[right] / 2
    return avg

def img_display(img, name):
    if len(img.shape) == 2:
        plt.imshow(img, cmap = 'gray')
    else:
        plt.imshow(img)
    plt.axis('off')
    plt.title(name)
    fig = plt.gcf()
    fig.set_size_inches(8, 5)
    plt.tight_layout()
    plt.savefig('imgs/' + name)
    plt.show()

def rggb_demosaicing_with_wb(img_gray, raw):
    # input: gray bayer image
    # output: recovered image
    rows, cols = img_gray.shape
    
    # 1. recover filter's color
    bayer_mask = np.zeros((rows, cols, 3))
    bayer_mask[0::2, 0::2, 0] = 1  # Red channel
    bayer_mask[0::2, 1::2, 1] = 1  # Green channel
    bayer_mask[1::2, 0::2, 1] = 1  # Green channel
    bayer_mask[1::2, 1::2, 2] = 1  # Blue channel
    new_img = np.stack((img_gray,) * 3, axis = -1)
    new_img = new_img * bayer_mask

    wb_gains = raw.camera_whitebalance  # R, G1, B, G2
    wb_gains_vector = np.array([wb_gains[0], wb_gains[1], wb_gains[3]], dtype=np.float32)
    new_img *= wb_gains_vector

    # 2. interpolation
    for row in range(rows):
        mask_row = row%2
        for col in range(cols):
            mask_col = col%2

            # green mask location get other two color
            if mask_row != mask_col:
                if mask_row == 1:
                    new_img[row, col, 0] = top_bottom_avg(img_gray, row, col) # red
                    new_img[row, col, 2] = left_right_avg(img_gray, row, col) # blue
                else:
                    new_img[row, col, 0] = left_right_avg(img_gray, row, col) # red
                    new_img[row, col, 2] = top_bottom_avg(img_gray, row, col) # blue
            else:
                # red mask location get other two color
                if mask_row == 0:
                    new_img[row, col, 1] = four_neighbors_avg(img_gray, row, col) # green
                    new_img[row, col, 2] = four_corners_avg(img_gray, row, col) # blue

                # blue mask location get other two color
                if mask_row == 1:
                    new_img[row, col, 1] = four_neighbors_avg(img_gray, row, col) # green
                    new_img[row, col, 0] = four_corners_avg(img_gray, row, col) # red

    return new_img / 255

# if __name__ == '__main__':
#     img = cv2.imread(sys.argv[1]) # BGR iamge
#     img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#     img = cv2.resize(img, (1200, 750))

#     img_display(img, 'original image')
#     sensor_layout, sensor_layout_gray= bayer_filter(img)
#     img_display(sensor_layout, 'byer filter color image')
#     img_display(sensor_layout_gray, 'byer filter gray image')
#     img_display(rgb_demosaicing(sensor_layout_gray), 'recovered image from byer filter gray image')