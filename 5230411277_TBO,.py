class Debitur:
    def __init__(self, ktp, nama, limit):
        self.ktp = ktp  
        self.nama = nama
        self._limit = limit

    def tampil(self):
        print(f"No. KTP: {self.ktp}, Nama: {self.nama}, Limit Pinjaman: {self._limit}")

class Pinjaman:
    def __init__(self, nama, pinjaman, bunga, bulan):
        self.nama = nama
        self.pinjaman = pinjaman
        self.bunga = bunga
        self.bulan = bulan       

    def tampil(self):
        print(f"Nama: {self.nama} Pinjaman: {self.pinjaman} Bunga: {self.bunga}% Waktu: {self.bulan} bulan")

def tambah_debitor(debtors):
    try:
        ktp = int(input("Masukkan Nomer KTP Baru: "))
        
        if any(debitor.ktp == ktp for debitor in debtors):
            print("No. KTP sudah ada. Validasi gagal.")
            return
        
        nama = input("Masukkan Nama Baru: ")
        limit = int(input("Masukkan Limit Pinjaman baru: "))
        new_debitor = Debitur(ktp, nama, limit)
        debtors.append(new_debitor)
        print("Debitur berhasil ditambahkan.")
    except ValueError:
        print("Input tidak valid. Pastikan KTP dan Limit adalah angka.")

def tampilkan_debitur(debtors):
    if not debtors:
        print("Tidak ada debitur.")
    else:
        for debitur in debtors:
            debitur.tampil()

def cari_debitur(debtors):
    pilihan = input("Cari berdasarkan (1) No. KTP atau (2) Nama? ")
    
    if pilihan == "1":
        try:
            ktp = int(input("Masukkan No. KTP yang dicari: "))
            found = next((d for d in debtors if d.ktp == ktp), None)
            if found:
                found.tampil()
            else:
                print("Debitur tidak ditemukan.")
        except ValueError:
            print("Input tidak valid. Pastikan KTP adalah angka.")
    
    elif pilihan == "2":
        nama = input("Masukkan Nama yang dicari: ")
        found_debitur = [d for d in debtors if nama.lower() in d.nama.lower()]
        if found_debitur:
            for debitur in found_debitur:
                debitur.tampil()
        else:
            print("Debitur tidak ditemukan.")
    else:
        print("Pilihan tidak valid.")

def tambah_pinjaman(loans):
    try:
        pinjam = input("Masukkan Nama: ")
        jumlah = int(input("Masukkan Jumlah Pinjaman: "))
        bunga = int(input("Masukkan Suku Bunga: "))
        lmit = int(input("Masukkan Limit Waktu dalam Bulan: "))
        new_loan = Pinjaman(pinjam, jumlah, bunga, lmit)
        loans.append(new_loan)
        print("Pinjaman berhasil ditambahkan.")
    except ValueError:
        print("Input tidak valid. Pastikan Jumlah Pinjaman, Bunga, dan Limit adalah angka.")

def tampilkan_pinjaman(loans):
    if not loans:
        print("Tidak ada pinjaman.")
    else:
        for loan in loans:
            loan.tampil()

def main():
    debtors = []
    loans = []
    
    while True:
        print("======Menu Utama======")
        print("1. Menu Kelola Debitur")
        print("2. Menu Pinjaman")
        print("0. Keluar")
        pilih = input("Pilih Menu di atas: ")
        
        if pilih == "1":
            while True:
                print("======Menu Kelola Debitur")
                print("1. Tampilkan Semua Debitur")
                print("2. Cari Debitur")
                print("3. Tambah Debitur")
                print("4. Kembali ke Menu Utama")
                pilihMenu = input("Pilih Menu di Atas: ")
                
                if pilihMenu == "1":
                    tampilkan_debitur(debtors)

                elif pilihMenu == "2":
                    cari_debitur(debtors)

                elif pilihMenu == "3":
                    tambah_debitor(debtors)

                elif pilihMenu == "4":
                    break

        elif pilih == "2":
            while True:
                print("======Menu Pinjaman======")
                print("1. Tambah Pinjaman")
                print("2. Tampilkan Pinjaman")
                print("3. Kembali ke Menu Utama")
                pilihMenu = input("Pilih Menu di Atas: ")
                
                if pilihMenu == "1":
                    tambah_pinjaman(loans)

                elif pilihMenu == "2":
                    tampilkan_pinjaman(loans)

                elif pilihMenu == "3":
                    break

        elif pilih == "0":
            print("Anda Keluar Program")
            break
        else:
            print("Pilihan Tidak Valid")

main()
