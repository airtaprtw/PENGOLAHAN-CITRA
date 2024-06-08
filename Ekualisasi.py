import cv2
import numpy as np
import matplotlib.pyplot as plt

# Baca gambar
img = cv2.imread('E:\\airta drafts\\sepeda.jpg', 0)

# Lakukan ekualisasi citra
equ = cv2.equalizeHist(img)

# Tampilkan citra asli dan citra yang sudah diekualisasi
plt.figure(figsize=(8, 4))
plt.subplot(1, 2, 1)
plt.imshow(img, cmap='gray')
plt.title('Citra Asli')
plt.subplot(1, 2, 2)
plt.imshow(equ, cmap='gray')
plt.title('Citra yang Sudah Diekualisasi')
plt.show()
