import cv2
import numpy as np
from matplotlib import pyplot as plt

# Baca citra
img = cv2.imread('E:\\airta drafts\\sepeda.jpg')

# Proses filter rata-rata
blur = cv2.blur(img, (5, 5))

# Proses filter Gaussian
gaussian_blur = cv2.GaussianBlur(img, (5, 5), 0)

# Proses filter median
median = cv2.medianBlur(img, 5)

# Tampilkan hasil
plt.subplot(2, 2, 1), plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)), plt.title('Citra Asli')
plt.subplot(2, 2, 2), plt.imshow(cv2.cvtColor(blur, cv2.COLOR_BGR2RGB)), plt.title('Filter Rata-rata')
plt.subplot(2, 2, 3), plt.imshow(cv2.cvtColor(gaussian_blur, cv2.COLOR_BGR2RGB)), plt.title('Filter Gaussian')
plt.subplot(2, 2, 4), plt.imshow(cv2.cvtColor(median, cv2.COLOR_BGR2RGB)), plt.title('Filter Median')
plt.show()
