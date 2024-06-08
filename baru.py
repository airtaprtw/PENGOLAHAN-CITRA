import cv2

# Baca citra berwarna
image = cv2.imread('E:\\airta drafts\\sepeda.jpg')

#Resize Citra menjadi 300x300 px
resized_image = cv2.resize(image, (300, 300))

# Tampilkan citra asli, citra grayscale, dan citra biner
cv2.imshow('Original Image', image)

cv2.waitKey(0)
cv2.destroyAllWindows()