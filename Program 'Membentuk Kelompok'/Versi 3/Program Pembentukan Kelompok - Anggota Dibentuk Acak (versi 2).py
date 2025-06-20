print(" PROGRAM PEMBENTUKAN KELOMPOK ".center(70,"="))

import random as rd

ada_input = False   # Penanda apakah ada input nama dari user


# Kode untuk meng-input data nama orang
data_list = []      # List untuk menyimpan data input nama orang    

while True:
    input_nama = input("Masukkan nama (ketik 'stop' untuk menghentikan proses): ")
    
    if input_nama.lower().strip() == "stop":                       # Kode untuk menghentikan proses
        print()
        break
    
    data_list.append(input_nama)                                   # Item data_list akan bertambah otomatis ketika user meng-input data
    ada_input = True                                               # Penanda bahwa ada input nama dari user

print(f"Hasil input data nama orang (masih sesuai urutan input): {data_list}\n")    


# Kode untuk membentuk kelompok secara acak
list_nama = []
nomor_kelompok = 1

print(f"Hasil Pembentukan Kelompok:")
while True:
    if len(data_list) == 0:                                        # Proses akan berakhir jika 'list_nama' kosong (tidak ada item)
        break
    
    data_baru = data_list.pop(rd.randint(0,(len(data_list)-1)))    # Mengambil data secara acak dari 'data_list' dan menghapusnya dari list tersebut
    list_nama.append(data_baru)                                     

    if len(list_nama) == 4:                                        # Jika jumlah nama dalam 'list_nama' sudah mencapai target, maka kelompok akan dicetak, lalu 'list_nama' akan dikosongkan kembali untuk diisi dengan nama-nama baru
        print(f"Kelompok {nomor_kelompok} = {list_nama}")
        list_nama = []              
        nomor_kelompok += 1


# Kode untuk menampilkan sisa nama yang belum terbentuk kelompok
if len(list_nama) < 4 and len(list_nama) > 0:              
    print(f"Kelompok {nomor_kelompok} = {list_nama}")


# Kode untuk menampilkan output jika pada awal proses tidak ada nama yang diinput
if ada_input == False:
    print("Tidak terbentuk kelompok karena tidak ada nama yang dimasukkan.")

print()
print("PROGRAM SELESAI")