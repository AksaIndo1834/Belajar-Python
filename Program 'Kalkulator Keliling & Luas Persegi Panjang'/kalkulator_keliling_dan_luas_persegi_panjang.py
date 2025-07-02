import os

# Fungsi untuk menampilkan judul program
def judul_program():
    '''Menampilkan Judul Program'''
    os.system("cls" if os.name == "nt" else "clear")

    print("="*35)
    print("PROGRAM PENGHITUNG".center(34))
    print("KELILING DAN LUAS PERSEGI PANJANG".center(35))
    print("="*35)


# Fungsi untuk menampilkan menu pilihan
def menu():
    '''Menampilkan Menu Pilihan'''
    print("Silahkan pilih satu di antara pilihan-pilihan berikut.")
    print("1 -> Hitung Keliling Persegi Panjang")
    print("2 -> Hitung Luas Persegi Panjang")
    print("3 -> Hitung Keliling dan Luas Persegi Panjang")
    print("4 -> Akhiri Program")

    pilihan = input("Pilihan Anda: ").lower().strip()

    while pilihan not in ["1","2","3","4"]:
        print(f"\nPilihan tidak valid. Silahkan masukkan pilihan yang tersedia.")
        pilihan = input("Pilihan Anda: ").lower().strip()
    
    print(f"\n{"-"*80}\n{"-"*80}\n")
    return pilihan


def input_panjang_dan_lebar():
    '''Menerima Input Nilai Panjang dan Lebar Persegi Panjang'''
    panjang = float(input("Masukkan nilai panjang: "))
    lebar = float(input("Masukkan nilai lebar: "))

    return panjang,lebar


# Fungsi untuk menghitung keliling persegi panjang
def hitung_keliling(panjang,lebar):
    '''Menghitung Keliling Persegi Panjang'''
    hasil = 2*(panjang + lebar)
    return f"\nKeliling persegi panjang = {hasil:.2f}"


# Fungsi untuk menghitung luas persegi panjang
def hitung_luas(panjang,lebar):
    '''Menghitung Luas Persegi Panjang'''
    hasil = panjang*lebar
    return f"\nLuas persegi panjang = {hasil:.2f}"


# Fungsi untuk masuk ke mode menghitung keliling dan luas persegi panjang
def hitung_keliling_dan_luas(panjang,lebar):
    '''Menghitung Keliling dan Luas Persegi Panjang'''
    hasil_keliling = 2*(panjang + lebar)
    hasil_luas = panjang*lebar
    
    return f"\nKeliling persegi panjang = {hasil_keliling:.2f} \nLuas persegi panjang = {hasil_luas:.2f}"


# Fungsi untuk menanyakan apakah pengguna ingin melanjutkan perhitungan atau tidak
def lanjut_lagi_atau_tidak():
    '''Mengambil Input User Terkait Keputusan untuk Lanjut Menghitung atau Tidak'''
    print(f"•\n•\n•")
    lanjut_atau_tidak = input("Apakah Anda ingin melanjutkan perhitungan lagi (ya/tidak)? ").lower().strip()

    while lanjut_atau_tidak not in ["ya","tidak"]:
        print(f"\nInput tidak valid.")
        lanjut_atau_tidak = input("Apakah Anda ingin melanjutkan perhitungan lagi (ya/tidak)? ").lower().strip()

    return lanjut_atau_tidak



# Program utama  
judul_program() 
pilihan_user = menu()

while True:
    if pilihan_user == "4":
        break
    else:
        panjang,lebar = input_panjang_dan_lebar()

        if pilihan_user == "1":
            print(hitung_keliling(panjang,lebar))
        elif pilihan_user == "2":
            print(hitung_luas(panjang,lebar))
        elif pilihan_user == "3":
            print(hitung_keliling_dan_luas(panjang,lebar))


    isLanjut = lanjut_lagi_atau_tidak()
    if isLanjut == "ya":
        print(f"•\n•\n•")
        continue

    elif isLanjut == "tidak":
        print(f"\n{"-"*80}\n{"-"*80}\n")
        pilihan_user = menu()
        
    
print("Program Selesai. Terima kasih telah menggunakan program ini.")
input('Tekan tombol "Enter" untuk mengakhiri program.')