# pip3 install pillow (Install PIL Python Imgae Library)
from PIL import Image

# fungsi citra biner
def citra_biner(nilai_ambang):
    # konversi gambar RGB ke grayscale
    CITRA_GRAYSCALE = Image.open('E:\\airta drafts\\sepeda.jpg').convert('L')
    PIXEL_GRAYSCALE = CITRA_GRAYSCALE.load()

    ukuran_horizontal = CITRA_GRAYSCALE.size[0]
    ukuran_vertikal = CITRA_GRAYSCALE.size[1]

    for x in range(ukuran_horizontal):
        for y in range(ukuran_vertikal):
            if PIXEL_GRAYSCALE[x, y] < nilai_ambang:
                PIXEL_GRAYSCALE[x, y] = 0
            else:
                PIXEL_GRAYSCALE[x, y] = 255

    nama_setelah_disave = 'gambar_sepeda_biner' + str(nilai_ambang) + '.jpg'
    CITRA_GRAYSCALE.save(nama_setelah_disave)
citra_biner(128)