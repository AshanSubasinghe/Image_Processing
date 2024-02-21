import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
def zoom_nearest_neighbor(im, scale_factor):
    h, w = im.shape[:2]
    new_h, new_w = int(h * scale_factor), int(w * scale_factor)
    zoomed_im = np.zeros((new_h, new_w), dtype=np.uint8)
    for i in range(new_h):
        for j in range(new_w):
            original_i, original_j = int(i / scale_factor), int(j / scale_factor)
            zoomed_im[i, j] = im[original_i, original_j]
    return zoomed_im
image = cv.imread('C:\Image_Processing_2\im02small.png', cv.IMREAD_GRAYSCALE)
zoomed_image_nn = zoom_nearest_neighbor(image, 4)
cv.imshow('Zoomed Image (Nearest-Neighbor)', zoomed_image_nn)
cv.waitKey(0)
cv.destroyAllWindows()
