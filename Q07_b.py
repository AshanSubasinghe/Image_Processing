import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

def bilinear_interpolation(im, scale_factor):
    h, w = im.shape[:2]
    new_h, new_w = int(h * scale_factor), int(w * scale_factor)
    zoomed_im = np.zeros((new_h, new_w), dtype=np.uint8)

    for i in range(new_h):
        for j in range(new_w):
            original_i, original_j = i / scale_factor, j / scale_factor
            i_low, j_low = int(original_i), int(original_j)
            i_high, j_high = min(i_low + 1, h - 1), min(j_low + 1, w - 1)
            i_ratio, j_ratio = original_i - i_low, original_j - j_low
            top_left = image[i_low, j_low]
            top_right = image[i_low, j_high]
            bottom_left = image[i_high, j_low]
            bottom_right = image[i_high, j_high]
            zoomed_im[i, j] = (1 - j_ratio) * ((1 - i_ratio) * top_left + i_ratio * bottom_left) + \
                                  j_ratio * ((1 - i_ratio) * top_right + i_ratio * bottom_right)

    return zoomed_im

image = cv.imread('C:\Image_Processing_2\im03small.png', cv.IMREAD_GRAYSCALE)
zoomed_image_bilinear = bilinear_interpolation(image, 4)

cv.imshow('Zoomed Image (Bilinear Interpolation)', zoomed_image_bilinear)
cv.waitKey(0)
cv.destroyAllWindows()