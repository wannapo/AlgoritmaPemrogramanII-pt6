class Mahasiswa:
    def __init__(self, nama, nim):
        # Enkapsulasi: Menyembunyikan detail internal [cite: 23, 28]
        self._nama = nama  # Protected [cite: 31, 201]
        self._nim = nim    # Protected [cite: 31, 201]
        self._nilai_matakuliah = {} # Data disimpan dalam dictionary [cite: 201]

    @property
    def nama(self):
        """Getter: Nama bersifat read-only [cite: 53, 202]"""
        return self._nama

    @property
    def nim(self):
        """Getter: NIM bersifat read-only [cite: 53, 202]"""
        return self._nim

    @property
    def nilai_rata_rata(self):
        """Getter: Menghitung rata-rata secara dinamis [cite: 203]"""
        if not self._nilai_matakuliah:
            return 0 # Jika tidak ada matkul, balikkan 0 [cite: 204]
        return sum(self._nilai_matakuliah.values()) / len(self._nilai_matakuliah)

    def tambah_atau_update_nilai(self, matkul, nilai):
        """Create & Update: Mengontrol penulisan data [cite: 57, 58]"""
        if isinstance(nilai, (int, float)) and 0 <= nilai <= 100:
            self._nilai_matakuliah[matkul] = nilai
            print(f"Selesai: Nilai {matkul} berhasil disimpan.")
        else:
            print("Error: Nilai harus angka 0-100.")

    def hapus_nilai(self, matkul):
        """Delete: Menghapus data dari dictionary internal"""
        if matkul in self._nilai_matakuliah:
            del self._nilai_matakuliah[matkul]
            print(f"Selesai: Data {matkul} berhasil dihapus.")
        else:
            print(f"Error: Mata kuliah {matkul} tidak ditemukan.")

    def tampilkan_data(self):
        """Read: Mengakses data melalui antarmuka publik [cite: 30]"""
        print(f"\n=== Data Mahasiswa ===")
        print(f"Nama      : {self.nama}")
        print(f"NIM       : {self.nim}")
        print(f"Nilai     : {self._nilai_matakuliah}")
        print(f"Rata-rata : {self.nilai_rata_rata:.2f}")

# --- Program Utama (Interaktif CRUD) ---
print("Registrasi Mahasiswa Baru")
nama_input = input("Masukkan Nama: ")
nim_input = input("Masukkan NIM: ")
mhs = Mahasiswa(nama_input, nim_input)

while True:
    print("\nMenu CRUD Nilai:")
    print("1. Lihat Data (Read)")
    print("2. Tambah/Ubah Nilai (Create/Update)")
    print("3. Hapus Nilai (Delete)")
    print("4. Keluar")
    
    pilihan = input("Pilih menu (1-4): ")

    if pilihan == '1':
        mhs.tampilkan_data()
    elif pilihan == '2':
        mk = input("Nama Mata Kuliah: ")
        try:
            ni = float(input("Masukkan Nilai: "))
            mhs.tambah_atau_update_nilai(mk, ni)
        except ValueError:
            print("Error: Input nilai harus angka!")
    elif pilihan == '3':
        mk = input("Mata kuliah yang mau dihapus: ")
        mhs.hapus_nilai(mk)
    elif pilihan == '4':
        print("Program selesai. Semangat kuliahnya!")
        break
    else:
        print("Pilihan tidak valid.")