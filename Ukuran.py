# OpenCv (Open Source Computer Vision Library) adalah sebuah pustaka sumber terbuka yang digunakan untuk memproses gambar dan video
# Install OpenCV (pip install opencv-python)
import cv2

# Untuk Memasukan Gambar yang Ingin Dideteksi Harus Memasukkan Gambar Pada Satu folder dengan codingan 
# 0 = IMREAD_GRAYSCALE
# 1 = IMREAD_COLOR
load = cv2.imread('E:\\airta drafts\\ibu.jpg', 1)
print (load.shape)
print ('width : ', load.shape[1])
print ('height : ', load.shape[0])
print ('size : ', load.size)