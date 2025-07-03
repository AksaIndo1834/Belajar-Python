
# PROGRAM KALKULATOR KELILING DAN LUAS PERSEGI PANJANG

## 📌 Deskripsi Program
Program ini adalah program untuk menghitung keliling dan luas sebuah persegi panjang. User hanya perlu menginput nilai panjang dan lebar persegi panjang, lalu program akan
menghitung keliling dan luasnya berdasarkan input nilai yang diberikan.

Program juga dibuat interaktif. Di dalam program, terdapat menu yang berisi pilihan. User dapat memilih mode perhitungan (hal yang ingin dihitung) atau memilih untuk mengakhiri program.
Selain itu, ketika masuk ke salah satu mode perhitungan, user dapat menginput/memasukkan sendiri nilai panjang dan lebar persegi panjang yang diinginkan.



## 🛠️ Persyaratan
- Python 3.x
- Tidak memerlukan library tambahan



## ❗ Hal yang Perlu Diperhatikan
- Program belum bisa memvalidasi apakah input untuk nilai panjang dan lebar berupa angka atau bukan. Maka dari itu, pastikan berhati-hati saat menginput nilai panjang dan lebar
  (Program akan error dan berhenti seketika jika user menginput selain angka, termasuk spasi dan enter kosong).
- Gunakan tanda titik (.) sebagai tanda koma pada bilangan desimal.



## ▶️ Cara Menjalankan

### 🔹 Melalui Command Prompt (CMD) 
1. Buka Command Prompt (CMD)
2. Arahkan ke lokasi file Python. Semisal file berapa di **"D:\Latihan\Python"**, maka ketik:  
   ```cmd
   cd "D:\Latihan\Python"
   ```
   Cara mendapatkan lokasi file:
   1) Buka folder tempat file python berada, lalu klik kanan pada bagian yang dilingkari merah.
       ![Mendapatkan Lokasi File (step 1)](https://github.com/AksaIndo1834/gambar_untuk_github/blob/main/Gambar%20Keperluan%20Github/Cara%20Mendapatkan%20Lokasi%20File%20(Step%201).png)

   2) Pilih opsi yang dilingkari warna merah.
      ![Mendapatkan Lokasi File (step 2)](https://github.com/AksaIndo1834/gambar_untuk_github/blob/main/Gambar%20Keperluan%20Github/Cara%20Mendapatkan%20Lokasi%20File%20(Step%202).png)
3. Jalankan program dengan ketik:
   ```cmd
   python kalkulator_keliling_dan_luas_persegi_panjang.py
   ```

### 🔸 Melalui Aplikasi Code Editor
1. Buka aplikasi code editor, seperti:
   - Visual Studio Code (VS Code)
   - Notepad++
   - dan lain-lain
2. Salin-tempel (copy-paste) isi file Python ke aplikasi code editor
3. Klik "Run"



## ⚙️ Cara Kerja Program
1. Menu pilihan akan ditampilkan ketika program dijalankan.
2. User memilih satu dari pilihan-pilihan yang ada dengan cara menginput kode nomornya. User dapat memilih mode perhitungan (hal yang ingin dihitung) atau memilih untuk mengakhiri program.
   Berikut adalah tampilan menu pilihan:
    ```python
    Silahkan pilih satu di antara pilihan-pilihan berikut.
    1 -> Hitung Keliling Persegi Panjang
    2 -> Hitung Luas Persegi Panjang
    3 -> Hitung Keliling dan Luas Persegi Panjang
    4 -> Akhiri Program
    Pilihan Anda: [input_user]
    ```
3. Jika user memilih 1, 2, atau 3:
   - User diminta untuk menginput nilai panjang dan lebar persegi panjang
   - Program lalu menghitung keliling, luas, atau keduanya (tergantung dari pilihan user di menu pilihan), lalu hasil perhitungan ditampilkan ke layar.
   - Setelah perhitungan, user akan ditanyai oleh program apakah ingin lanjut melakukan perhitungan atau tidak.
   - Jika ingin lanjut, user akan tetap berada di mode perhitungan yang sama dan mengulangi proses (menginput nilai panjang dan lebar baru -> program menghitung -> Menampilkan hasil perhitungan).
   - Jika tidak ingin lanjut, user akan kembali ke menu pilihan sehingga user dapat memilih mode perhitungan lain atau mengakhiri program.
4. Jika user memilih pilihan 4:
   - Program akan menampilkan pesan terakhir.
   - User diberikan jeda sebelum program berakhir sehingga user dapat melihat kembali hasil perhitungan yang telah dilakukan.
   - Untuk menghentikan program, user hanya perlu menekan "Enter"
   - Setelah itu, program akan berhenti.



## 💡 Flowchart Program
![Flowchart program kalkulator keliling dan luas persegi panjang](https://github.com/AksaIndo1834/gambar_untuk_github/blob/main/Gambar%20Keperluan%20Github/Flowchart%20program%20'hitung%20keliling%20dan%20luas%20persegi%20panjang'.png?raw=true)

*__catatan:__*

Jika tulisan pada gambar sulit di baca, lakukan hal ini:
1. Klik kanan (jika menggunakan komputer) atau tekan-tahan (jika menggunakan handphone)
2. Pilih opsi "Open image in new tab". Akan terbuka tab baru berisi gambar tersebut
3. Buka tab tersebut. Di sana, Anda dapat melakukan *zoom in* atau *zoom out* pada gambar agar dapat melihat tulisannya dengan lebih jelas
