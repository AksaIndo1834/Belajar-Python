import tkinter as tk
import random


# ========== UTILITAS DASAR ==========

def hapus_pesan_setelah_delay(window, label, delay=2000):
    window.after(delay, lambda: label.configure(text=""))


def ambil_daftar_nama(kotak):
    isi = kotak.get("1.0", tk.END).strip().split("\n")
    return [nama.strip() for nama in isi if nama.strip() != ""]


def perbarui_kotak_nama(kotak, daftar_nama):
    kotak.config(state="normal")
    kotak.delete("1.0", tk.END)
    for nama in daftar_nama:
        kotak.insert(tk.END, nama + "\n")
    kotak.config(state="disabled")


def acak_nama(nama_list):
    nama_acak = nama_list[:]
    random.shuffle(nama_acak)
    return nama_acak


# ========== VALIDASI ==========

def validasi_nama(nama, daftar_nama):
    if not nama:
        return False, "Input tidak boleh kosong"
    elif nama in daftar_nama:
        return False, "Nama sudah ada dalam daftar"
    return True, "Nama valid"


def validasi_hapus(nama, daftar_nama):
    if not nama:
        return False, "Input tidak boleh kosong"
    elif nama not in daftar_nama:
        return False, "Nama tidak ada dalam daftar"
    return True, "Nama ditemukan dan akan dihapus"


def validasi_input_angka(input_angka):
    try:
        angka = int(input_angka)
        if angka < 2:
            return False, "Angka harus ≥ 2"
        return True, "Angka valid"
    except ValueError:
        return False, "Input bukan angka valid"


# ========== FUNGSI UTAMA ==========

def tambah_nama(window, /, *, namaOrang, kotakDaftarNama, pesanSetelahInput):
    nama = namaOrang.get().strip()
    daftar_nama = ambil_daftar_nama(kotakDaftarNama)

    valid, pesan = validasi_nama(nama, daftar_nama)
    if valid:
        daftar_nama.append(nama)
        perbarui_kotak_nama(kotakDaftarNama, daftar_nama)
        pesanSetelahInput.config(text="Nama berhasil ditambahkan ke daftar", fg="green")
    else:
        pesanSetelahInput.config(text=pesan, fg="red")

    namaOrang.set("")
    hapus_pesan_setelah_delay(window, pesanSetelahInput)


def hapus_nama(window, /, *, namaOrang, kotakDaftarNama, pesanSetelahInput):
    nama = namaOrang.get().strip()
    daftar_nama = ambil_daftar_nama(kotakDaftarNama)

    valid, pesan = validasi_hapus(nama, daftar_nama)
    if valid:
        daftar_baru = [i for i in daftar_nama if i != nama]
        perbarui_kotak_nama(kotakDaftarNama, daftar_baru)
        pesanSetelahInput.config(text="Nama berhasil dihapus dari daftar", fg="green")
    else:
        pesanSetelahInput.config(text=pesan, fg="red")

    namaOrang.set("")
    hapus_pesan_setelah_delay(window, pesanSetelahInput)


def bentuk_kelompok(window, /, *, banyakAnggota, kotakDaftarNama, kotakHasilKelompok, pesanSetelahInput):
    input_anggota = banyakAnggota.get().strip()
    valid, pesan = validasi_input_angka(input_anggota)

    if not input_anggota:
        pesanSetelahInput.config(text="Input tidak boleh kosong", fg="red")
    elif not valid:
        pesanSetelahInput.config(text=pesan, fg="red")
    else:
        pesanSetelahInput.config(text="Input angka diterima", fg="green")
        kotakHasilKelompok.config(state="normal")
        kotakHasilKelompok.delete("1.0", tk.END)

        daftar_nama = ambil_daftar_nama(kotakDaftarNama)
        if not daftar_nama:
            kotakHasilKelompok.insert(tk.END, f"Tidak terbentuk kelompok karena tidak ada nama di dalam daftar nama.")
        else:
            jumlah_per_kelompok = int(input_anggota)
            nama_acak = acak_nama(daftar_nama)

            hasil_kelompok = [
                nama_acak[i:i + jumlah_per_kelompok]
                for i in range(0, len(nama_acak), jumlah_per_kelompok)
            ]

            for idx, anggota in enumerate(hasil_kelompok, 1):
                kotakHasilKelompok.insert(tk.END, f"Kelompok {idx}: {', '.join(anggota)}\n")

            
    kotakHasilKelompok.config(state="disabled")
    banyakAnggota.set("")
    hapus_pesan_setelah_delay(window, pesanSetelahInput)