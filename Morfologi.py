import cv2
import numpy as np

# Baca citra
img = cv2.imread('E:\\airta drafts\\sepeda.jpg', 0)

# Definisikan kernel
kernel = np.ones((5,5),np.uint8)

# Lakukan operasi erosi
erosion = cv2.erode(img, kernel, iterations = 1)

# Lakukan operasi dilasi
dilation = cv2.dilate(img, kernel, iterations = 1)

# Tampilkan hasil
cv2.imshow('Erosion', erosion)
cv2.imshow('Dilation', dilation)
cv2.waitKey(0)
cv2.destroyAllWindows()
