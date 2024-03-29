import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
image1 = cv.imread(r'C:\Image_Processing_2\rice_gaussian_noise.png', cv.IMREAD_GRAYSCALE)
image2 = cv.imread(r'C:\Image_Processing_2\rice_salt_pepper_noise.png', cv.IMREAD_GRAYSCALE)
if image1 is None or image2 is None:
    print("Error: Unable to read one or both images.")
else:
    blurred_image1 = cv.GaussianBlur(image1, (5, 5), 0)
    blurred_image2 = cv.GaussianBlur(image2, (5, 5), 0)
    _, segmented_image1 = cv.threshold(blurred_image1, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)
    _, segmented_image2 = cv.threshold(blurred_image2, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)
    f, ax = plt.subplots(2, 3, figsize=(15, 10))
    ax[0, 0].imshow(image1, cmap='gray')
    ax[0, 0].set_title('Original Image 1')
    ax[0, 0].axis('off')
    ax[0, 1].imshow(blurred_image1, cmap='gray')
    ax[0, 1].set_title('Blurred Image 1')
    ax[0, 1].axis('off')
    ax[0, 2].imshow(segmented_image1, cmap='gray')
    ax[0, 2].set_title('Segmented Image 1')
    ax[0, 2].axis('off')
    ax[1, 0].imshow(image2, cmap='gray')
    ax[1, 0].set_title('Original Image 2')
    ax[1, 0].axis('off')
    ax[1, 1].imshow(blurred_image2, cmap='gray')
    ax[1, 1].set_title('Blurred Image 2')
    ax[1, 1].axis('off')
    ax[1, 2].imshow(segmented_image2, cmap='gray')
    ax[1, 2].set_title('Segmented Image 2')
    ax[1, 2].axis('off')
    plt.tight_layout()
    plt.show()
