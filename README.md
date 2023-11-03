# GAMESHOP

GameShop adalah sebuah sistem untuk membeli dan bermain game online. Aplikasi ini memungkinkan pengguna untuk membeli game, melakukan top-up saldo, dan juga memungkinkan admin untuk mengelola game dan pengguna. Program ini dibangun menggunakan bahasa pemrograman Python dan memanfaatkan beberapa modul&library.


## Module & Library
1. `import os`: Digunakan untuk berinteraksi dengan sistem operasi.

2. `import json`: Digunakan untuk mengakses data JSON.

3. `import pwinput`: Digunakan untuk menampilkan **** untuk input kata sandi.

4. `from prettytable import PrettyTable`: Digunakan untuk membuat tabel rapi dalam teks.

5. `from datetime import datetime` : untuk menampilkan tanggal dan waktu saat cetak invoice.
```python
import os
from datetime import datetime
import json 
import pwinput
from prettytable import PrettyTable
```
## Struktur Program

![FLOWCHART SISTEM PEMBELIAN GAME ONLINE-Page-1 drawio](https://github.com/PA-DASPRO-Kelompok-13/gameshop/assets/144348757/feda8ef3-6ab4-4eea-a2bc-c98c57001a8f)


## Fungsi Utama Program

Program GameShop memiliki beberapa fungsi utama, di antaranya:

1. Daftar & Login:

    - Fungsi Daftar digunakan oleh pengguna untuk membuat akun baru.
    - Fungsi Login memungkinkan pengguna untuk masuk ke akun mereka.

2. Transaksi:

    - Pengguna dapat melakukan transaksi pembelian game.
    - Pengguna dapat melakukan top-up saldo akun mereka.

3. Admin CRUD:

    - Admin dapat menambahkan, mengedit, dan menghapus game dari daftar yang tersedia.
    - Admin dapat mengelola pengguna, seperti menghapus akun atau mengubah status pengguna.

## Fitur

- Pengguna:

  - Daftar: Pengguna dapat mendaftar.
  - Login: Pengguna dapat masuk ke akun mereka.
  - Melihat daftar game yang tersedia.
  - Isi Saldo
  - Membeli Game
- Admin
  - Menambah game: Admin dapat menambahkan game baru ke dalam sistem.
  - Melihat game: Admin dapat melihat daftar game yang tersedia 
  - Mengedit game: Admin dapat mengedit informasi game yang ada.
  - Menghapus game: Admin dapat menghapus game dari sistem.
  - Mengelola pengguna/admin/game : Admin dapat melihat, menambahkan, mengedit, dan menghapus data pengguna, admin dan game
