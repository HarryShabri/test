import mysql.connector
import os
def hapus():
    os.system('cls')

con = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
)

hapus()
mulai = ''
while mulai!=0:
    print("Apa yang ingin kamu lakukan ?")
    print('''
1. Buat Database
2. Database yang sudah ada ''')

    pilih = int(input('Masukkan pilihanmu : '))
    while pilih !=0:
        if pilih == 1:
            nm_db = input('Masukkan nama database yang kamu inginkan : ')
            hapus()
            print(nm_db)
            print('''
1. Yakin? 
2. Batal ''')
            pilih = int(input('\nMasukkan pilihanmu : '))
            if pilih == 1:
                pass
            elif pilih == 2:
                hapus()
                break
            sql = "create database %s"%(nm_db)
            db.execute(sql)
            print("database berhasil dibuat")
        elif pilih == 2: 
            con = mysql.connector.connect(
                host = 'localhost',
                user = input('Masukkan user : '),
                password = input('Masukkan password : '),
                database = input('Masukkan nama database : '))
            db = con.cursor()
            if con.is_connected():
                print('berhasil terhubung dengan database')
                print('\n apa yang ingin kamu lakukan ?')
                print('''
1. memasukkan data 
2. melihat data ''')
                pilih = int(input('Masukkan pilihanmu : '))
                hapus()
                if pilih == 1:
                    print("""


1. buat tabel baru
2. tabel yang yang sudah ada""")
                    sql = "insert into "