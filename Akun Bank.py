class AkunBank:
    def __init__(self, nomor_akun, nama_pemilik, saldo_awal):
        self._nomor_akun = nomor_akun
        self._nama_pemilik = nama_pemilik
        self._saldo = 0
        self.saldo = saldo_awal # Validasi awal [cite: 188]

    def setor_dana(self, jumlah):
        if jumlah > 0:
            self._saldo += jumlah # Saldo nambah [cite: 197]
            print(f"Setoran Rp{jumlah:,.0f} sukses.")
            return True
        return False

    def tarik_dana(self, jumlah):
        if 0 < jumlah <= self._saldo: # Cek saldo cukup atau nggak [cite: 198]
            self._saldo -= jumlah
            print(f"Penarikan Rp{jumlah:,.0f} sukses.")
            return True
        print("Penarikan gagal!")
        return False