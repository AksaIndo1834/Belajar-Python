
# 🧮 PROGRAM KALKULATOR SEDERHANA

## 📌 Deskripsi Program
Program Python ini adalah kalkulator sederhana untuk melakukan operasi matematika pada dua bilangan.  
Operasi yang tersedia:
- Penjumlahan (`+`)
- Pengurangan (`-`)
- Perkalian (`x`)
- Pembagian (`/`)



## 🛠️ Persyaratan
- Python 3.x
- Tidak memerlukan library tambahan



## ▶️ Cara Menjalankan

### 💻 Secara Offline
1. Buka **Command Prompt (CMD)** atau aplikasi text editor (VS Code, Notepad++, dsb).
2. Jika melalui CMD, arahkan ke lokasi file Python:  
   ```bash
   cd D:\Latihan\Python
   ```
3. Jalankan program dengan:
   ```bash
   python kalkulator_sederhana.py
   ```
4. Jika pakai text editor, cukup tekan tombol **"Run"**.

### 🌐 Secara Online
1. Buka salah satu situs berikut:
   - [replit.com](https://replit.com)
   - [Programiz Online Python Compiler](https://www.programiz.com/python-programming/online-compiler)
2. Salin-tempel isi file Python ke editor online.
3. Klik **Run**.



## ⚙️ Cara Kerja Program
1. User memasukkan dua angka.
2. Memilih operasi: `+`, `-`, `x`, atau `/`.
3. Program menghitung dan menampilkan hasilnya.
4. Jika pembagian dengan 0 → akan muncul pesan error.
5. Jika operasi tidak dikenali → muncul pesan error.

📝 *Catatan: Setelah satu proses perhitungan, program akan langsung berhenti.*



## 🔍 Contoh Input/Output
```
Masukkan angka pertama: 1  
Masukkan angka kedua: 2  
Masukkan operasi (+ (tambah), - (kurang), x (kali), / (bagi)): +

Hasil operasi = 3.0
```

### ❗ Pembagian dengan nol:
```
Masukkan angka pertama: 1  
Masukkan angka kedua: 0  
Masukkan operasi (+ (tambah), - (kurang), x (kali), / (bagi)): /

Error: Bilangan tidak bisa dibagi dengan angka nol.
```

### ❗ Operasi tidak dikenali:
```
Masukkan angka pertama: 1  
Masukkan angka kedua: 2  
Masukkan operasi (+ (tambah), - (kurang), x (kali), / (bagi)): #

Operasi # tidak dikenali. Silahkan gunakan +, -, x, atau /.
```
