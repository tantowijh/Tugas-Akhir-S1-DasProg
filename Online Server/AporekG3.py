import os, platform, time, datetime, requests

path = os.path.dirname(os.path.abspath(__file__)) + "/temp"
url = 'https://raw.githubusercontent.com/tantowijh/Tugas-Akhir-S1-DasProg/main/Data/'

# inisiasi spasi, baris, dan garis
spasi = 72; nl = '\n'; nama = ''
garis1 = "="*spasi; garis2 = "-"*spasi

# inisiasi warna dengan kode ANSII
hitam = '\033[0m'; htebal = '\033[1;30m'; hijau = '\033[1;92m'
jtipis = '\033[0;92m'; biru = '\033[34m'; merah = '\033[91m'

# Fungsi untuk menghapus layar terminal atau cmd
def clearscreen():
    if platform.system() == "Windows": os.system("cls") 
    else: os.system("clear")

def load_file():
  if not os.path.exists(path):
    os.mkdir(path)
  agt = requests.get(url + 'anggota.txt')
  obat = requests.get(url + 'daftarobat.txt')
  with open(path + "/anggota.txt", "wb") as f:
    f.write(agt.content)
  with open(path + "/daftarobat.txt", "wb") as f:
    f.write(obat.content)

clearscreen()
load_file()

def del_file():
  for name in os.listdir(path):
    if name.endswith(".txt"): os.remove(path+'/'+name)
  if path: os.rmdir(path)

# Menentukan waktu pembelian
def waktu():
    def day(x): 
        days = {"Sunday":"Minggu","Monday":"Senin", "Tuesday":"Selasa", "Wednesday": "Rabu", 
                "Thursday":"Kamis", "Friday":"Jum'at","Saturday":"Sabtu"}
        hari = days[x]; return hari
    date = 'Hari ' + day(datetime.datetime.now().strftime("%A")) \
    + datetime.datetime.now().strftime(", %d-%b-%Y, Jam (%H:%M)")
    return date

def daftar_anggota():
  no_agt = 1; spasi_agt = ' '*27
  # menentukan dimana file daftar anggota
  anggota = path + "/anggota.txt"
  print(f'No Nama \t\t\t NIM \t\t Kelas')
  print(garis2)
  with open(anggota, 'r') as agt:
    for line in agt:
      try: 
        nama, nim, kelas = line.rstrip().split(",")
        print(f'{no_agt}) {nama} {spasi_agt[:-len(nama)]} {nim} \t{kelas}')
        no_agt += 1
      except ValueError: continue
  print(garis2+nl)

# Daftar Obat dan harga produk
"""Menyimpan table Obat dan Harga menggunakan Dictionary"""
penyimpanan = {}
def reg_info():
    # menentukan dimana file daftar obat
    dftr_obat = path + "/daftarobat.txt"
    angka = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")
    with open(dftr_obat, 'r') as inf:
        for line in inf:
            (info, harga) = line.rstrip().split(":")
            if not harga.endswith(angka):
                harga = ''.join(filter(str.isdigit, harga))
            penyimpanan[info] = int(harga)

# informasi apotek
def header(x):
    """Membuat header untuk daftar obat tersedia dan pembayaran obat"""
    print('{}'.format(garis1+hijau))
    print(x.center(spasi))
    print("    _    ____   ___ _____ _____ _  __   ____ _____ ".center(spasi))
    print("   / \  |  _ \ / _ \_   _| ____| |/ /  / ___|___ / ".center(spasi))
    print("  / _ \ | |_) | | | || | |  _| | ' /  | |  _  |_ \ ".center(spasi))
    print(" / ___ \|  __/| |_| || | | |___| . \  | |_| |___) |".center(spasi))
    print("/_/   \_\_|    \___/ |_| |_____|_|\_\  \____|____/ ".center(spasi))
    print('{}{}{}'.format(nl+jtipis,"Jl. Kesuksesan Kita Bersama".center(spasi).title(), merah))
    print('{}{}'.format(waktu().center(spasi),hitam+nl+garis1))

# informasi barang
def info_obat():
    """Memuat informasi obat yang tersedia untuk memudahkan pembelian"""
    reg_info()
    print(f'{htebal + "Daftar Obat":65}{"Harga" + hitam}')
    print(garis2)
    no = 1
    for x, y in penyimpanan.items():
        print(f'{no:2}) {x:54}Rp.{y:,}')
        no += 1
    print(garis2)

# Variable untuk menyimpan obat yang dibeli
daftar_obat = []
# Variable untuk menyimpan biaya obat
total_obat = []

# Fungsi untuk menampilkan semua data
def show_data():
    """Menampilkan semua obat yang ada dalam keranjang Pelanggan
    
    *Menampilkan semua obat yang telah ditambahkan ke dalam keranjang 
    oleh pelanggan guna mempermudah untuk merubahnya atau untuk menghapusnya*
    """
    if len(daftar_obat)<=0:
        print('{}Daftar obat Anda{:34}Harga{}'.format(htebal,"",hitam+nl+garis2))
        print('{}Maaf keranjang Anda masih kosong...{:15}{}{}'.format(merah,"","0",hitam))
    else:
        print('{}Daftar obat Anda{:34}Harga{}'.format(htebal,"",hitam+nl+garis2))
        for index in range(len(daftar_obat)):
            print("{:2}) {:46}Rp.{:,}".format(index+1, daftar_obat[index], total_obat[index]))
    print(garis2+nl)

# Fungsi untuk menambah daftar obat
def insert_data():
    """Menambahkan obat ke dalam keranjang pelanggan"""  
    info_obat()
    while True:
        try:
            val = int(input("Apa yang ingin Anda beli hari ini? [0 ke Menu Utama] --> "))
            if val < 0 or val > len(penyimpanan):
                print('Kami mohon maaf obat itu {}tidak tersedia {}di apotek kami!'
                      .format(merah,hitam))
            elif val == 0: break
            else:
                obat = list(penyimpanan.keys())[val-1]
                if obat in penyimpanan:
                    while True:
                        try: banyak = int(input("Berapa banyak obat yang Anda mau? ")); break
                        except: print("Hanya angka!")
                    for b in range(1,banyak+1):
                        daftar_obat.append(obat)
                        total_obat.append(penyimpanan[obat])
                    print('Kami telah menambahkan obat {} {}ke keranjang Anda!'
                          .format(biru+obat,hitam))
        except:
            print(merah + "Hanya memuat masukan angka!" + hitam)
    print(nl)

# Fungsi untuk edit daftar obat
def edit_data():
    """Memudahkan pelanggan mengganti obat yang akan dibeli"""
    show_data()
    if daftar_obat:
        while True:
            try:
                index = int(input("Inputkan ID Obat yang akan diubah: "))
                index -= 1
                if index < 0 or index > (len(daftar_obat)-1): 
                    print("ID Obat Salah!"); continue
                break
            except: print("Hanya memuat angka!")
        info_obat()
        while True:
            try:
                val = int(input("Anda ingin merubah ke obat apa? [0 ke Menu Utama] --> "))
                if val < 0 or val > len(penyimpanan):
                    print('Kami mohon maaf obat itu {}tidak tersedia {}di apotek kami!'
                    .format(merah,hitam))
                elif val == 0: break
                else:
                    obat = list(penyimpanan.keys())[val-1]
                    if obat in penyimpanan:
                        daftar_obat[index] = obat
                        total_obat[index] = penyimpanan[obat]
                        print('Kami telah merubah obat menjadi {} {}di keranjang Anda!'
                            .format(biru+obat,hitam))
                    break
            except:
                print(merah + "Hanya memuat masukan angka!" + hitam)
    print(nl)

# Fungsi untuk menghapus daftar obat
def delete_data():
    """Memudahkan pelanggan untuk menghapus obat jika tidak diperlukan"""
    show_data()
    if daftar_obat:
        while True:
            try:
                index = int(input("Inputkan ID Obat yang akan dihapus: "))
                index -= 1
                if index < 0 or index > (len(daftar_obat)-1): 
                    print("ID Obat Salah!"); continue
                break
            except: print("Hanya memuat angka!")
        daftar_obat.remove(daftar_obat[index])
        total_obat.remove(total_obat[index])
        print('{}Obat berhasil dihapus{}!'.format(merah,hitam))
    print(nl)

# barang dan jumlah harga
def pembayaran_obat():
    """Meminta pelanggan untuk membayar sejumlah uang berdasarkan harga yang telah dihitung"""
    print(f'{htebal + "Daftar Obat Anda":57}{"Jumlah":10}{"Harga" + hitam}')
    print(garis2)
    no2 = 1
    for x, y in penyimpanan.items():
      if daftar_obat:
        if x in daftar_obat:
            jmlh = daftar_obat.count(x)
            print(f'{no2:2}) {x:46}{"x"}{str(jmlh):9}Rp.{(y*jmlh):,}')
            no2 += 1
      else:
          print("{}Maaf keranjang Anda masih kosong...{:15}{:10}{}"
                .format(merah,"","0","0"+hitam))
          break
    print(garis2)
    jmlh_bayar = sum(total_obat)
    print(f'{htebal + "Total:":67}{merah}Rp.{jmlh_bayar:,}{hitam}')
    # Memilih untuk melanjutkan pembayaran atau kembali
    if jmlh_bayar:
        yes_no = input(f'{"Apakah Anda ingin lanjut ke pembayaran? [y/n]: "}')
        if yes_no == 'y':
            while True:
                try: jmlh_uang = int(input(f'{"Jumlah uang Anda:":60}Rp.')); break
                except: print(merah + "Hanya memuat masukan angka!" + hitam)
            sisa = int(jmlh_uang)-jmlh_bayar
            print(garis1)
            if sisa >= 0:
                print(f'{htebal + "Kembalian Anda adalah":67}{biru}Rp.{sisa:,}{hitam}')
                daftar_obat.clear()
                total_obat.clear()
                print(nl)
                print("Selamat pembayaran Anda telah".center(spasi))
                print(" _    _   _ _   _    _    ____  _ ".center(spasi))
                print("| |  | | | | \ | |  / \  / ___|| |".center(spasi))
                print("| |  | | | |  \| | / _ \ \___ \| |".center(spasi))
                print("| |__| |_| | |\  |/ ___ \ ___) |_|".center(spasi))
                print("|_____\___/|_| \_/_/   \_\____/(_)".center(spasi))
            else:
                maaf = 'Maaf uang Anda kurang, mohon ulangi pembayaran!'
                print(f'{htebal + maaf:67}{biru}Rp.{sisa:,}{hitam}')
    print(nl)

# Fungsi untuk menampilkan menu
def show_menu():
    """Menampilkan menu kepada pelanggan yang datang"""
    print(htebal + "Silahkan Pilih Menu :" + hitam)
    print("[1] Tampilkan Keranjang Obat")
    print("[2] Tambahkan Obat Baru")
    print("[3] Ubah Obat dalam Keranjang")
    print("[4] Hapus Obat dalam Keranjang")
    print("[5] Pembayaran Obat")
    print("[6] Daftar Anggota")
    print("[0] Keluar dari Program")
    print(garis2)
    while True:
        try: menu = int(input("Choose Menu --> ")); break
        except: print("Hanya memuat angka!")
            
    if menu == 1: 
        clearscreen()
        header("KERANJANG OBAT")
        show_data()
        input("Tekan Enter untuk ke menu utama ")
    elif menu == 2: 
        clearscreen()
        header("TAMBAHKAN OBAT")
        insert_data()
        input("Tekan Enter untuk ke menu utama ")
    elif menu == 3: 
        clearscreen()
        header("MENGUBAH OBAT") 
        edit_data()
        input("Tekan Enter untuk ke menu utama ")
    elif menu == 4: 
        clearscreen()
        header("MENGHAPUS OBAT") 
        delete_data()
        input("Tekan Enter untuk ke menu utama ")
    elif menu == 5: 
        clearscreen()
        header("PEMBAYARAN OBAT")
        pembayaran_obat()
        input("Tekan Enter untuk ke menu utama ")
    elif menu == 6: 
        clearscreen()
        header("Daftar Anggota Kelompok 3".title())
        daftar_anggota()
        input("Tekan Enter untuk ke menu utama ")
    elif menu == 0: del_file(); exit()
    else: print("Menu tidak tersedia!\n"); time.sleep(1)

if __name__ == "__main__":
    while True:
        if not nama:
            nama = input('Silahkan masukkan nama Anda: ')
        clearscreen()
        header("MENU UTAMA")
        print('Halo, selamat datang Bpk/Ibu {}!'.format(biru+nama.title()+hitam))
        show_menu()