#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import cv2


# In[4]:


import matplotlib.pyplot as plt
from matplotlib.image import imread
image = imread('E:\\airta drafts\\sepeda.jpg')
plt.imshow(image)
plt.axis  # Untuk menghilangkan sumbu
plt.show()


# # Mengubah Citra menjadi Citra Grayscale:

# In[5]:


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

# In[6]:


_, binary_image = cv2.threshold(gray_image, 128, 255, cv2.THRESH_BINARY)

# Display the binary image
plt.imshow(binary_image, cmap='gray')
plt.axis('off')
plt.show()


# # Menampilkan Pixel-pixel dalam Citra:

# In[8]:


for i in range(binary_image.shape[0]):
    for j in range(binary_image.shape[1]):
        pixel_value = binary_image[i, j]
        print(f"Pixel di ({i}, {j}): {pixel_value}")


# # Membuat Citra Negatif:

# # import cv2
# import matplotlib.pyplot as plt
# image = cv2.imread('E:\\airta drafts\\sepeda.jpg')
# negative_image = 255 - image
# plt.imshow(cv2.cvtColor(negative_image, cv2.COLOR_BGR2RGB))
# plt.axis()
# plt.show()
# 

# # Menampilkan Histogram Citra:

# In[10]:


gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
histogram = cv2.calcHist([gray_image], [0], None, [256], [0, 256])
plt.plot(histogram)
plt.title('Histogram')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')
plt.show()


# # Melakukan Equalisasi Citra:
# 

# In[11]:


# Equalize the grayscale image
equalized_image = cv2.equalizeHist(gray_image)

# Display the equalized image
plt.imshow(equalized_image, cmap='gray')
plt.axis('off')
plt.show()


# # Melakukan Image Brightening:

# In[12]:


# Brightening factor (adjust as needed)
alpha = 1.5

# Brighten the image
brightened_image = cv2.convertScaleAbs(image, alpha=alpha, beta=0)

# Display the brightened image
plt.imshow(cv2.cvtColor(brightened_image, cv2.COLOR_BGR2RGB))
plt.axis()
plt.show()


# In[14]:


# Load the second image
image2 = cv2.imread('E:\\airta drafts\\sepeda.jpg')

# Add the two images
result_image = cv2.add(image, image2)

# Display the result
plt.imshow(cv2.cvtColor(result_image, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.show()


# In[16]:


import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load two images
image1 = cv2.imread('E:\\airta drafts\\sepeda.jpg', cv2.IMREAD_GRAYSCALE)
image2 = cv2.imread('E:\\airta drafts\\sepeda.jpg', cv2.IMREAD_GRAYSCALE)

# Perform bitwise AND operation
result_and = cv2.bitwise_and(image1, image2)

# Perform bitwise OR operation
result_or = cv2.bitwise_or(image1, image2)

# Perform morphological dilation
kernel = np.ones((5, 5), np.uint8)
dilated_image = cv2.dilate(image1, kernel, iterations=1)

# Display the results
plt.subplot(231), plt.imshow(image1, cmap='gray'), plt.title('Image 1')
plt.subplot(232), plt.imshow(image2, cmap='gray'), plt.title('Image 2')
plt.subplot(233), plt.imshow(result_and, cmap='gray'), plt.title('Bitwise AND')
plt.subplot(234), plt.imshow(result_or, cmap='gray'), plt.title('Bitwise OR')
plt.subplot(235), plt.imshow(dilated_image, cmap='gray'), plt.title('Dilated Image')
plt.show()


# In[17]:


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


# In[18]:


# Gaussian Blur
gaussian_blur = cv2.GaussianBlur(image, (5, 5), 0)

# Median Blur
median_blur = cv2.medianBlur(image, 5)

# Bilateral Filter
bilateral_filter = cv2.bilateralFilter(image, 9, 75, 75)

# Display the results
plt.subplot(131), plt.imshow(gaussian_blur, cmap='gray'), plt.title('Gaussian Blur')
plt.subplot(132), plt.imshow(median_blur, cmap='gray'), plt.title('Median Blur')
plt.subplot(133), plt.imshow(bilateral_filter, cmap='gray'), plt.title('Bilateral Filter')
plt.show()


# In[ ]:




