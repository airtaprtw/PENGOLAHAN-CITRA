from PIL import Image

def show_pixel_values(image_path):
    # Buka gambar menggunakan PIL
    image = Image.open(image_path)
    
    # Dapatkan ukuran gambar (lebar x tinggi)
    width, height = image.size
    
    # Dapatkan mode gambar (misalnya 'RGB' atau 'L')
    mode = image.mode
    
    # Loop melalui setiap piksel dan tampilkan nilai pikselnya
    for y in range(height):
        for x in range(width):
            pixel_value = image.getpixel((x, y))
            print(f"Pixel di posisi ({x}, {y}): {pixel_value}")
    
    # Tutup gambar
    image.close()

# Ganti 'nama_gambar.jpg' dengan nama gambar yang ingin Anda gunakan
gambar_path = 'E:\\airta drafts\\sepeda.jpg'
show_pixel_values(gambar_path)