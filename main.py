import os
from time import sleep
sleep(0)
os.system("cls")

# Bakso Slamet Cabang Californiaaaaaa

# Awal
print("="*28)
print("\tBakso Slamet\t")
print("="*28, "\n")

# Welcome
print("Hello, Welcome to Bakso Slamet")
print("can i know u name sir?")
nama = input("Nama Pembeli : ")
print("mau pesan apa hari ini "+ nama, "\n")

# Menu
print("========== Menu ==========")
print("1. Bakso\t\t$.8")
print("2. Mie Ayam\t\t$.15")
print("3. Teh Manis\t\t$.3")
print("4. Aqua\t\t\t$.0.5")
print("========== Menu ==========", "\n")

# Variable menu
h = []
a = 1

# Pilih menu
def fgsmenu():
    menu = int(input("Masukan Pesanan [1/2/3/4] : "))
    if menu == 1:
        price = 8
    elif menu == 2:
        price = 15
    elif menu == 3:
        price = 3
    elif menu == 4:
        price = 0.5
    else:
        while True:
            print("Menu tidak ada")
            if menu == 1 or menu == 2 or menu == 3 or menu == 4:
                if menu == 1:
                    price = 8
                elif menu == 2:
                    price = 15
                elif menu == 3:
                    price = 3
                elif menu == 4:
                    price = 0.5
            break
        fgsmenu()
fgsmenu()

# Jumlah pembelian
order = int(input("Masukan jumlah order : "))

for i in range(order):
    h.append(price)

# Tambah menu
def tmbhmenu():
    while True:
        q = input("Apakah ada yang ingin di tambah kan? [Y/N] : ")
        if q == "y":
            y = int(input("Masukan Pesanan [1/2/3/4] : "))
            if q == 1:
                price = 8
            elif q == 2:
                price = 15
            elif q == 3:
                price = 3
            elif q == 4:
                price = 0.5
            tambah = int(input("Masukan jumlah order : "))
            for i in range(order):
                h.append(price)
            c = tambah + order
            print("Total pesanan : ", c)
            pay = sum(h)
            print("Total pembayaran : $.{}" .format(pay))
        else:
            pay = sum(h)
            print("Total pesanan : ", order)
            print("Total pembayaran : $.{}" .format(pay))
            break
tmbhmenu()

