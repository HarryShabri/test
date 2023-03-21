# Daftar mahasiswa awal
mahasiswa = []

# Fungsi untuk menambahkan mahasiswa ke daftar
def tambah_mahasiswa():
    nama = input("Masukkan nama mahasiswa: ")
    nim = input("Masukkan NIM mahasiswa: ")
    mahasiswa.append({"nama": nama, "nim": nim})
    print("Mahasiswa berhasil ditambahkan!")

# Fungsi untuk menampilkan daftar mahasiswa
def tampilkan_mahasiswa():
    if not mahasiswa:
        print("Daftar mahasiswa kosong!")
    else:
        print("Daftar mahasiswa:")
        for mhs in mahasiswa:
            print(f"- {mhs['nama']}, NIM: {mhs['nim']}")

# Fungsi untuk memperbarui data mahasiswa
def perbarui_mahasiswa():
    if not mahasiswa:
        print("Daftar mahasiswa kosong!")
    else:
        nim = input("Masukkan NIM mahasiswa yang ingin diperbarui: ")
        for mhs in mahasiswa:
            if mhs["nim"] == nim:
                mhs["nama"] = input("Masukkan nama mahasiswa baru: ")
                print("Data mahasiswa berhasil diperbarui!")
                return
        print("Mahasiswa tidak ditemukan!")

# Fungsi untuk menghapus mahasiswa dari daftar
def hapus_mahasiswa():
    if not mahasiswa:
        print("Daftar mahasiswa kosong!")
    else:
        nim = input("Masukkan NIM mahasiswa yang ingin dihapus: ")
        for mhs in mahasiswa:
            if mhs["nim"] == nim:
                mahasiswa.remove(mhs)
                print("Mahasiswa berhasil dihapus!")
                return
        print("Mahasiswa tidak ditemukan!")

# Fungsi utama
def main():
    while True:
        print("\nPilih aksi:")
        print("1. Tambah mahasiswa")
        print("2. Tampilkan daftar mahasiswa")
        print("3. Perbarui data mahasiswa")
        print("4. Hapus mahasiswa")
        print("0. Keluar")
        pilihan = input("Masukkan pilihan: ")
        if pilihan == "1":
            tambah_mahasiswa()
        elif pilihan == "2":
            tampilkan_mahasiswa()
        elif pilihan == "3":
            perbarui_mahasiswa()
        elif pilihan == "4":
            hapus_mahasiswa()
        elif pilihan == "0":
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()
