import os, platform, time, datetime
from urllib.request import urlopen

# menentukan dimana file daftar anggota
anggota = urlopen('https://raw.githubusercontent.com/tantowijh/\
Tugas-Akhir-S1-DasProg/main/Data/anggota.txt')
# menentukan dimana file daftar obat
dftr_obat = urlopen('https://raw.githubusercontent.com/tantowijh/\
Tugas-Akhir-S1-DasProg/main/Data/daftarobat.txt')

# inisiasi spasi, baris, dan garis
space = 72; newline = '\n'; nama = ''
baris1 = "="*space; baris2 = "-"*space

# inisiasi warna dengan kode ANSII
hitam = '\033[0m'; htebal = '\033[1;30m'; hijau = '\033[1;92m'
jtipis = '\033[0;92m'; biru = '\033[34m'; merah = '\033[91m'

# Variable untuk menyimpan obat yang dibeli
daftar_obat = []
# Variable untuk menyimpan biaya obat
total_obat = []

# Mengubah hari ke bahasa Indonesia
days = {"Sunday":"Minggu","Monday":"Senin", "Tuesday":"Selasa", "Wednesday": "Rabu", 
        "Thursday":"Kamis", "Friday":"Jum'at","Saturday":"Sabtu"}
def day(x): hari = days[x]; return hari

# Menentukan waktu pembelian
date = day(datetime.datetime.now().strftime("%A")) \
    + datetime.datetime.now().strftime(", %d-%b-%Y (%H:%M)")

# Fungsi untuk menghapus layar terminal
def clearscreen():
    if platform.system() == "Windows": os.system("cls") 
    else: os.system("clear")

# Daftar Obat dan harga produk
"""Menyimpan table Obat dan Harga menggunakan Dictionary"""
penyimpanan = {}
def reg_info():
    angka = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")
    for line in dftr_obat:
        (info, harga) = line.rstrip().decode('utf-8').split(":")
        if not harga.endswith(angka):
            harga = ''.join(filter(str.isdigit, harga))
        penyimpanan[info] = int(harga)

def header_anggota(x, y):
    """Membuat header untuk daftar obat tersedia dan pembayaran obat"""
    print(baris1)
    print(x.center(space))
    print("     _    _   _  ____  ____  ___ _____  _     ".center(space))
    print("    / \  | \ | |/ ___|/ ___|/ _ \_   _|/ \    ".center(space))
    print("   / _ \ |  \| | |  _| |  _| | | || | / _ \   ".center(space))
    print("  / ___ \| |\  | |_| | |_| | |_| || |/ ___ \  ".center(space))
    print(" /_/   \_\_| \_|\____|\____|\___/ |_/_/   \_\ ".center(space))
    print("                                              ".center(space))
    print(y.center(space))
    print(baris1)

def daftar_anggota():
  no_agt = 1
  spasi_agt = ' '*27
  header_anggota("Daftar".upper(),"Kelompok 3".upper())
  print(f'No Nama \t\t\t NIM \t\t Kelas')
  print(baris2)
  for line in anggota:
    try:
      nama, nim, kelas = line.rstrip().decode('utf-8').split(",")
      print(f'{no_agt}) {nama} {spasi_agt[:-len(nama)]} {nim} \t{kelas}')
      no_agt += 1
    except ValueError: continue
  print(baris2)