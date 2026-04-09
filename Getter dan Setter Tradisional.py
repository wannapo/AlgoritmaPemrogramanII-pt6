class Produk:
    def __init__(self, nama, harga, stok):
        self._nama = nama    # Protected (pakai underscore _) [cite: 64]
        self._harga = harga
        self._stok = stok

    def get_harga(self): # Getter: Mengambil nilai [cite: 53]
        return self._harga

    def set_harga(self, harga_baru): # Setter: Mengubah nilai + Validasi [cite: 56, 58]
        if harga_baru > 0:
            self._harga = harga_baru
            print(f"Harga {self._nama} berhasil diubah.")
        else:
            print("Error: Harga harus lebih besar dari nol.")

# Cara pakenya:
laptop = Produk("Laptop", 15000000, 10)
laptop.set_harga(16000000) # Panggil fungsi setter [cite: 90]