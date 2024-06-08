from PIL import Image

def flipping_vertikal(gambar, nama_setelah_disave):
    CITRA = Image.open(gambar)
    PIXEL = CITRA.load()

    ukuran_horizontal = CITRA.size[0]
    ukuran_vertikal = CITRA.size[1]

    CITRA_BARU = Image.new("RGB", (ukuran_horizontal, ukuran_vertikal))
    PIXEL_BARU = CITRA_BARU.load()

    for x in range(ukuran_horizontal):
        for y in range(ukuran_vertikal):
            PIXEL_BARU[x, y] = PIXEL[x, ukuran_vertikal - 1 - y]

    CITRA_BARU.save(nama_setelah_disave)

def flipping_horizontal(gambar, nama_setelah_disave):
    CITRA = Image.open(gambar)
    PIXEL = CITRA.load()

    ukuran_horizontal = CITRA.size[0]
    ukuran_vertikal = CITRA.size[1]

    CITRA_BARU = Image.new("RGB", (ukuran_horizontal, ukuran_vertikal))
    PIXEL_BARU = CITRA_BARU.load()

    for x in range(ukuran_horizontal):
        for y in range(ukuran_vertikal):
            PIXEL_BARU[x, y] = PIXEL[ukuran_horizontal - 1 - x, y]

    CITRA_BARU.save(nama_setelah_disave)

def flipping_titik_asal(gambar, nama_setelah_disave):
    CITRA = Image.open(gambar)
    PIXEL = CITRA.load()

    ukuran_horizontal = CITRA.size[0]
    ukuran_vertikal = CITRA.size[1]

    CITRA_BARU = Image.new("RGB", (ukuran_horizontal, ukuran_vertikal))
    PIXEL_BARU = CITRA_BARU.load()

    for x in range(ukuran_horizontal):
        for y in range(ukuran_vertikal):
            PIXEL_BARU[x, y] = PIXEL[ukuran_horizontal - 1 - x, ukuran_vertikal -1 -y]

    CITRA_BARU.save(nama_setelah_disave)

flipping_vertikal('E:\\airta drafts\\sepeda.jpg', 'sepeda_flip_vertikal.jpg')
flipping_horizontal('E:\\airta drafts\\sepeda.jpg', 'sepeda_flip_horizontal.jpg')
flipping_titik_asal('E:\\airta drafts\\sepeda.jpg', 'sepeda_flip_titik_asal.jpg')