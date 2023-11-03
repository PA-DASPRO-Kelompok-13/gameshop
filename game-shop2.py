import os
from datetime import datetime
import json
import pwinput
from prettytable import PrettyTable

path_user = 'user.json'
with open(path_user, "r") as file:
    data_user = json.load(file)

path_game = 'game.json'
with open(path_game, "r") as file:
    data_game = json.load(file)

path_keranjang = 'keranjang.json'
with open(path_keranjang, "r") as file:
    data_keranjang = json.load(file)

path_riwayat = 'riwayat.json'
with open(path_riwayat, "r") as file:
    data_riwayat2 = json.load(file)

tanggal = datetime.now()
format_tanggal = tanggal.strftime('%d/%m/%y')
tanggal = format_tanggal

invoice = "invoice.txt"

def lanjutkan():
    input(f'              Tekan tombol Enter Untuk Kembali ke Menu')

def clear_screen():
    os.system('cls')

def batas():
    print("[]=================================================================[]")

def halaman_login():
    batas()
    print(' ' * 22 + "Selamat Datang Di GameShop") 
    batas()
    print(f"    1. Masuk") 
    print(f"    2. Daftar") 
    print(f"    3. Exit")
    batas()
    
    pilihan = int(input(f'    Silahkan Masukkan Pilihan Anda : '))
    if pilihan == 1:
        clear_screen()
        login()
    elif pilihan == 2:
        clear_screen()
        daftar()
    elif pilihan == 3:
        clear_screen()
        batas()
        print(' ' * 24 + 'Silahkan Datang Kembali')
        batas()
        return


# Ini Adalah Login Untuk Multiple User yang akan route sesuai Role
def login():
    batas()
    print(' ' * 28 + 'Silahkan Login')
    batas()
    username_input = input(f"    Username : ")
    password_input = pwinput.pwinput(prompt="    Password : ")

    nama_user = username_input
    login_successful = False

    for x in data_user['users']:
        username = x['username']
        password = x['password']
        role = x['role']

        if username_input == username and password_input == password:
            login_successful = True
            if role == 'admin':
                clear_screen()
                admin(nama_user)
            elif role == 'user':
                clear_screen()
                user(nama_user)

    if not login_successful:
        clear_screen()
        batas()
        print(' ' * 22 + 'Data Anda Salah, Login Ulang')
        login()
    return nama_user


# Ini adalah script untuk mendaftar user
def daftar():
    batas()
    print(' ' * 28 + 'Silahkan Daftar')
    batas()
    wallet_terakhir = None
    for user in data_user['users']:
        if user['role'] == 'user':
            nomor_wallet = user.get('nomor_wallet')
            if nomor_wallet != None:
                if wallet_terakhir == None or nomor_wallet > wallet_terakhir:
                    wallet_terakhir = nomor_wallet

    
    nama_user = input(f'    Masukkan Nama : ')
    username_user = input(f'    Masukkan Username : ')
    password_user = input(f'    Masukkan password : ')
    role_user = 'user'
    pin_user = int(input(f'    Pin : '))
    nomor_wallet_user = int(wallet_terakhir + 1)
    saldo_wallet_user = 0

    user_baru = {
        "nama": nama_user,
        "username": username_user,
        "password": password_user,
        "role": role_user,
        "pin_wallet": pin_user,
        "nomor_wallet": nomor_wallet_user,
        "saldo_wallet": saldo_wallet_user
    }

    data_user['users'].append(user_baru)

    with open(path_user, 'w') as file:
        json.dump(data_user, file, indent=4)
    
    clear_screen()
    batas()
    print(' ' * 20 + "Pengguna baru telah ditambahkan")
    login()


# ==================== Start Admin Section ====================
def admin(nama_user):
# ==================== Start Crud ADMIN ====================
    def aksi_admin(nama_user):
        batas()
        print(' ' * 26 + 'Halaman CRUD Admin')
        batas()

        def tabel_admin():
            nomor_urutan = 1
            tabel_user = PrettyTable()
            tabel_user.field_names = ['No', 'Nama', 'Username']
            for user in data_user['users']:
                if user['role'] == 'admin':
                    tabel_user.add_row([nomor_urutan, user['nama'], user['username']])
                    nomor_urutan += 1
            print(tabel_user)

        def tambah_admin():
            batas()
            print(' ' * 28 + 'Tambahkan Admin')
            batas()
            nama_user = input(f'    Nama : ')
            username_user = input(f'    Username : ')
            password_user = input(f'    password : ')
            role_user = 'admin'

            user_baru = {
                "nama": nama_user,
                "username": username_user,
                "password": password_user,
                "role": role_user,
            }

            data_user['users'].append(user_baru)

            with open(path_user, 'w') as file:
                json.dump(data_user, file, indent=4)

            clear_screen()
            batas()
            print(' ' * 18 + f'Admin baru telah ditambahkan')
            batas()
            tabel_admin()
            batas()
            lanjutkan()
            clear_screen()
            aksi_admin(nama_user)


        def edit_admin():
            batas()
            print(' ' * 28 + 'Edit Admin')
            batas()
            tabel_admin()

            batas()
            id_edit = int(input(f'    Masukkan Nomor Yang Ingin Diedit : '))
            user_edit = None

            for user in data_user['users']:
                if user.get('role') == 'admin':
                    id_edit -= 1
                    if id_edit == 0:
                        user_edit = user
                        break

            clear_screen()
            if user_edit:
                batas()
                print(' ' * 22 + 'Data User Yang di Edit:')
                batas()
                nama_lama = user_edit['nama']
                username_lama = user_edit['username']
                password_lama = user_edit['password']
                role_lama = user_edit['role']

                nama_baru = input(f'    Masukkan Nama Baru ({nama_lama}): ')
                username_baru = input(f'    Masukkan Username Baru ({username_lama}): ')
                password_baru = input(f'    Masukkan Password Baru ({password_lama}): ')
                role_baru = role_lama

            else:
                print("Pengguna dengan nomor urutan yang diminta tidak ditemukan.")

            user_edit['nama'] = nama_baru
            user_edit['username'] = username_baru
            user_edit['password'] = password_baru
            user_edit['role'] = role_baru

            with open(path_user, 'w') as file:
                json.dump(data_user, file, indent=4)
            
            clear_screen()
            batas()
            print(' ' * 18 + f'Data Admin Telah Disimpan')
            batas()
            tabel_admin()
            batas()
            lanjutkan()
            clear_screen()
            aksi_admin(nama_user)


        def hapus_admin():
            batas()
            print(' ' * 28 + 'Hapus Admin')
            batas()
            tabel_admin()

            id_hapus = int(input('Masukkan Nomor Yang Ingin Dihapus : '))
            user_hapus = None

            for user in data_user['users']:
                if user.get('role') == 'admin':
                    id_hapus -= 1
                    if id_hapus == 0:
                        user_hapus = user
                        break

            if user_hapus:
                data_user['users'].remove(user_hapus)

                with open(path_user, 'w') as file:
                    json.dump(data_user, file, indent=4)
            else:
                print("User Tidak Ditemukan")
            
            clear_screen()
            batas()
            print(' ' * 18 + f'Data Admin Telah Dihapus')
            batas()
            tabel_admin()
            batas()
            lanjutkan()
            clear_screen()
            aksi_admin(nama_user)


        tabel_admin()
        batas()
        print(' ' * 18 + f'Pilih Aksi Yang Ingin Anda Lakukan :')
        batas()
        print(f'    1. Tambah User')
        print(f'    2. Edit User')
        print(f'    3. Hapus User')
        print(f'    4. Kembali')
        batas()
        pilihan_aksi = int(input(f'    Masukkan Pilihan : '))

        if pilihan_aksi == 1:
            clear_screen()
            tambah_admin()
        elif pilihan_aksi == 2:
            clear_screen()
            edit_admin()
        elif pilihan_aksi == 3:
            clear_screen()
            hapus_admin()
        elif pilihan_aksi == 4:
            clear_screen()
            admin(nama_user)
        else:
            clear_screen()
            print(' ' * 20 + 'Input anda tidak valid, Coba Lagi')
# ==================== End Crud ADMIN ====================


# ==================== Start Crud USER ====================
    def aksi_user(nama_user):
        
        batas()
        print(' ' * 26 + 'Halaman CRUD User')
        batas()

        wallet_terakhir = None
        for user in data_user['users']:
            if user['role'] == 'user':
                nomor_wallet = user.get('nomor_wallet')
                if nomor_wallet != None:
                    if wallet_terakhir == None or nomor_wallet > wallet_terakhir:
                        wallet_terakhir = nomor_wallet

        def tabel_user():
            nomor_urutan = 1
            tabel_user = PrettyTable()
            tabel_user.field_names = ['No', 'Nama', 'Username', 'Pin', 'No. Wallet', 'Saldo']
            for user in data_user['users']:
                if user['role'] == 'user':
                    tabel_user.add_row([nomor_urutan, user['nama'], user['username'], user.get('pin_wallet', ''), user.get('nomor_wallet', ''), user.get('saldo_wallet', '')])
                    nomor_urutan += 1
            print(tabel_user)


        # CRUD Admin Section
        def tambah_user():
            batas()
            print(' ' * 28 + 'Tambahkan User')
            batas()

            nama_user = input(f'    Nama : ')
            username_user = input(f'    Username : ')
            password_user = input(f'    password : ')
            role_user = 'user'
            pin_user = int(input(f'    Pin : '))
            nomor_wallet_user = int(wallet_terakhir + 1)
            saldo_wallet_user = 0

            user_baru = {
                "nama": nama_user,
                "username": username_user,
                "password": password_user,
                "role": role_user,
                "pin_wallet": pin_user,
                "nomor_wallet": nomor_wallet_user,
                "saldo_wallet": saldo_wallet_user
            }

            data_user['users'].append(user_baru)

            with open(path_user, 'w') as file:
                json.dump(data_user, file, indent=4)
            print("Pengguna baru telah ditambahkan")

            clear_screen()
            batas()
            print(' ' * 18 + f'User baru telah ditambahkan')
            batas()
            tabel_user()
            batas()
            lanjutkan()
            clear_screen()
            aksi_user(nama_user)


        def edit_user():
            batas()
            print(' ' * 28 + 'Edit User')
            batas()
            tabel_user()

            batas()
            id_edit = int(input(f'    Masukkan Nomor Yang Ingin Diedit : '))
            user_edit = None

            for user in data_user['users']:
                if user.get('role') == 'user':
                    id_edit -= 1
                    if id_edit == 0:
                        user_edit = user
                        break
            
            clear_screen()
            
            if user_edit:
                batas()
                print(' ' * 22 + 'Data User Yang di Edit:')
                batas()
                nama_lama = user_edit['nama']
                username_lama = user_edit['username']
                password_lama = user_edit['password']
                role_lama = user_edit['role']
                pin_wallet_lama = user_edit['pin_wallet']
                nomor_wallet_lama = user_edit['nomor_wallet']
                saldo_wallet_lama = user_edit['saldo_wallet']

                nama_baru = input(f'    Masukkan Nama Baru ({nama_lama}): ')
                username_baru = input(f'    Masukkan Username Baru ({username_lama}): ')
                password_baru = input(f'    Masukkan Password Baru ({password_lama}): ')
                role_baru = role_lama
                pin_wallet_baru = int(input(f'    Masukkan Pin Baru ({pin_wallet_lama}): '))
                nomor_wallet_baru = nomor_wallet_lama
                saldo_wallet_baru = int(input(f'    Masukkan Saldo Baru ({saldo_wallet_lama}): '))
            else:
                print("Pengguna dengan nomor urutan yang diminta tidak ditemukan.")

            user_edit['nama'] = nama_baru
            user_edit['username'] = username_baru
            user_edit['password'] = password_baru
            user_edit['role'] = role_baru
            user_edit['pin_wallet'] = pin_wallet_baru
            user_edit['nomor_wallet'] = nomor_wallet_baru
            user_edit['saldo_wallet'] = saldo_wallet_baru

            with open(path_user, 'w') as file:
                json.dump(data_user, file, indent=4)
            
            clear_screen()
            batas()
            print(' ' * 18 + f'Data User Telah Disimpan')
            batas()
            tabel_user()
            batas()
            lanjutkan()
            clear_screen()
            aksi_user(nama_user)

        def hapus_user():
            batas()
            print(' ' * 28 + 'Hapus User')
            batas()
            tabel_user()

            id_hapus = int(input('Masukkan Nomor Yang Ingin Dihapus : '))
            user_hapus = None
            
            for user in data_user['users']:
                if user.get('role') == 'user':
                    id_hapus -= 1
                    if id_hapus == 0:
                        user_hapus = user
                        break
            
            if user_hapus:
                data_user['users'].remove(user_hapus)
                
                with open(path_user, 'w') as file:
                    json.dump(data_user, file, indent=4)
            else:
                print("User Tidak Ditemukan")

            clear_screen()
            batas()
            print(' ' * 18 + f'Data User Telah Dihapus')
            batas()
            tabel_user()
            batas()
            lanjutkan()
            clear_screen()
            aksi_user(nama_user)

        tabel_user()
        batas()
        print(' ' * 18 + f'Pilih Aksi Yang Ingin Anda Lakukan :')
        batas()
        print(f'    1. Tambah User')
        print(f'    2. Edit User')
        print(f'    3. Hapus User')
        print(f'    4. Kembali')
        batas()
        pilihan_aksi = int(input(f'    Masukkan Pilihan : '))

        if pilihan_aksi == 1:
            clear_screen()
            tambah_user()
        elif pilihan_aksi == 2:
            clear_screen()
            edit_user()
        elif pilihan_aksi == 3:
            clear_screen()
            hapus_user()
        elif pilihan_aksi == 4:
            clear_screen()
            admin(nama_user)
# ==================== End Crud USER ====================


# ==================== Start Crud GAME ====================
    def aksi_barang(nama_user):
        batas()
        print(' ' * 26 + 'Halaman CRUD Game')
        batas()

        ID_terbesar = None
        for game in data_game['game']:
            ID = game.get('ID')
            if ID is not None:
                ID = int(ID)
                if ID_terbesar is None or ID > ID_terbesar:
                    ID_terbesar = ID

        def tabel_game():
            nomor_urutan = 1
            tabel_game = PrettyTable()
            tabel_game.field_names = ['No', 'Nama Game', 'Developer', 'Tahun Rilis', 'Versi Game', 'Harga Game']
            for game in data_game['game']:
                tabel_game.add_row([nomor_urutan, game['nama_game'], game['developer'], game['tahun_rilis'], game['versi_game'], game['harga_game']])
                nomor_urutan += 1
            print(tabel_game)


        def tambah_game():
            batas()
            print(' ' * 28 + 'Tambahkan Game')
            batas()
            id_baru = ID_terbesar + 1
            ID = str(f'0{id_baru}')
            nama_game = input(f'    Nama Game: ')
            developer = input(f'    Developer: ')
            tahun_rilis = input(f'    Tahun Rilis: ')
            versi_game = float(input(f'    Versi Game: '))
            harga_game = int(input(f'    Harga Game: '))

            game_baru = {
                "ID": ID,
                "nama_game": nama_game,
                "developer": developer,
                "tahun_rilis": tahun_rilis,
                "versi_game": versi_game,
                "harga_game": harga_game
            }

            data_game['game'].append(game_baru)

            with open(path_game, 'w') as file:
                json.dump(data_game, file, indent=4)
            print("Game baru telah ditambahkan")

            clear_screen()
            batas()
            print(' ' * 18 + f'Game baru telah ditambahkan')
            batas()
            tabel_game()
            batas()
            lanjutkan()
            clear_screen()
            aksi_barang(nama_user)


        def edit_game():
            batas()
            print(' ' * 28 + 'Edit Game')
            batas()
            tabel_game()
            id_edit = int(input('Masukkan Nomor Game Yang Ingin Diedit : '))

            game_to_edit = None
            for game in data_game['game']:
                if game.get('ID'):
                    id_edit -= 1
                    if id_edit == 0:
                        game_to_edit = game
                        break
            clear_screen()

            if game_to_edit:
                batas()
                print(' ' * 22 + 'Data Game Yang di Edit:')
                batas()
                nama_game_baru = input(f'    Masukkan Nama Baru ({game_to_edit["nama_game"]}): ')
                developer_baru = input(f'    Masukkan Developer Baru ({game_to_edit["developer"]}): ')
                tahun_rilis_baru = input(f'    Masukkan Tahun Rilis Baru ({game_to_edit["tahun_rilis"]}): ')
                versi_game_baru = float(input(f'    Masukkan Versi Game Baru ({game_to_edit["versi_game"]}): '))
                harga_game_baru = int(input(f'    Masukkan Harga Game Baru ({game_to_edit["harga_game"]}): '))

                game_to_edit["nama_game"] = nama_game_baru
                game_to_edit["developer"] = developer_baru
                game_to_edit["tahun_rilis"] = tahun_rilis_baru
                game_to_edit["versi_game"] = versi_game_baru
                game_to_edit["harga_game"] = harga_game_baru

                with open(path_game, 'w') as file:
                    json.dump(data_game, file, indent=4)
            else:
                print('Nomor game tidak valid.')

            clear_screen()
            batas()
            print(' ' * 18 + f'Data Game Telah Disimpan')
            batas()
            tabel_game()
            batas()
            lanjutkan()
            clear_screen()
            aksi_barang(nama_user)


        def hapus_game():
            batas()
            print(' ' * 28 + 'Hapus Game')
            batas()
            tabel_game()

            id_hapus = int(input('Masukkan Nomor Yang Ingin Dihapus : '))
            game_hapus = None

            for game in data_game['game']:
                if game.get('ID'):
                    id_hapus -= 1
                    if id_hapus == 0:
                        game_hapus = game
                        break
            
            if game_hapus:
                data_game['game'].remove(game_hapus)

            with open(path_game, 'w') as file:
                json.dump(data_game, file, indent=4)

            clear_screen()
            batas()
            print(' ' * 18 + f'Data Game Telah Dihapus')
            batas()
            tabel_game()
            batas()
            lanjutkan()
            clear_screen()
            aksi_user(nama_user)


        tabel_game()
        batas()
        print(' ' * 18 + f'Pilih Aksi Yang Ingin Anda Lakukan :')
        batas()
        print(f'    Pilih Aksi Yang Ingin Anda Lakukan :')
        print(f'    1. Tambah Game')
        print(f'    2. Edit Game')
        print(f'    3. Hapus Game')
        print(f'    4. Kembali')
        batas()
        pilihan_aksi = int(input(f'    Masukkan Pilihan : '))

        if pilihan_aksi == 1:
            clear_screen()
            tambah_game()
        elif pilihan_aksi == 2:
            clear_screen()
            edit_game()
        elif pilihan_aksi == 3:
            clear_screen()
            hapus_game()
        elif pilihan_aksi == 4:
            clear_screen()
            admin(nama_user)
# ==================== End Crud GAME ====================


# ==================== Start Menu Admin ====================
    batas()
    print(' ' * 20 + f'Selamat Datang Di Admin Panel')
    batas()
    print(' ' * 20 + 'Apa Yang Ingin Anda Lakukan?')
    batas()
    print(f'    1. Admin')
    print(f'    2. User')
    print(f'    3. Game')
    print(f'    4. Keluar')
    batas()
    aksi = int(input(f'    Masukkan Pilihan : '))

    if aksi == 1:
        clear_screen()
        aksi_admin(nama_user)
    elif aksi == 2:
        clear_screen()
        aksi_user(nama_user)
    elif aksi == 3:
        clear_screen()
        aksi_barang(nama_user)
    elif aksi == 4:
        clear_screen()
        batas()
        print(' ' * 26 + 'Selamat Tinggal')
        batas()
# ==================== End Menu Admin ====================

# ==================== End Admin Section ====================





# ==================== Halaman User ====================
def user(nama_user):
    def user_lihat_game(nama_user):
        tabel_game = PrettyTable()
        tabel_game.field_names = ['ID','Nama Game', 'Developer', 'Tahun Rilis', 'Versi Game', 'Harga Game']
        
        for item in data_game['game']:
            tabel_game.add_row([item['ID'],item['nama_game'], item['developer'], item['tahun_rilis'], item['versi_game'], item['harga_game']])
        
        print(tabel_game)
        print(f'    Pilih Aksi Anda :')
        print(f'    1. Kembali ke Menu')
        print(f'    2. Beli Game')
        batas()
        
        lihat_game = input(f'   Pilih : ')
        if lihat_game == '1':
            user(nama_user)
        elif lihat_game == '2':
            clear_screen()
            user_beli_game(nama_user)
        else:
            print('pilihan tidak valid')


# ==================== Start Beli Game ====================
    def user_beli_game(nama_user):
        tabel_game = PrettyTable()
        tabel_game.field_names = ['ID','Nama Game', 'Developer', 'Tahun Rilis', 'Versi Game', 'Harga Game']
        
        for item in data_game['game']:
            tabel_game.add_row([item['ID'],item['nama_game'], item['developer'], item['tahun_rilis'], item['versi_game'], item['harga_game']])
        print(tabel_game)
        
        id_produk = input("Masukkan ID produk yang akan dibeli (0 untuk selesai): ")
        game_co = None
        
        for game in data_game['game']:
            if game["ID"] == id_produk:
                game_co = game
                break
        
        if game_co != None:
            clear_screen()
            batas()
            print(' ' * 12 + 'Barang Berhasil Ditambahkan ke Keranjang')
        
        else:
            print('Data Tidak Ada')
        
        nama_game_co = str(game_co['nama_game'])
        harga_game_co = int(game_co['harga_game'])
        
        co_keranjang = {
            "nama_game" : nama_game_co,
            "harga_game" : harga_game_co,
            "nama_user" : nama_user
        }
        
        if "keranjang" not in data_keranjang:
            data_keranjang["keranjang"] = []
        
        data_keranjang["keranjang"].append(co_keranjang)
        
        with open(path_keranjang, 'w') as file:
            json.dump(data_keranjang, file, indent=4)
        
        user_keranjang(nama_user)

# ==================== End Beli Game ====================


# ==================== Start Keranjang User ====================
    def user_keranjang(nama_user):
        
        tabel_keranjang = PrettyTable()
        tabel_keranjang.field_names = ['Nama Game', 'Harga Game']
        
        keranjang_user = []
        for x in data_keranjang['keranjang']:
            if x['nama_user'] == nama_user:
                keranjang_user.append(x)
        
        if not keranjang_user:
            batas()
            print(' ' * 24  + 'Keranjang Anda kosong.')
            batas()
            lanjutkan()
            user(nama_user)
        else:

            print(' ' * 24 +  "Isi Keranjang Anda : ")
            batas()
            for x in keranjang_user:
                tabel_keranjang.add_row([x['nama_game'], x['harga_game']])
            print(tabel_keranjang)
            batas()
            print(f'    Pilih Aksi yang ingin Anda Lakukan')
            print(f'    1. Hapus Barang Yang Ada Di Keranjang')
            print(f'    2. Checkout Barang Di Keranjang')
            print(f'    3. Kembali Ke Menu')
            batas()
            aksi_keranjang = input(f'    Masukkan Pilihan : ')
            
            if aksi_keranjang == '1':
                clear_screen()
                hapus_keranjang(nama_user)
            elif aksi_keranjang == '2':
                clear_screen()
                user_checkout(nama_user)
            elif aksi_keranjang == '3':
                user(nama_user)

# ==================== End Keranjang User ====================


# ==================== Start Hapus Keranjang ====================
    def hapus_keranjang(nama_user):
        
        tabel_keranjang = PrettyTable()
        tabel_keranjang.field_names = ['No', 'Nama Game', 'Harga Game']
        
        keranjang_user = []
        for x in data_keranjang['keranjang']:
            if x['nama_user'] == nama_user:
                keranjang_user.append(x)
        
        nomor_urutan = 1
        for x in keranjang_user:
            tabel_keranjang.add_row([nomor_urutan, x['nama_game'], x['harga_game']])
            nomor_urutan += 1
        
        batas()
        print(tabel_keranjang)
        batas()
        pilihan = int(input(f'    Masukkan Nomor Game Yang Ingin Di Hapus : '))
        index_barang = pilihan - 1
        game_hapus = keranjang_user[index_barang]['nama_game']
        
        for item in data_keranjang['keranjang']:
            if item['nama_user'] == nama_user and item['nama_game'] == game_hapus:
                data_keranjang['keranjang'].remove(item)
        
        with open(path_keranjang, 'w') as file:
            json.dump(data_keranjang, file, indent=4)
        
        clear_screen()
        batas()
        print(' ' * 23 + 'Game Berhasil Dihapus')
        user_keranjang(nama_user)

# ==================== End Hapus Keranjang ====================


# ==================== Start User Checkout ====================
    def user_checkout(nama_user):
        total_harga = 0
        
        batas()
        print(' ' * 22 + 'Anda Ingin Membeli :')
        batas()
        for x in data_keranjang['keranjang']:
            if x['nama_user'] == nama_user:
                game_co = x['nama_game']
                harga_co = x['harga_game']
                total_harga += harga_co
                print(' ' * 4 + game_co)
        print(' ' * 4 + f'Seharga :  {total_harga}')
        batas()
        for y in data_user['users']:
            if y['username'] == nama_user:
                saldo_user = y['saldo_wallet']
        
        transaksi = False
        
        if total_harga >= saldo_user:
            print(' ' * 22 + 'Saldo Anda Tidak Cukup')
            batas()
            print(f'    1. Top Up Saldo')
            print(f'    2. Batalkan Transaksi')
            pilihan = input('Masukkan Pilihan Anda : ')
            if pilihan == '1':
                clear_screen()
                user_isi_saldo(nama_user)
            elif pilihan == '2':
                print(' ' * 28 + 'Transaksi Dibatalkan')
            
        elif total_harga <= saldo_user:
            print(' ' * 28 + 'Saldo Anda Cukup')
            batas()
            print(f'    1. Konfirmasi Pembayaran')
            print(f'    2. Top Up Saldo')
            print(f'    3. Batalkan Transaksi')
            batas()
            pilihan = input(f'    Masukkan Pilihan Anda : ')
            if pilihan == '1':
                clear_screen()
                batas()
                print(' ' * 26 + 'Lanjutkan Pembayaran')
                batas()
                transaksi = True
            elif pilihan == '2':
                user_isi_saldo(nama_user)
            elif pilihan == '3':
                batas()
                print(' ' * 26 + 'Transaksi Dibatalkan')
                batas()
                lanjutkan()
        
        if transaksi == True:
            
            print(f'    Total pembayaran Anda : Rp. {total_harga}')
            print(f'    Saldo Anda            : Rp. {saldo_user}')
            batas()
            
            konfirmasi_pin = int(pwinput.pwinput(f'    Masukkan Pin Anda : '))
            for x in data_user['users']:
                if x['username'] == nama_user:
                    if x['pin_wallet'] == konfirmasi_pin:
                        sisa_saldo = saldo_user-total_harga
                        
                        clear_screen()
                        batas()
                        print(' ' * 16 + 'Pin Terkonfirmasi, Pembayaran Berhasil')
                        batas()
                        lanjutkan()
                    else:
                        print('Pin Salah')
        
        with open(invoice, "w")as file:
            file.write("[]=========================================[]\n")
            file.write("[]            INVOICE PEMBELIAN            []\n")
            file.write("[]=========================================[]\n")
            file.write(f"  Nama Pembeli: {nama_user}\n")
            file.write(f"  Tanggal Invoice: {tanggal}\n")
            file.write("[]=========================================[]\n")
            file.write("[]            Game Yang Dibeli             []\n")
            file.write("[]=========================================[]\n")

            for x in data_keranjang['keranjang']:
                if x['nama_user'] == nama_user:
                    file.write(f"  -{game_co} \n")
            
            file.write("[]=========================================[]\n")
            file.write(f"  Total Harga: {total_harga} IDR\n")
            file.write("[]=========================================[]\n")
            
            for item in data_keranjang['keranjang']:
                if item['nama_user'] == nama_user:
                    data_riwayat2['riwayat'].append({"nama_game": item["nama_game"], "pembeli": nama_user})
            
            data_keranjang['keranjang'] = [item for item in data_keranjang['keranjang'] if item['nama_user'] != nama_user]
            
            for x in data_user['users']:
                if x['username'] == nama_user:
                    x['saldo_wallet'] = sisa_saldo

        
        with open(path_user, 'w') as file:
            json.dump(data_user, file, indent=4)
        
        with open(path_keranjang, 'w') as file:
            json.dump(data_keranjang, file, indent=4)
        
        with open(path_riwayat, 'w') as file:
            json.dump(data_riwayat2, file, indent=4)

        user(nama_user)

# ==================== End User Checkout ====================


# ==================== Start Isi Saldo ====================
    def user_isi_saldo(nama_user):
        batas()
        print(' ' * 25 + 'Top Up Saldo Wallet')
        batas()
        print(' ' * 4 + f'Saldo Anda : {saldo_user}')
        batas()
        # print(' ' * 28 + f'Pilihan Saldo')
        # batas()
        print(f'    1. 50000')
        print(f'    2. 100000')
        print(f'    3. 200000')
        print(f'    4. 350000')
        print(f'    5. 500000')
        print(f'    6. 700000')
        print(f'    7. Kembali')
        batas()
        topup_user = int(input(f'    Masukkan Nomor Pilihan Anda : '))
        clear_screen()
        
        if topup_user == 1:
            nominal = 50000
        elif topup_user == 2:
            nominal = 100000
        elif topup_user == 3:
            nominal = 200000
        elif topup_user == 4:
            nominal = 3500000
        elif topup_user == 5:
            nominal = 500000
        elif topup_user == 6:
            nominal = 700000
        elif topup_user == 7:
            user(nama_user)
        
        batas()
        print(' ' * 7 + f'Apakah anda ingin melakukan isi saldo sebesar Rp. {nominal}?')
        konfirmasi = input(' ' * 7 + 'Lanjutkan Transaksi? (Y/T) : ')
        batas()
        
        tambah_saldo = False
        if konfirmasi == 'y' or konfirmasi == 'Y':
            konfirmasi_pin = int(pwinput.pwinput(' ' * 7 +  f'Masukkan Pin Anda : '))
            
            for x in data_user['users']:
                if x['username'] == nama_user:
                    if x['pin_wallet'] == konfirmasi_pin:
                        tambah_saldo = True
                        clear_screen()
                    else:
                        print('Pin Salah')
        elif konfirmasi == 't' or konfirmasi == 'T':
            print(' ' * 20 +  f'Transaksi Anda Dibatalkan')
            batas()
            lanjutkan()
            clear_screen()
            user(nama_user)
        else:
            print('Tidak Tahu')
        
        if tambah_saldo == True:
            for x in data_user['users']:
                if x['username'] == nama_user:
                    x['saldo_wallet'] += nominal
            
            with open(path_user, 'w') as file:
                json.dump(data_user, file, indent=4)
            batas()
            print(' ' * 24 + 'Berhasil Top Up Saldo!')
            batas()
            lanjutkan()
            user(nama_user)
        

# ==================== End Isi Saldo ====================


# ==================== Start User Menu ====================
    for x in data_user['users']:
        if x['username'] == nama_user:
            saldo_user = x['saldo_wallet']
    nama_user = nama_user
    clear_screen()
    
    batas()
    print(f'    Hai, {nama_user}')
    print(f'    Saldo Anda : {saldo_user}')
    batas()
    
    print(" " * 32 + 'Menu')
    batas()
    print(f'    1. Lihat Game')
    print(f'    2. Lihat isi Keranjang')
    print(f'    3. Isi Saldo')
    print(f'    4. Keluar')
    batas()
    input_halaman_user = input(f'    Pilih menu : ')
    
    if input_halaman_user == '1' :
        clear_screen()
        user_lihat_game(nama_user)
        return
    elif input_halaman_user == '2':
        clear_screen()
        user_keranjang(nama_user)
    elif input_halaman_user == '3':
        clear_screen()
        user_isi_saldo(nama_user)
    elif input_halaman_user == '4':
        clear_screen()
        batas()
        print(' ' * 24 + 'Silahkan Datang Kembali')
        batas()
        return

# ==================== End User Menu ====================

clear_screen()
halaman_login()
# login()