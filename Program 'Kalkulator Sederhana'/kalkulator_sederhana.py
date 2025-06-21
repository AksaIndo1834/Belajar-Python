# ===== LATIHAN PERCABANGAN LOGIKA =====
# Tugas: Buat kalkulator sederhana - operasi antara dua angka. Alur programnya:
#        1) User akan meng-input dua angka dan sebuah operasi (+,-,x,/)
#        2) Tergantung dari operasi yang diinput user, program akan melakukan operasi pada kedua angka sesuai operasi yang di-input user

print(" KALKULATOR SEDERHANA ".center(50,"="))

input_angka_pertama = float(input("Masukkan angka pertama: "))
input_angka_kedua = float(input("Masukkan angka kedua: "))
input_operasi = input("Masukkan operasi (+ (tambah), - (kurang), x (kali), / (bagi)): ").lower().strip()

if input_operasi == "+":
    print(f"Hasil operasi = {input_angka_pertama + input_angka_kedua}")
elif input_operasi == "-":
    print(f"Hasil operasi = {input_angka_pertama - input_angka_kedua}")
elif input_operasi == "x":
    print(f"Hasil operasi = {input_angka_pertama * input_angka_kedua}")
elif input_operasi == "/":
    if input_angka_kedua == 0:
        print(f"Error: Bilangan tidak bisa dibagi dengan angka nol.")
    else:
        print(f"Hasil operasi = {input_angka_pertama / input_angka_kedua}")
else:
    print(f"Operasi {input_operasi} tidak dikenali. Silahkan gunakan +, -, x, atau /.")