#Nama : Dewi Maharani Dyah Pitaloka
#Kelas : JCDSOL - 012

data_barang = [
    {
        'Kode': 'MYF001',
        'Nama': 'Minyak Goreng',
        'Merk': 'Filma',
        'Ukuran': '1 Liter',
        'Stok': 10,
        'Harga Jual': 22000,
        'Harga Beli': 20000
    },
    {
        'Kode': 'MYF002',
        'Nama': 'Minyak Goreng',
        'Merk': 'Filma',
        'Ukuran': '1 Liter',
        'Stok': 15,
        'Harga Jual': 22800,
        'Harga Beli': 22000
    },
    {
        'Kode': 'BRP001',
        'Nama': 'Beras',
        'Merk': 'Puravita',
        'Ukuran': '5 Kg',
        'Stok': 17,
        'Harga Jual': 68900,
        'Harga Beli': 68000
    },
    {
        'Kode': 'BRR001',
        'Nama': 'Beras',
        'Merk': 'Rojolele',
        'Ukuran': '5 Kg',
        'Stok': 20,
        'Harga Jual': 65700,
        'Harga Beli': 64500
    },
    {
        'Kode': 'GPG001',
        'Nama': 'Gula Pasir',
        'Merk': 'Gulaku',
        'Ukuran': '1 Kg',
        'Stok': 50,
        'Harga Jual': 17000,
        'Harga Beli': 16500
    },
    {
        'Kode': 'GPM001',
        'Nama': 'Gula Pasir',
        'Merk': 'Gunungmadu',
        'Ukuran': '1 Kg',
        'Stok': 60,
        'Harga Jual': 16500,
        'Harga Beli': 16000
    },
    {
        'Kode': 'GRG001',
        'Nama': 'Garam',
        'Merk': 'Refina',
        'Ukuran': '200 g',
        'Stok': 70,
        'Harga Jual': 5000,
        'Harga Beli': 4500
    },
]

cart = []

# CRUD
def menampilkanDaftarBarang():
    while True:
        submenu = input('''
        |--------------------Submenu Daftar Barang--------------------|
        |                                                             |
        | 1. Menampilkan Seluruh Data                                 |
        | 2. Menampilkan Data Tertentu                                |
        | 3. Kembali ke Menu Utama                                    |
        |                                                             |
        *-------------------------------------------------------------*
        |Pilih Submenu Yang Ingin Anda Jalankan (1-3) : ''')

        if submenu == '1':
            menampilkanSemuaDaftar()

        elif submenu == '2':
            kode_barang = input('''
            *-------------------------------------------------------------*
            Masukkan Kode Barang: ''').upper()
            for i in range(len(data_barang)):
                if kode_barang == data_barang[i]['Kode']:
                    y = '\n------------------------Data Ditemukan------------------------'
                    break
                else:
                    y = '\n---------------------Data tidak ditemukan---------------------'
            print(y)
            
            if y == '\n------------------------Data Ditemukan------------------------':
                print('\n---------------------------------------------------Berikut Productnya:---------------------------------------------------\n')
                print('-------------------------------------------------------------------------------------------------------------------------')
                print('| {:9} | {:15} | {:11} | {:9} | {:10} | {:11} | {:12} |'.format('Kode Barang', 'Nama Barang', 'Merk', 'Ukuran', 'Stok', 'Harga Jual', 'Harga Beli'))
                print('| {:9} | {:11} | {:15} | {:11} | {:9} | {:10} | {:12} | {:19} |'.format(i,data_barang[i]['Kode'], data_barang[i]['Nama'], data_barang[i]['Merk'], data_barang[i]['Ukuran'], data_barang[i]['Stok'], data_barang[i]['Harga Jual'], data_barang[i]['Harga Beli']))

        elif submenu == '3':
             break

        else:
            print('''
            ----------------Pilihan Yang Anda Masukkan Salah --------------
            ''')

def menampilkanSemuaDaftar():
    print('------------------------------------------------Daftar Barang Keseluruhan------------------------------------------------')
    print('| {:9} | {:9} | {:15} | {:11} | {:9} | {:10} | {:12} | {:12}'.format('Nomor', 'Kode Barang', 'Nama Barang', 'Merk', 'Ukuran', 'Stok', 'Harga Jual', 'Harga Beli'))

    for i in range(len(data_barang)):
        print('| {:9} | {:11} | {:15} | {:11} | {:9} | {:10} | {:12} | {:19} |'.format(i,data_barang[i]['Kode'], data_barang[i]['Nama'], data_barang[i]['Merk'], data_barang[i]['Ukuran'], data_barang[i]['Stok'], data_barang[i]['Harga Jual'], data_barang[i]['Harga Beli']))

def tambahDataBarang():
    while True:
        submenu = input('''
        |-----------------Submenu Tambah Daftar Barang----------------|
        |                                                             |
        | 1. Tambah Data Baru                                         |
        | 2. Kembali Ke Menu Utama                                    |
        |                                                             |
        *-------------------------------------------------------------*
        |Pilih Submenu Yang Ingin Anda Jalankan (1-2) : ''')

        if submenu == '1':
            print('''
            *-------------------------------------------------------------*''')
            while True:
                kode_baru = input('\tMasukkan Kode Yang Baru : ').upper()
                duplikat_kode = any(barang['Kode'].upper() == kode_baru for barang in data_barang)

                if duplikat_kode:
                    print('''
                    --------Kode Barang Sudah Ada. Harap Memasukkan Kode Baru------
                    ''')
                else:
                    nama_baru = input('\tMasukkan Nama Barang: ').capitalize()
                    merk_baru = input('\tMasukkan Merk: ').capitalize()
                    ukuran_baru = input('\tMasukkan Ukuran Barang: ').capitalize()

                    # Memastikan input stok adalah angka
                    while True:
                        try:
                            stok_baru = int(input('\tMasukkan Jumlah Stok Barang: '))
                            break
                        except ValueError:
                            print('''
                                -----Inputan Hanya Boleh Berupa Angka dan Bernilai Positif-----
                                ''')

                    # Memastikan input harga jual adalah angka
                    while True:
                        try:
                            harga_jual_baru = int(input('\tMasukkan Harga Jual Barang (Rp): '))
                            break
                        except ValueError:
                            print('''
                                -----Inputan Hanya Boleh Berupa Angka dan Bernilai Positif-----
                                ''')

                    # Memastikan input harga beli adalah angka
                    while True:
                        try:
                            harga_beli_baru = int(input('\tMasukkan Harga Beli Barang (Rp) : '))
                            break
                        except ValueError:
                            print('''
                                -----Inputan Hanya Boleh Berupa Angka dan Bernilai Positif-----
                                ''')

                    while True:
                        konfirmasi = input('\tApakah Anda Yakin Ingin Menyimpan Data? (Y/N): ').upper()
                        if konfirmasi == 'N':
                            print('''
                            --------------------Data Tidak Ditambahkan---------------------
                            ''')
                            break
                        elif konfirmasi == 'Y':
                            data_barang.append({
                                'Kode': kode_baru,
                                'Nama': nama_baru,
                                'Merk': merk_baru,
                                'Ukuran': ukuran_baru,
                                'Stok': stok_baru,
                                'Harga Jual': harga_jual_baru,
                                'Harga Beli': harga_beli_baru,
                            })
                            print('''
                            --------------------Data Berhasil Ditambahkan------------------
                            ''')
                            menampilkanSemuaDaftar()

                            break
                        else:
                            print('''
                            ----------------Pilihan Yang Anda Masukkan Salah --------------
                            ''')

                    break
            else:
                continue

        elif submenu == '2':
            break

        else:
            print('''
            ----------------Pilihan Yang Anda Masukkan Salah --------------
            ''')

def updateDataBarang():
    while True:
        submenu = input('''
        |-----------------Submenu Update Daftar Barang----------------|
        |                                                             |
        | 1. Update Data                                              |
        | 2. Kembali Ke Menu Utama                                    |
        |                                                             |
        *-------------------------------------------------------------*
        |Pilih Submenu Yang Ingin Anda Jalankan (1-2) : ''')

        if submenu == '1':

            print('''
            *-------------------------------------------------------------*''')
            kode_barang = input("\tMasukkan Kode Barang Yang Ingin Diupdate: ").upper()
            data_ditemukan = False

            for barang in data_barang:
                if barang['Kode'].upper() == kode_barang:
                    print('-------------------------------------------------------------------------------------------------------------------------')
                    print('| {:9} | {:15} | {:11} | {:9} | {:10} | {:11} | {:12}'.format('Kode Barang', 'Nama Barang', 'Merk', 'Ukuran', 'Stok', 'Harga Jual', 'Harga Beli'))
                    print('| {:11} | {:15} | {:11} | {:9} | {:10} | {:12} | {:19} |'.format(barang['Kode'], barang['Nama'], barang['Merk'], barang['Ukuran'], barang['Stok'], barang['Harga Jual'], barang['Harga Beli']))
                    data_ditemukan = True

            if data_ditemukan:
                while True:
                    konfirmasi = input('''
                        
                        Ingin Mengupdate Info Barang? (Y/N): ''').lower()
                    
                    if konfirmasi == 'n':
                        print('''
                            -----------------Info Barang Tidak di Update----------------
                            ''')
                        
                        break

                    if konfirmasi == 'y':
                        print('*-------------------------------------------------------------*')
                        subsubmenu = input('''
                        Masukkan Kolom Data Yang Ingin Di Update: ''').lower()

                        if subsubmenu == 'kode barang':
                            barang['Kode'] = input('''
                            Masukkan Kode Barang Terbaru: ''').upper()
                            print('-------------------------------------------------------------------------------------------------------------------------')
                            print('| {:9} | {:15} | {:11} | {:9} | {:10} | {:11} | {:12}'.format('Kode Barang', 'Nama Barang', 'Merk', 'Ukuran', 'Stok', 'Harga Jual', 'Harga Beli'))
                            print('| {:11} | {:15} | {:11} | {:9} | {:10} | {:12} | {:19} |'.format(barang['Kode'], barang['Nama'], barang['Merk'], barang['Ukuran'], barang['Stok'], barang['Harga Jual'], barang['Harga Beli']))
                            print('''
                            --------------Kode Barang Sudah Berhasil di Update-------------
                            ''')
                                
                        elif subsubmenu == 'nama barang':
                            barang['Nama'] = input('''
                            Masukkan Nama Barang Terbaru: ''').capitalize()
                            print('-------------------------------------------------------------------------------------------------------------------------')
                            print('| {:9} | {:15} | {:11} | {:9} | {:10} | {:11} | {:12}'.format('Kode Barang', 'Nama Barang', 'Merk', 'Ukuran', 'Stok', 'Harga Jual', 'Harga Beli'))
                            print('| {:11} | {:15} | {:11} | {:9} | {:10} | {:12} | {:19} |'.format(barang['Kode'], barang['Nama'], barang['Merk'], barang['Ukuran'], barang['Stok'], barang['Harga Jual'], barang['Harga Beli']))
                            print('''
                            --------------Nama Barang Sudah Berhasil di Update-------------
                            ''')

                        elif subsubmenu == 'merk':
                            barang['Merk'] = input('''
                            Masukkan Merk Barang Terbaru: ''').capitalize()
                            print('-------------------------------------------------------------------------------------------------------------------------')
                            print('| {:9} | {:15} | {:11} | {:9} | {:10} | {:11} | {:12}'.format('Kode Barang', 'Nama Barang', 'Merk', 'Ukuran', 'Stok', 'Harga Jual', 'Harga Beli'))
                            print('| {:11} | {:15} | {:11} | {:9} | {:10} | {:12} | {:19} |'.format(barang['Kode'], barang['Nama'], barang['Merk'], barang['Ukuran'], barang['Stok'], barang['Harga Jual'], barang['Harga Beli']))
                            print('''
                            ---------------Merk Barang Sudah Berhasil di Update------------
                            ''')

                        elif subsubmenu == 'ukuran':
                            barang['Ukuran'] = input('''
                            Masukkan Ukuran Barang Terbaru [Jumlah + Satuan Unit Metrik]: ''').capitalize()
                            print('-------------------------------------------------------------------------------------------------------------------------')
                            print('| {:9} | {:15} | {:11} | {:9} | {:10} | {:11} | {:12}'.format('Kode Barang', 'Nama Barang', 'Merk', 'Ukuran', 'Stok', 'Harga Jual', 'Harga Beli'))
                            print('| {:11} | {:15} | {:11} | {:9} | {:10} | {:12} | {:19} |'.format(barang['Kode'], barang['Nama'], barang['Merk'], barang['Ukuran'], barang['Stok'], barang['Harga Jual'], barang['Harga Beli']))
                            print('''
                            --------------Ukuran Barang Sudah Berhasil di Update-----------
                            ''')

                        elif subsubmenu == 'stok':
                            while True:
                                try:
                                    barang['Stok'] = int(input('''
                                        Masukkan Jumlah Stok Barang Terbaru: '''))
                                    print('-------------------------------------------------------------------------------------------------------------------------')
                                    print('| {:9} | {:15} | {:11} | {:9} | {:10} | {:11} | {:12}'.format('Kode Barang', 'Nama Barang', 'Merk', 'Ukuran', 'Stok', 'Harga Jual', 'Harga Beli'))
                                    print('| {:11} | {:15} | {:11} | {:9} | {:10} | {:12} | {:19} |'.format(barang['Kode'], barang['Nama'], barang['Merk'], barang['Ukuran'], barang['Stok'], barang['Harga Jual'], barang['Harga Beli']))
                                    print('''
                                    ---------------Stok Barang Sudah Berhasil di Update------------
                                    ''')
                                    break
                                except ValueError:
                                    print('''
                                            -----Inputan Hanya Boleh Berupa Angka dan Bernilai Positif-----
                                            ''')
                            continue

                        elif subsubmenu == 'harga jual':
                            while True:
                                try:
                                    barang['Harga Jual'] = int(input('''
                                    Masukkan Harga Jual Terbaru (Rp): '''))
                                    print('-------------------------------------------------------------------------------------------------------------------------')
                                    print('| {:9} | {:15} | {:11} | {:9} | {:10} | {:11} | {:12}'.format('Kode Barang', 'Nama Barang', 'Merk', 'Ukuran', 'Stok', 'Harga Jual', 'Harga Beli'))
                                    print('| {:11} | {:15} | {:11} | {:9} | {:10} | {:12} | {:19} |'.format(barang['Kode'], barang['Nama'], barang['Merk'], barang['Ukuran'], barang['Stok'], barang['Harga Jual'], barang['Harga Beli']))
                                    print('''
                                    ---------------Harga Jual Sudah Berhasil di Update--------------
                                    ''')
                                    break
                                except ValueError:
                                    print('''
                                            -----Inputan Hanya Boleh Berupa Angka dan Bernilai Positif-----
                                            ''')

                        elif subsubmenu == 'harga beli':
                            while True:
                                try:
                                    barang['Harga Beli'] = int(input('''
                                    Masukkan Harga Beli Terbaru (Rp): '''))
                                    print('-------------------------------------------------------------------------------------------------------------------------')
                                    print('| {:9} | {:15} | {:11} | {:9} | {:10} | {:11} | {:12}'.format('Kode Barang', 'Nama Barang', 'Merk', 'Ukuran', 'Stok', 'Harga Jual', 'Harga Beli'))
                                    print('| {:11} | {:15} | {:11} | {:9} | {:10} | {:12} | {:19} |'.format(barang['Kode'], barang['Nama'], barang['Merk'], barang['Ukuran'], barang['Stok'], barang['Harga Jual'], barang['Harga Beli']))
                                    print('''
                                    ---------------Harga Beli Sudah Berhasil di Update--------------
                                    ''')
                                    break
                                except ValueError:
                                    print('''
                                            -----Inputan Hanya Boleh Berupa Angka dan Bernilai Positif-----
                                            ''')
                        
                        else:
                            print('''
                            ---Nama Kolom Yang Anda Masukkan Salah. Harap Masukkan Nama Kolom Yang Benar---
                            ''')

                    else:
                        print('''
                        ----------------Pilihan Yang Anda Masukkan Salah --------------
                        ''')
            else:
                print('''
                ---Kode Barang Tidak Ditemukan. Harap Memasukkan Nama atau Kode Yang Sudah Terdaftar---
                ''')

        elif submenu == '2':
            break

        else:
            print('''
            ----------------Pilihan Yang Anda Masukkan Salah --------------
            ''')
  
def hapusDataBarang():
    while True:
        submenu = input('''
        |------------------Submenu Hapus Data Barang------------------|
        |                                                             |
        | 1. Hapus Data                                               |
        | 2. Kembali Ke Menu Utama                                    |
        |                                                             |
        *-------------------------------------------------------------*
        |Pilih Submenu Yang Ingin Anda Jalankan (1-2) : ''')

        if submenu == '1':
            kode_barang = input("Masukkan Kode Barang Yang Ingin Dihapus: ").upper()
            data_ditemukan = False

            for barang in data_barang:
                if kode_barang == barang['Kode']:
                    data_ditemukan = True
                    break

            if data_ditemukan:
                print('-------------------------------------------------------------------------------------------------------------------------')
                print('| {:9} | {:15} | {:11} | {:9} | {:10} | {:11} | {:12}'.format('Kode Barang', 'Nama Barang', 'Merk', 'Ukuran', 'Stok', 'Harga Jual', 'Harga Beli'))
                print('| {:11} | {:15} | {:11} | {:9} | {:10} | {:12} | {:19} |'.format(barang['Kode'], barang['Nama'], barang['Merk'], barang['Ukuran'], barang['Stok'], barang['Harga Jual'], barang['Harga Beli']))

                while True:
                    konfirmasi = input("\n Apakah Anda Yakin Ingin Menghapus Data Ini? (Y/N): ").lower()
                    if konfirmasi == 'y':
                        index_dihapus = data_barang.index(barang)
                        del data_barang[index_dihapus]
                        print('''
                        -----------------Barang Telah Berhasil Dihapus-----------------
                        
                        ''')
                        menampilkanSemuaDaftar()

                        break
                    elif konfirmasi == 'n':
                        print('''
                        ---------------------Barang Tidak Dihapus----------------------
                        ''')
                        break
                    else:
                        print('''
                        ----------------Pilihan Yang Anda Masukkan Salah --------------
                        ''')
            else:
                print('''
                Kode Barang Tidak Ditemukan. Harap Memasukkan Kode Yang Sudah Terdaftar.
                ''')

        elif submenu == '2':
            break

        else:
            print('''
            ----------------Pilihan Yang Anda Masukkan Salah --------------
            ''')

# FITUR TAMBAHAN
    while True:
        submenu = input('''
        |---------------Submenu Hitung Omzet Sisa Stok----------------|
        |                                                             |
        | 1. Hitung Omzet Keseluruhan Sisa Stok                       |
        | 2. Hitung Omzet Sisa Stok Berdasarkan Nama atau Kode Barang |
        | 3. Kembali Ke Menu Utama                                    |
        |                                                             |
        *-------------------------------------------------------------*
        |Pilih Submenu Yang Ingin Anda Jalankan (1-3) : ''')

        if submenu == '1':
            menampilkanSemuaDaftar()
            
            total_omzet = hitungOmzetList(data_barang)
            print('-------------------------------------------------------------------------------------------')
            print('''
                | Omzet Keseluruhan Sisa Stok = Jumlah Total dari Jumlah Stok * (Harga Jual - Harga Beli)
                | Omzet Keseluruhan Yang Akan Didapat dari Sisa Stok = {}
                '''.format(total_omzet))
            print('-------------------------------------------------------------------------------------------')

        elif submenu == '2':
            kode_barang = input('''
            *-------------------------------------------------------------*
            Masukkan Kode Barang Yang Ingin Dihitung Omzetnya: ''').upper()
            data_ditemukan = False
            list_barang_ditampilkan = []

            for barang in data_barang:
                if barang['Kode'].upper() == kode_barang or barang['Nama'].upper() == kode_barang.upper():
                    list_barang_ditampilkan.append(barang)
                    data_ditemukan = True

            if data_ditemukan:
                print('-------------------------------------------------------------------------------------------------------------------------')
                print('| {:9} | {:15} | {:11} | {:9} | {:10} | {:11} | {:12} |'.format('Kode Barang', 'Nama Barang', 'Merk', 'Ukuran', 'Stok', 'Harga Jual', 'Harga Beli'))
                for barang in list_barang_ditampilkan:
                    print('| {:11} | {:15} | {:11} | {:9} | {:10} | {:12} | {:19} |'.format(barang['Kode'], barang['Nama'], barang['Merk'], barang['Ukuran'], barang['Stok'], barang['Harga Jual'], barang['Harga Beli']))

                omzet_barang_ditampilkan = hitungOmzetList(list_barang_ditampilkan)

                print('-------------------------------------------------------------------------------------------')
                print('''
                    | Omzet Keseluruhan Sisa Stok = Jumlah Stok * (Harga Jual - Harga Beli)
                    | Omzet Keseluruhan Yang Akan Didapatkan Dari Sisa Stok = {}
                '''.format(omzet_barang_ditampilkan))
                print('-------------------------------------------------------------------------------------------')
            else:
                print('''
                ---------------------Data tidak ditemukan---------------------
                ''')

        elif submenu == '3':
            break

        else:
            print('''
            ----------------Pilihan Yang Anda Masukkan Salah --------------
            ''')

def membeliBarang():
    menampilkanSemuaDaftar()

    while True:
        index_barang = input('''
        *-------------------------------------------------------------*
        Masukkan Nomor Barang Yang Ingin Dibeli : ''')

        if not index_barang.isdigit() or int(index_barang) < 0 or int(index_barang) >= len(data_barang):
            print("Nomor barang tidak valid. Mohon masukkan nomor yang sesuai.")
            continue

        index_barang = int(index_barang)

        jumlah_beli = input('''
        *-------------------------------------------------------------*
        Masukkan Jumlah Barang Yang Ingin Dibeli : ''')

        if not jumlah_beli.isdigit() or int(jumlah_beli) <= 0:
            print("Jumlah barang tidak valid. Mohon masukkan jumlah yang sesuai.")
            continue

        jumlah_beli = int(jumlah_beli)

        if jumlah_beli > data_barang[index_barang]['Stok']:
            print('''
            *-------------------------------------------------------------*
            Stok tidak cukup, stok {} tinggal {}
            *-------------------------------------------------------------*'''.format(data_barang[index_barang]['Nama'], data_barang[index_barang]['Stok']))
        else:
            cart.append({
                'Nama': data_barang[index_barang]['Nama'],
                'Jumlah': jumlah_beli,
                'Harga': data_barang[index_barang]['Harga Jual'],
                'index': index_barang
            })

            print('''
            ************** Isi Belanjaan **************''')
            print('| {:15} | {:11} | {:12} |'.format('Nama', 'Jumlah', 'Harga'))

            for item in cart:
                print(f"| {item['Nama']:15} | {item['Jumlah']:11} | {item['Harga']:12} |")

            konfirmasi = input('''
            *-------------------------------------------------------------*
            Mau beli yang lain? (Y/T) = ''').lower()
            if konfirmasi == 't':
                break

    print('''
    -------------------Daftar Belanja--------------------''')
    print('| {:15} | {:11} | {:12} |{:12} |'.format('Nama', 'Jumlah', 'Harga', 'Total Harga'))
    totalHarga = 0
    for item in cart:
        print(f"| {item['Nama']:15} | {item['Jumlah']:11} | {item['Harga']:12} |{item['Jumlah'] * item['Harga']:12} |")

        totalHarga += item['Jumlah'] * item['Harga']

    while True:
        print('''*-------------------------------------------------------------*
        Total Yang Harus Dibayar = {}'''.format(totalHarga))
        jumlahUang = input('''
        *-------------------------------------------------------------*
        Masukkan jumlah uang : ''')

        if not jumlahUang.isdigit() or int(jumlahUang) < totalHarga:
            print("Jumlah uang tidak valid. Mohon masukkan jumlah yang cukup.")
            continue

        jumlahUang = int(jumlahUang)

        if jumlahUang > totalHarga:
            kembalian = jumlahUang - totalHarga
            print('''****** Terima kasih ******
            Uang kembali anda : {} 
            ******************************'''.format(kembalian))
            for item in cart:
                data_barang[item['index']]['Stok'] -= item['Jumlah']
            cart.clear()
            break
        elif jumlahUang == totalHarga:
            print('********************** Terima kasih **********************')
            for item in cart:
                data_barang[item['index']]['Stok'] -= item['Jumlah']
            cart.clear()
            break


# MENU UTAMA
def mainmenu():
    while True:
        pilihmainmenu = input('''
        |*** Selamat Datang di Aplikasi Penjualan Sembako Maharani ***|
        |======================== Menu Utama: ========================|
        |                                                             |        
        | 1. Menampilkan Daftar Barang                                |
        | 2. Tambah Data Barang                                       |
        | 3. Update Data Barang                                       |
        | 4. Hapus Data Barang                                        |
        | 5. Membeli Barang                                           | 
        | 6. Keluar Program                                           |
        *-------------------------------------------------------------*
        |Pilih Menu Yang Ingin Anda Jalankan (1-6) :''')

        if pilihmainmenu == '1':
            menampilkanDaftarBarang()
        elif pilihmainmenu == '2':
            tambahDataBarang()
        elif pilihmainmenu == '3':
            updateDataBarang()
        elif pilihmainmenu == '4':
            hapusDataBarang()
        elif pilihmainmenu == '5':
            membeliBarang()
        elif pilihmainmenu == '6':
            print('''
            ----------------------KELUAR-----------------------
            ********Anda Telah Keluar Dari Aplikasi Ini********
            ****Terimakasih Telah Menggunakan Aplikasi Ini*****
            ''')
            break
        else:
            print('''
            ----------------Pilihan Yang Anda Masukkan Salah--------------
            ''')

mainmenu()

