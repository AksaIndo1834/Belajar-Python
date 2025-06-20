print(" PROGRAM PEMBENTUKAN KELOMPOK ".center(70,"="))

import random as rd

# Kode utama untuk menginput nama dan menyimpannya dalam list 'data_list'
data_list = []      # Input nama disimpan di sini

while True:
    input_nama = input("Masukkan nama (ketik 'stop' untuk menghentikan proses): ")
    if input_nama.lower().strip() == "stop":        # Kode untuk menghentikan proses
        print()
        break
    
    data_list.append(input_nama)                    # Input nama akan ditambahkan ke dalam 'data_list' secara otomatis ketika user menginput nama
    
print(f"Hasil input data nama orang (masih sesuai urutan input): {data_list}\n")


# Kode utama untuk membentuk kelompok secara acak
list_nama = []
range_nilai_i = len(data_list)

while True:
    if len(data_list) == 0:                         # Kode untuk menghentikan proses jika tidak ada nama lagi di 'data_list'
        print()
        break

    data_baru = data_list.pop(rd.randint(0,(len(data_list)-1)))         # Mengambil nama secara acak dari 'data_list' dan menghapusnya dari list tersebut   
    list_nama.append(data_baru)

kelompok_nama = [list_nama[i:i+4] for i in range(0,range_nilai_i,4)]    # Membentuk kelompok dengan jumlah maksimal nama sesuai dengan yang di-set


# Kode utama untuk menampilkan hasil pembentukan kelompok
print(f"Hasil Pembentukan Kelompok:")
if len(kelompok_nama) == 0:
    print("Tidak terbentuk kelompok karena tidak ada nama yang dimasukkan.")
   
else:
    for index,data in enumerate(kelompok_nama):
        print(f"Kelompok {index+1} = {data}")


print()
print("PROGRAM SELESAI") 