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
4. Program akan mengambil nama secara acak dari `data_list` berdasarkan indeksnya dan menyimpannya dalam `list_nama`. Proses ini berulang hingga `list_nama` mencapai 4 nama, kemudian kelompok dicetak dan `list_nama` dikosongkan untuk nama-nama berikutnya.
5. Jika pada akhir proses ada sisa nama di `list_nama` (kurang dari 4), kelompok terakhir akan tetap terbentuk dan ditampilkan.
6. Hasil pembentukan kelompok akan ditampilkan ke layar.
7. Jika tidak ada nama yang dimasukkan, program akan menampilkan pesan "Tidak terbentuk kelompok karena tidak ada nama yang dimasukkan." 



CONTOH PENGGUNAAN

Contoh Input:
Masukkan nama (ketik 'stop' untuk menghentikan proses): Budi
Masukkan nama (ketik 'stop' untuk menghentikan proses): Ahmad
Masukkan nama (ketik 'stop' untuk menghentikan proses): Caca
Masukkan nama (ketik 'stop' untuk menghentikan proses): Putra
Masukkan nama (ketik 'stop' untuk menghentikan proses): Putri
Masukkan nama (ketik 'stop' untuk menghentikan proses): Aisyah
Masukkan nama (ketik 'stop' untuk menghentikan proses): Kalia
Masukkan nama (ketik 'stop' untuk menghentikan proses): stop

Contoh Output:
Hasil input data nama orang (masih sesuai urutan input): ['Budi', 'Ahmad', 'Caca', 'Putra', 'Putri', 'Aisyah', 'Kalia']

Hasil Pembentukan Kelompok:
Kelompok 1 = ['Aisyah', 'Putri', 'Budi', 'Kalia']
Kelompok 2 = ['Ahmad', 'Putra', 'Caca']

Contoh Output (Tanpa Input):
Masukkan nama (ketik 'stop' untuk menghentikan proses): stop

Hasil input data nama orang (masih sesuai urutan input): [] 

Hasil Pembentukan Kelompok:
Tidak terbentuk kelompok karena tidak ada nama yang dimasukkan. 



KUSTOMISASI JUMLAH ANGGOTA PER KELOMPOK
Anda dapat mengubah jumlah anggota per kelompok dengan memodifikasi nilai `4` pada dua bagian kode berikut:

Bagian 1:
if len(list_nama) == 4:
    print(f"Kelompok {nomor_kelompok} = {list_nama}")
    list_nama = []
    nomor_kelompok += 1

Bagian 2:
if len(list_nama) < 4 and len(list_nama) > 0:
    print(f"Kelompok {nomor_kelompok} = {list_nama}")

Contoh:
• Untuk membuat kelompok berisi 3 orang, ubah nilai 4 menjadi 3 di kedua bagian.
• Untuk membuat kelompok berisi 5 orang, ubah nilai 4 menjadi 5 di kedua bagian.