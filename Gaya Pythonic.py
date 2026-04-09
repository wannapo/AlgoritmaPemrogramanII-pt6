class Produk:
    def __init__(self, nama, harga, stok):
        self._nama = nama
        self.harga = harga # Langsung lari ke @harga.setter [cite: 132]

    @property # Getter [cite: 136]
    def harga(self):
        return self._harga

    @harga.setter # Setter [cite: 138]
    def harga(self, nilai_baru):
        if isinstance(nilai_baru, (int, float)) and nilai_baru > 0: # Validasi angka positif [cite: 140]
            self._harga = nilai_baru
        else:
            print("Error: Harga tidak valid!")

# Cara pakenya lebih simpel:
keyboard = Produk("Mechanical Keyboard", 1200000, 20)
keyboard.harga = 1350000  # Kayak ganti variabel biasa, tapi validasi tetep jalan [cite: 163]