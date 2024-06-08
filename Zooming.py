import cv2
import numpy as np

# Baca citra
img = cv2.imread('E:\\airta drafts\\sepeda.jpg')

# Tentukan faktor zooming
fx = 2  # faktor zooming horizontal
fy = 2  # faktor zooming vertikal

# Proses zooming
zoomed_img = cv2.resize(img, None, fx=fx, fy=fy, interpolation=cv2.INTER_LINEAR)

# Tampilkan citra asli dan citra yang sudah di-zoom
cv2.imshow('Citra Asli', img)
cv2.imshow('Citra Setelah Zooming', zoomed_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
