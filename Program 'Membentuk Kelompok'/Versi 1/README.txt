==============================
 PROGRAM PEMBENTUKAN KELOMPOK
==============================

DESKRIPSI PROGRAM
Program Python ini berfungsi untuk membagi nama-nama yang diinput oleh pengguna menjadi beberapa kelompok. Pembagian kelompok didasarkan pada urutan nama yang diinput. Secara default, setiap kelompok akan berisi 4 nama.



PERSYARATAN
- Python 3.x
- Tidak memerlukan library tambahan



CARA KERJA
1. Pengguna menginput nama satu per satu.
2. Ketik 'stop' untuk menghentikan proses input nama.
3. Nama-nama yang diinput akan disimpan dalam list `data_list`.
4. Program akan membagi list nama menjadi beberapa kelompok, di mana setiap kelompok berisi 4 anggota.
5. Jika total nama yang diinput bukan kelipatan 4, kelompok terakhir akan berisi sisa nama.
6. Hasil pembentukan kelompok akan ditampilkan ke layar.
7. Jika tidak ada nama yang dimasukkan, program akan menampilkan pesan "Tidak terbentuk kelompok karena tidak ada nama yang dimasukkan." 



CONTOH PENGGUNAAN

Contoh Input:
Masukkan nama (ketik 'stop' untuk menghentikan proses): Budi
Masukkan nama (ketik 'stop' untuk menghentikan proses): Ahmad
Masukkan nama (ketik 'stop' untuk menghentikan proses): Caca
Masukkan nama (ketik 'stop' untuk menghentikan proses): Putri
Masukkan nama (ketik 'stop' untuk menghentikan proses): Putra
Masukkan nama (ketik 'stop' untuk menghentikan proses): stop

Contoh Output:
Daftar nama yang telah dimasukkan: ['Budi', 'Ahmad', 'Caca', 'Putri', 'Putra'] (jumlah: 5 nama)

Hasil Pembentukan Kelompok:
[['Budi', 'Ahmad', 'Caca', 'Putri'], ['Putra']]
Kelompok 1: ['Budi', 'Ahmad', 'Caca', 'Putri']
Kelompok 2: ['Putra']

Contoh Output (Tanpa Input):
Masukkan nama (ketik 'stop' untuk menghentikan proses): stop

Daftar nama yang telah dimasukkan: [] (jumlah: 0 nama)

Hasil Pembentukan Kelompok:
[]
Tidak terbentuk kelompok karena tidak ada nama yang dimasukkan. 



KUSTOMISASI JUMLAH ANGGOTA PER KELOMPOK
Anda dapat mengubah jumlah anggota per kelompok dengan memodifikasi nilai `4` pada baris kode berikut:
`kelompok_nama = [data_list[i:i+4] for i in range(0,len(data_list),4)]`

Contoh:
- Untuk membuat kelompok berisi 3 orang, ubah menjadi:
  `kelompok_nama = [data_list[i:i+3] for i in range(0,len(data_list),3)]` 
- Untuk membuat kelompok berisi 5 orang, ubah menjadi:
  `kelompok_nama = [data_list[i:i+5] for i in range(0,len(data_list),5)]` 