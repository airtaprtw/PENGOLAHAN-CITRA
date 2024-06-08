import cv2
import numpy as np

# Baca dua citra
img1 = cv2.imread('E:\\airta drafts\\sepeda.jpg')
img2 = cv2.imread('E:\\airta drafts\\laut.jpg')

# Resize citra kedua agar ukurannya sama dengan citra pertama
img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))

# Lakukan operasi AND pada kedua citra
bitwise_and = cv2.bitwise_and(img1, img2)

# Lakukan operasi OR pada kedua citra
bitwise_or = cv2.bitwise_or(img1, img2)

# Tampilkan hasil
cv2.imshow('Bitwise AND', bitwise_and)
cv2.imshow('Bitwise OR', bitwise_or)
cv2.waitKey(0)
cv2.destroyAllWindows()