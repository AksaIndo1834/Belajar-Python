# 🌡 PROGRAM KALKULATOR SEDERHANA

## 📌 Deskripsi Program
Program Python ini akan mengonversi suhu ke satuan lainnya. Program ini mendukung suhu dengan angka positif, negatif, dan desimal.  
Suhu yang tersedia untuk dikonversikan:
1. Celcius
2. Fahrenheit
3. Kelvin
4. Reamur


## ⚠ Perhatian bagi Pengguna
Program sangat sensitif terhadap salah ketik (typo) pada input. Jika terjadi salah ketik, program akan seketika error dan berhenti.

Contoh kasus salah ketik yang dapat membuat program error:
- Memasukkan input selain angka dan tanda positif/negatif (Pastikan tanda positif/negatif berada di depan angka dan menempel dengan angka).
- Menggunakan tanda koma (,) sebagai desimal (Gunakanlah titik sebagai desimalnya).



## 🛠️ Persyaratan
- Python 3.x
- Tidak memerlukan library tambahan



## ▶️ Cara Menjalankan

### 💻 Secara Offline
1. Buka **Command Prompt (CMD)** atau aplikasi text editor (VS Code, Notepad++, dsb).
2. Jika melalui CMD, arahkan ke lokasi file Python. Semisal file berapa di **"D:\Latihan\Python"**, maka ketik:  
   ```cmd
   cd D:\Latihan\Python
   ```
   Cara mendapatkan lokasi file:
   1) Buka folder tempat file python berada, lalu klik kanan pada bagian yang dilingkari merah.
       ![Mendapatkan Lokasi File (step 1)](https://github.com/AksaIndo1834/gambar_untuk_github/blob/main/Gambar%20Keperluan%20Github/Cara%20Mendapatkan%20Lokasi%20File%20(Step%201).png)

   2) Pilih opsi yang dilingkari warna merah.
      ![Mendapatkan Lokasi File (step 2)](https://github.com/AksaIndo1834/gambar_untuk_github/blob/main/Gambar%20Keperluan%20Github/Cara%20Mendapatkan%20Lokasi%20File%20(Step%202).png)
3. Jalankan program dengan ketik:
   ```cmd
   python konversi_suhu.py
   ```
4. Jika pakai text editor, program dapat dijalankan dengan klik tombol **"Run"**.

### 🌐 Secara Online
1. Buka salah satu situs berikut:
   - [replit.com](https://replit.com)
   - [Programiz Online Python Compiler](https://www.programiz.com/python-programming/online-compiler)
2. Salin-tempel (copy-paste) isi file Python ke editor online.
3. Klik **Run**.



## ⚙️ Cara Kerja Program
1. User memasukkan nilai suhu.
2. Secara berurutan, user memasukkan nilai suhu dalam Celcius, Fahrenheit, Kelvin, dan terakhir Reamur.
3. Pada masing-masing bagian, nilai suhu akan dikonversikan ke satuan lainnya.
   Sebagai gambaran:
   Setelah user memasukkan nilai suhu Celcius, program akan mengonversikan suhu Celcius ke Fahrenheit, Kelvin, dan Reamur serta menampilkan hasilnya. Selanjutnya, user menginput suhu Fahrenheit dan dikonversikan oleh program.
   Begitu seterusnya hingga Reamur. 


📝 *Catatan:* 
- Setelah proses konversi, program akan langsung berhenti.
- Gunakan titik (.) sebagai tanda koma pada angka desimal.



## 🔍 Contoh Input/Output
```python
========== KONVERSI SUHU ==========

Masukan nilai suhu dalam celcius = 0
Suhu celcius = 0.0 °C

Hasil konversi:
Suhu dalam Fahrenheit = 32.0 °F
Suhu dalam Kelvin = 273.0 K    
Suhu dalam Reamur = 0.0 °Re    

----------------------------------------

Masukan nilai suhu dalam fahrenheit = 0
Suhu fahrenheit = 0.0 °F

Hasil konversi:
Suhu dalam Celcius = -17.77777777777778 °C
Suhu dalam Kelvin = 255.22222222222223 K
Suhu dalam Reamur = -14.222222222222221 °Re

----------------------------------------

Masukan nilai suhu dalam kelvin = 0
Suhu kelvin = 0.0 K

Hasil konversi:
Suhu dalam Celcius = -273.0 °C
Suhu dalam Fahrenheit = -459.40000000000003 °F
Suhu dalam Reamur = -218.4 °Re

----------------------------------------

Masukan nilai suhu dalam reamur = 0
Suhu reamur = 0.0 °Re

Hasil konversi:
Suhu dalam Celcius = 0.0 °C
Suhu dalam Fahrenheit = 32.0 °F
Suhu dalam Kelvin = 273.0 K


**Konversi Selesai**
```
