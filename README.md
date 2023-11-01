# GAMESHOP

Sebuah sistem dimana admin dapat melakukan penjualan dan pengelolaan game serta pengguna dapat melakukan transaksi pembelian game

## Module & Library
1. `import os`: Digunakan untuk berinteraksi dengan sistem operasi.

2. `import json`: Digunakan untuk mengakses data JSON.

3. `import pwinput`: Digunakan untuk menampilkan **** untuk input kata sandi.

4. `from prettytable import PrettyTable`: Digunakan untuk membuat tabel rapi dalam teks.
```python
import os
import json 
import pwinput
from prettytable import PrettyTable
```

## Halaman User

Halaman untuk user setelah login program</br>

- Menyapa User sesuai dengan akun yang digunakan untuk login </br>
- Menampilkan Saldo user </br>
- Menampilkan Jumlah keranjang user

Menu
1. lihat game : mengarahkan user ke halaman untuk melihat game
2. Lihat isi keranjang : mengarahkan user ke halaman keranjang user 
3. Isi Saldo : mengarahkan user ke halaman untuk mengisi saldo user
4. Keluar : mengarahkan user ke halaman login

input untuk user memilih menu

![Screenshot 2023-11-01 061422](https://github.com/mdzakyirawan/pa13/assets/144348757/3fe94df1-17b7-4fff-b076-c525cc3df4d4)


## Halaman User Lihat Game
Halaman untuk user melihat daftar game</br>

Menampilkan daftar game menggunakan prettytable</br>
1. kembali ke menu : mengarahkan user ke menu user
2. beli game : mengarahkan user ke halaman pembelian game

input untuk pilihan user

![image](https://github.com/mdzakyirawan/pa13/assets/144348757/2bf6aef3-74dd-41ef-bd37-2de6efb453da)

## Halaman User Beli Game
Halaman untuk user dapat memilih game yang ingin dibeli</br>

Menampilkan daftar game yang tersedia</br>
input untuk user memilih game yang ingin dibeli 

![image](https://github.com/mdzakyirawan/pa13/assets/144348757/80bdff35-ddc7-4937-b3f0-4c50fae34281)


## Keranjang User
Keranjang untuk game game yang sudah dipilih oleh user</br>

Menampilkan tabel daftar game yang sudah ada di keranjang user

Pilihan aksi 
1. Hapus Barang : untuk menghapus game dari keranjang user
2. Checkout : untuk melakukan checkout dan transaksi pembelian game
3. Kembali ke menu : mengarahkan user kembali ke menu user

![image](https://github.com/mdzakyirawan/pa13/assets/144348757/4f8097ec-8153-4fa1-a8bd-fb4392e9436a)

## User Hapus Keranjang
Menampilkan tabel daftar game yang ada di keranjang user</br>
input untuk memilih game yang ingin dihapus user

![image](https://github.com/mdzakyirawan/pa13/assets/144348757/65148251-68e2-43a9-82db-c49fe63a3180)

## User Checkout

Menampilkan game yang akan dibeli</br> 
Menampilkan total harga game</br>
Menampilkan status saldo</br>

1. Konfirmasi Pembayaran : melanjutkan transaksi ke halaman 
2. Top Up Saldo : mengarahkan ke halaman pembayaran
3. Batalkan Transaksi : membatalkan transaksi

input untuk pilihan user

![image](https://github.com/PA-DASPRO-Kelompok-13/gameshop/assets/144348757/b4f49acb-06e8-40f4-92ce-a6e9f302f1aa)

Menampilkan total harga untuk dibayar</br>
Menampilkan saldo user saat ini</br>
input untuk pin user</br>
pemberitahuan pin terkonfirmasi dan pembayaran berhasil<//br>

![image](https://github.com/PA-DASPRO-Kelompok-13/gameshop/assets/144348757/4460eff5-1610-4fe9-b199-8b812ea48ee5)

## User Isi Saldo
Menampilkan pilihan nominal isi saldo </br>
input pilihan user untuk mengisi saldo </br>
![image](https://github.com/PA-DASPRO-Kelompok-13/gameshop/assets/144348757/4b90b298-7917-46e4-9271-e2971237ae1f)

konfirmasi pengisian saldo</br>
input untuk masukkan pin user</br>
pemberitahuan berhasil top up saldo

![image](https://github.com/PA-DASPRO-Kelompok-13/gameshop/assets/144348757/e1f2b9e8-b94d-4845-bffb-a8bb84956107)



