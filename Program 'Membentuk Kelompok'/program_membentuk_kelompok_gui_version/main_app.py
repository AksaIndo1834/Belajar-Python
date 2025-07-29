import tkinter as tk
from tkinter import ttk

from button_command_module import *

# ====== WINDOW UTAMA ======
window = tk.Tk()
window.geometry("800x600")
window.configure(bg="#ADD8E6")
window.title("Program Membuat Kelompok")



# ====== FRAME SELURUH WIDGETS ======
border_frame_utama = tk.Frame(window, bg="#FFFFFF")
border_frame_utama.pack(padx=30, pady=30, fill="both", expand=True)

frame_utama = tk.Frame(border_frame_utama, bg="#97BBC6")
frame_utama.pack(padx=5, pady=5, fill="both", expand=True)



# ====== STRING VAR ======
var_input_nama = tk.StringVar()
var_hapus_nama = tk.StringVar()
var_banyak_anggota = tk.StringVar()



# ====== FRAME INPUT-HAPUS NAMA ======
frame_input_hapus_nama = tk.Frame(frame_utama, bg="#97BBC6")
frame_input_hapus_nama.grid(column=0, row=0, sticky="we")


# ====== WIDGET INPUT NAMA ======
label_input_nama = tk.Label(frame_input_hapus_nama, text="Masukkan Nama ke Dalam Daftar:", fg="#FFFFFF", font=("Comic Sans MS", 11, "bold"), justify="left", bg="#97BBC6")
label_input_nama.grid(column=0, row=0, padx=10, pady=(10,0), sticky="w")

entry_input_nama = ttk.Entry(frame_input_hapus_nama, textvariable=var_input_nama, width=30)
entry_input_nama.grid(column=0, row=1, padx=10, pady=(2,0), sticky="we")

tombol_input_nama = ttk.Button(
    frame_input_hapus_nama,
    text="Masukkan Nama",
    width=15,
    command=lambda: tambah_nama(window, namaOrang=var_input_nama, kotakDaftarNama=kotak_daftar2_nama, pesanSetelahInput=pesan_stlh_input))    # catatan: Jangan lupa tambahkan command nya

tombol_input_nama.grid(column=1, row=1, pady=(2,0))

pesan_stlh_input = tk.Label(frame_input_hapus_nama, text="", fg="#FFFFFF", font=("Calibri", 10), justify="left", bg="#97BBC6")
pesan_stlh_input.grid(column=0, row=2, padx=10, sticky="w")


# ====== WIDGET HAPUS NAMA ======
label_hapus_nama = tk.Label(frame_input_hapus_nama, text="Hapus Nama dari Daftar:", fg="#FFFFFF", font=("Comic Sans MS", 11, "bold"), justify="left", bg="#97BBC6")
label_hapus_nama.grid(column=0, row=3, padx=10, pady=(10,0), sticky="w")

entry_hapus_nama = ttk.Entry(frame_input_hapus_nama, textvariable=var_hapus_nama, width=30)
entry_hapus_nama.grid(column=0, row=4, padx=10, pady=(2,0), sticky="we")

tombol_hapus_nama = ttk.Button(
    frame_input_hapus_nama,
    text="Hapus Nama",
    width=15,
    command=lambda: hapus_nama(window, namaOrang=var_hapus_nama, kotakDaftarNama=kotak_daftar2_nama, pesanSetelahInput=pesan_stlh_hapus))    # catatan: Jangan lupa tambahkan command nya

tombol_hapus_nama.grid(column=1, row=4, pady=(2,0))

pesan_stlh_hapus = tk.Label(frame_input_hapus_nama, text="", fg="#FFFFFF", font=("Calibri", 10), justify="left", bg="#97BBC6")
pesan_stlh_hapus.grid(column=0, row=5, padx=10, sticky="w")



# ====== FRAME DAFTAR-DAFTAR NAMA ======
frame_daftar2_nama = tk.Frame(frame_utama, bg="#97BBC6")
frame_daftar2_nama.grid(column=1, row=0, sticky="we")


# ====== WIDGET DAFTAR-DAFTAR NAMA ======
kotak_daftar2_nama = tk.Text(frame_daftar2_nama, width=40, height=9.5, state="disabled")
kotak_daftar2_nama.pack(padx=(60,10), pady=(10,0), fill="x", expand=True, anchor="nw")



# ====== FRAME BENTUK KELOMPOK ======
frame_bentuk_kelompok = tk.Frame(frame_utama, bg="#97BBC6")
frame_bentuk_kelompok.grid(column=0, row=1, sticky="we")


# ====== WIDGET BENTUK KELOMPOK ======
label_banyak_anggota = tk.Label(frame_bentuk_kelompok, text="Banyak Anggota per Kelompok:", fg="#FFFFFF", font=("Comic Sans MS", 11, "bold"), justify="left", bg="#97BBC6")
label_banyak_anggota.grid(column=0, row=0, padx=10, pady=(80,0), sticky="w")

entry_banyak_anggota = ttk.Entry(frame_bentuk_kelompok, textvariable=var_banyak_anggota, width=43)
entry_banyak_anggota.grid(column=0, row=1, padx=10, pady=(2,0), sticky="we")

tombol_banyak_anggota = ttk.Button(
    frame_bentuk_kelompok,
    text="Set Banyak Anggota",
    width=18,
    command=lambda: bentuk_kelompok(window, banyakAnggota=var_banyak_anggota, kotakDaftarNama=kotak_daftar2_nama, kotakHasilKelompok=kotak_hasil_kelompok, pesanSetelahInput=pesan_stlh_set_banyak_anggota))    # catatan: Jangan lupa tambahkan command nya

tombol_banyak_anggota.grid(column=1, row=1, pady=(2,0), sticky="w")

pesan_stlh_set_banyak_anggota = tk.Label(frame_bentuk_kelompok, text="", fg="#FFFFFF", font=("Calibri", 10), justify="left", bg="#97BBC6")
pesan_stlh_set_banyak_anggota.grid(column=0, row=2, padx=10, sticky="w")



# ====== FRAME HASIL KELOMPOK ======
frame_hasil_kelompok = tk.Frame(frame_utama, bg="#97BBC6")
frame_hasil_kelompok.grid(column=0, columnspan=2, row=2, sticky="nsew")

kotak_hasil_kelompok = tk.Text(frame_hasil_kelompok, state="disabled")
kotak_hasil_kelompok.grid(column=0, row=0, padx=10, pady=10, sticky="nsew")



# ====== CONFIGURE GRID ======
frame_utama.grid_columnconfigure(0, weight=1)
frame_utama.grid_columnconfigure(1, weight=3)
frame_utama.grid_rowconfigure(2, weight=3)

frame_input_hapus_nama.grid_columnconfigure(0, weight=1)

frame_bentuk_kelompok.grid_columnconfigure(0, weight=1)

frame_hasil_kelompok.grid_columnconfigure(0, weight=1)
frame_hasil_kelompok.grid_rowconfigure(0, weight=1)



# ====== KODE UNTUK WINDOW TETAP BERJALAN ======
window.mainloop()