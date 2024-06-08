import cv2
import numpy as np
import matplotlib.pyplot as plt

#Baca dua citra
img1 = cv2.imread('E:\\airta drafts\\sepeda.jpg')
img2 = cv2.imread('E:\\airta drafts\\laut.jpg')

#Ukuran
img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))

#Operasi Penambahan Citra
added_image = cv2.addWeighted(img1, 0.5, img2, 0.5, 0)

#Operasi Pengurangan Citra
subtracted_image = cv2.subtract(img1, img2)

#Tampilkan Hasil
plt.figure(figsize=(12, 6))
plt.subplot(1,3,1)
plt.imshow(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
plt.title('sepeda.jpg')
plt.subplot(1,3,2)
plt.imshow(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB))
plt.title('laut.jpg')
plt.subplot(1,3,3)
plt.imshow(cv2.cvtColor(added_image, cv2.COLOR_BGR2RGB))
plt.title('Hasil Penambahan Citra')
plt.show()

plt.figure(figsize=(12, 6))
plt.subplot(1,3,1)
plt.imshow(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
plt.title('sepeda.jpg')
plt.subplot(1,3,2)
plt.imshow(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB))
plt.title('laut.jpg')
plt.subplot(1,3,3)
plt.imshow(cv2.cvtColor(subtracted_image, cv2.COLOR_BGR2RGB))
plt.show()