import numpy as np
import cv2

import matplotlib.pyplot as plt
from matplotlib.image import imread
image = imread('E:\\airta drafts\\sepeda.jpg')

# Translasi
M = np.float32([[1, 0, 50], [0, 1, 30]])
translated_image = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))

# Rotasi
angle = 45
M = cv2.getRotationMatrix2D((image.shape[1] / 2, image.shape[0] / 2), angle, 1)
rotated_image = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))

# Flipping (Horizontal and Vertical)
flipped_horizontal = cv2.flip(image, 1)
flipped_vertical = cv2.flip(image, 0)

# Zooming (Scaling)
scaled_image = cv2.resize(image, None, fx=2, fy=2)

# Display the results
plt.subplot(231), plt.imshow(image, cmap='gray'), plt.title('Original Image')
plt.subplot(232), plt.imshow(translated_image, cmap='gray'), plt.title('Translated Image')
plt.subplot(233), plt.imshow(rotated_image, cmap='gray'), plt.title('Rotated Image')
plt.subplot(234), plt.imshow(flipped_horizontal, cmap='gray'), plt.title('Horizontal Flip')
plt.subplot(235), plt.imshow(flipped_vertical, cmap='gray'), plt.title('Vertical Flip')
plt.subplot(236), plt.imshow(scaled_image, cmap='gray'), plt.title('Zoomed Image')
plt.show()