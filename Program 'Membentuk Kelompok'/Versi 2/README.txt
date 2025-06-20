==============================
 PROGRAM PEMBENTUKAN KELOMPOK
==============================

DESKRIPSI PROGRAM
Program Python ini berfungsi untuk membagi nama-nama yang diinput oleh pengguna menjadi beberapa kelompok secara acak. Secara default, setiap kelompok akan berisi 4 nama.



PERSYARATAN
- Python 3.x
- Tidak memerlukan library tambahan



CARA KERJA
1. Pengguna menginput nama satu per satu.
2. Ketik 'stop' untuk menghentikan proses input nama.
3. Nama-nama yang diinput akan disimpan dalam list `data_list`.
4. Program akan mengambil nama dari `data_list` secara acak berdasarkan indeksnya.
5. Nama yang diambil secara acak akan disimpan dalam `list_nama` hingga semua nama dari `data_list` terambil.
6. `list_nama` kemudian akan dibagi menjadi kelompok-kelompok kecil, masing-masing berisi 4 nama.
7. Jika total nama bukan kelipatan 4, kelompok terakhir akan berisi sisa nama.
8. Hasil pembentukan kelompok akan ditampilkan ke layar.
9. Jika tidak ada nama yang dimasukkan, program akan menampilkan pesan "Tidak terbentuk kelompok karena tidak ada nama yang dimasukkan." 



CONTOH PENGGUNAAN

Contoh Input:
Masukkan nama (ketik 'stop' untuk menghentikan proses): Budi
Masukkan nama (ketik 'stop' untuk menghentikan proses): Ahmad
Masukkan nama (ketik 'stop' untuk menghentikan proses): Caca
Masukkan nama (ketik 'stop' untuk menghentikan proses): Putri
Masukkan nama (ketik 'stop' untuk menghentikan proses): Putra
Masukkan nama (ketik 'stop' untuk menghentikan proses): Beni
Masukkan nama (ketik 'stop' untuk menghentikan proses): Aisyah
Masukkan nama (ketik 'stop' untuk menghentikan proses): stop

Contoh Output:
Hasil input data nama orang (masih sesuai urutan input): ['Budi', 'Ahmad', 'Caca', 'Putri', 'Putra', 'Beni', 'Aisyah']

Hasil Pembentukan Kelompok:
Kelompok 1 = ['Putri', 'Ahmad', 'Putra', 'Budi']
Kelompok 2 = ['Caca', 'Aisyah', 'Beni']

Contoh Output (Tanpa Input):
Masukkan nama (ketik 'stop' untuk menghentikan proses): stop

Hasil input data nama orang (masih sesuai urutan input): [] 

Hasil Pembentukan Kelompok:
Tidak terbentuk kelompok karena tidak ada nama yang dimasukkan. 



KUSTOMISASI JUMLAH ANGGOTA PER KELOMPOK
Anda dapat mengubah jumlah anggota per kelompok dengan memodifikasi nilai `4` pada baris kode berikut:
`kelompok_nama = [data_list[i:i+4] for i in range(0,len(data_list),4)]`

Contoh:
- Untuk membuat kelompok berisi 3 orang, ubah menjadi:
  `kelompok_nama = [data_list[i:i+3] for i in range(0,len(data_list),3)]` 
- Untuk membuat kelompok berisi 5 orang, ubah menjadi:
  `kelompok_nama = [data_list[i:i+5] for i in range(0,len(data_list),5)]` 