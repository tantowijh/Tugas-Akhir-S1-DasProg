import os, platform, time, datetime

# Variable untuk menyimpan obat yang dibeli
daftar_obat = []
# Variable untuk menyimpan biaya obat
total_obat = []

# inisiasi spasi, baris, dan garis
space = 72; newline = '\n'; nama = ''
baris1 = "="*space; baris2 = "-"*space

# inisiasi warna dengan kode ANSII
hitam = '\033[0m'; htebal = '\033[1;30m'; hijau = '\033[1;92m'
jtipis = '\033[0;92m'; biru = '\033[34m'; merah = '\033[91m'

# Fungsi untuk menghapus layar terminal dan cmd
def clearscreen():
    if platform.system() == "Windows": os.system("cls") 
    else: os.system("clear")

# Menentukan waktu pembelian
def waktu():
    def day(x): 
        days = {"Sunday":"Minggu","Monday":"Senin", "Tuesday":"Selasa", "Wednesday": "Rabu", 
                "Thursday":"Kamis", "Friday":"Jum'at","Saturday":"Sabtu"}
        hari = days[x]; return hari
    date = 'Hari ' + day(datetime.datetime.now().strftime("%A")) \
    + datetime.datetime.now().strftime(", %d-%b-%Y, Jam (%H:%M)")
    return date

# Daftar Obat dan harga produk
"""Menyimpan table Obat dan Harga menggunakan Dictionary"""
penyimpanan = {"Polysilane Granul":53918,
               "Oxopect Sirup 60ML":51037, 
               "Prosogan FD 30MG Tablet":25855, 
               "Tolak Angin Cair Plus Madu 15ML 12 SACHET":40747, 
               "Imboost FC Tablet":43091, 
               "Proceles Tablet":2127, 
               "Ozen 10MG/ML Drop 12ML":87199, 
               "Breathy Tetes Hidung":52306,
               "Bodrexin Pilek Alergi PE Sirup 56ML":8559, 
               "OBH Combi Dewasa Batuk Flu Rasa Jahe 100ML":20884, 
               "Siladex Batuk Pilek  30ML":9716, 
               "Hufagrip Pilek Sirup 60ML":18132,
               "Promag Tablet (Per Strip Isi 12 Tablet)":8515,
               "Sensodyne Reg 100G (Merah)":39831,
               "Sensodyne Fresh Mint Flouride 100G":39895}

# informasi apotek
def header(x):
    """Membuat header untuk daftar obat tersedia dan pembayaran obat"""
    print('{}'.format(baris1+hijau))
    print(x.center(space))
    print("    _    ____   ___ _____ _____ _  __   ____ _____ ".center(space))
    print("   / \  |  _ \ / _ \_   _| ____| |/ /  / ___|___ / ".center(space))
    print("  / _ \ | |_) | | | || | |  _| | ' /  | |  _  |_ \ ".center(space))
    print(" / ___ \|  __/| |_| || | | |___| . \  | |_| |___) |".center(space))
    print("/_/   \_\_|    \___/ |_| |_____|_|\_\  \____|____/ ".center(space))
    print('{}{}{}'.format(newline+jtipis,"Jl. Kesuksesan Kita Bersama".center(space).title(), merah))
    print('{}{}'.format(waktu().center(space),hitam+newline+baris1))

# informasi barang
def info_obat():
    """Memuat informasi obat yang tersedia untuk memudahkan pembelian
    
    Daftar Obat
        Berisi nama obat
    Daftar Harga
        Berisi harga obat
    """
    print(f'{htebal + "Daftar Obat":65}{"Harga" + hitam}')
    print(baris2)
    no = 1
    for x, y in penyimpanan.items():
        ss = len(x)
        print(f'{no:2}) {x:54}Rp.{y:,}')
        no += 1
    print(baris2)

# Fungsi untuk menampilkan semua data
def show_data():
    """Menampilkan semua obat yang ada dalam keranjang Pelanggan
    
    *Menampilkan semua obat yang telah ditambahkan ke dalam keranjang 
    oleh pelanggan guna mempermudah untuk merubahnya atau untuk menghapusnya*
    """
    if len(daftar_obat)<=0:
        print('{}Daftar obat Anda{:34}Harga{}'.format(htebal,"",hitam+newline+baris2))
        print('{}Maaf keranjang Anda masih kosong...{:15}{}{}'.format(merah,"","0",hitam))
    else:
        print('{}Daftar obat Anda{:34}Harga{}'.format(htebal,"",hitam+newline+baris2))
        for index in range(len(daftar_obat)):
            print("{:2}) {:46}Rp.{:,}".format(index+1, daftar_obat[index], total_obat[index]))
    print(baris2+newline)

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
    print(newline)

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
    print(newline)

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
    print(newline)

# barang dan jumlah harga
def pembayaran_obat():
    """Meminta pelanggan untuk membayar sejumlah uang berdasarkan harga yang telah dihitung"""
    print(f'{htebal + "Daftar Obat Anda":57}{"Jumlah":10}{"Harga" + hitam}')
    print(baris2)
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
    print(baris2)
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
            print(baris1)
            if sisa >= 0:
                print(f'{htebal + "Kembalian Anda adalah":67}{biru}Rp.{sisa:,}{hitam}')
                daftar_obat.clear()
                total_obat.clear()
                print(newline)
                print("Selamat pembayaran Anda telah".center(space))
                print(" _    _   _ _   _    _    ____  _ ".center(space))
                print("| |  | | | | \ | |  / \  / ___|| |".center(space))
                print("| |  | | | |  \| | / _ \ \___ \| |".center(space))
                print("| |__| |_| | |\  |/ ___ \ ___) |_|".center(space))
                print("|_____\___/|_| \_/_/   \_\____/(_)".center(space))
            else:
                maaf = 'Maaf uang Anda kurang, mohon ulangi pembayaran!'
                print(f'{htebal + maaf:67}{biru}Rp.{sisa:,}{hitam}')
    print(newline)

# Fungsi untuk menampilkan menu
def show_menu():
    """Menampilkan menu kepada pelanggan yang datang"""
    print(htebal + "Silahkan Pilih Menu :" + hitam)
    print("[1] Tampilkan Keranjang Obat")
    print("[2] Tambahkan Obat Baru")
    print("[3] Ubah Obat dalam Keranjang")
    print("[4] Hapus Obat dalam Keranjang")
    print("[5] Pembayaran Obat")
    print("[0] Keluar dari Program")
    print(baris2)
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
    elif menu == 0: exit()
    else: print("Menu tidak tersedia!\n"); time.sleep(1)

if __name__ == "__main__":
    while True:
        clearscreen()
        if not nama:
            nama = input('Silahkan masukkan nama Anda: ')
        clearscreen()
        header("MENU UTAMA")
        print('Halo, selamat datang Bpk/Ibu {}!'.format(biru+nama.title()+hitam))
        show_menu()