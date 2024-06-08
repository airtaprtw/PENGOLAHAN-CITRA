import numpy as np
import cv2
import matplotlib.pyplot as plt
from matplotlib.image import imread
image = imread('E:\\airta drafts\\sepeda.jpg')
plt.imshow(image)
plt.axis  # Untuk menghilangkan sumbu
plt.show()


# # Mengubah Citra menjadi Citra Grayscale:
import cv2
import matplotlib.pyplot as plt
color_image = cv2.imread('E:\\airta drafts\\sepeda.jpg')

# Convert to grayscale
gray_image = cv2.cvtColor(color_image, cv2.COLOR_BGR2GRAY)

# Display the grayscale image
plt.imshow(gray_image, cmap='gray')
plt.axis()
plt.show()


# # Mengubah Citra Grayscale Menjadi Citra Biner:
_, binary_image = cv2.threshold(gray_image, 128, 255, cv2.THRESH_BINARY)

# Display the binary image
plt.imshow(binary_image, cmap='gray')
plt.axis('off')
plt.show()