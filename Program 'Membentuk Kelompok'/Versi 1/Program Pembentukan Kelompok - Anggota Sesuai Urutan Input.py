data_list = []          # Input nama disimpan di sini


# Program Pembentukan Kelompok - Anggota Sesuai Urutan Input
# Program ini akan meminta input nama dari pengguna dan membentuk kelompok berdasarkan urutan input.
while True:
    input_nama = input("Masukkan nama (ketik 'stop' untuk menghentikan proses): ")
    if input_nama.lower().strip() == "stop":
        print()
        break
    
    data_list.append(input_nama)

print(f"Daftar nama yang telah dimasukkan: {data_list} (jumlah: {len(data_list)} nama)")
print()


# Membagi data_list menjadi bebarapa kelompok dan mengatur banyak nama dalam satu kelompok
kelompok_nama = [data_list[i:i+4] for i in range(0,len(data_list),4)]


# Menampilkan hasil pembentukan kelompok
print(f"Hasil Pembentukan Kelompok:")

print(kelompok_nama)
if len(kelompok_nama) == 0:
    print("Tidak terbentuk kelompok karena tidak ada nama yang dimasukkan.")
else:
    for index,data in enumerate(kelompok_nama):
        print(f"Kelompok {index+1}: {data}")


print()
print("PROGRAM SELESAI")