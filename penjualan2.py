print("-----------------  Kasir Rumah Makan naga hitam -----------------")
pembeli = input("Masukkan nama Pembeli: ")
print ("Nama Pembeli :", pembeli) 

def fungsimakanan():
   global totalmkn
   global porsi
   global mkn
   print("========== Menu ==========")
   print("1. Bakso\t\t$.8")
   print("2. Mie Ayam\t\t$.15")
   print("========== Menu ==========", "\n")
   nomor=int(input("Masukan Pilihan: "))
   porsi= int(input("Berapa Porsi: "))
   
   if nomor==1:
       totalmkn=porsi*8
       print (porsi," porsi Bakso = $", totalmkn)
       mkn=("Bakso")
   elif nomor==2:
       totalmkn=porsi*15
       print (porsi," porsi Mie ayam = $", totalmkn)
       mkn=("Mie ayam")
   else:
      print("Pilihan tidak ada, silahkan masukan lagi!!")
      fungsimakanan()

def fungsiminuman():
   global totalmnm
   global mnm
   global gelas
   print("\n----------------- Menu Minuman -----------------")
   print("1. Teh Manis\t\t$.3")
   print("2. Aqua\t\t\t$.0.5")
   nomor=int(input("Masukan Pilihan: "))
   gelas= int(input("Berapa Gelas: "))

   if nomor==1:
       totalmnm=gelas*3
       print (gelas," Teh Manis = $", totalmnm)
       mnm=(" Gelas Teh manis")
   elif nomor==2:
       totalmnm=gelas*0.5
       print (gelas, " Aqua = $", totalmnm)
       mnm=("Aqua")
   else:
      print("Pilihan tidak ada, silahkan masukan lagi!!")
      fungsiminuman()
def fungsibayar():
    global uang
    global kembalian
    uang = int(input('Masukkan uang bayar : $ '))
    totalsemua = totalmnm+totalmkn
    if uang == totalsemua:
        kembalian=0
    elif uang > totalsemua:
        kembalian = uang - totalsemua
    elif uang < totalsemua:
        kembalian = 'Gak cukup woi'
fungsimakanan()
fungsiminuman()
fungsibayar()
totalsemua=totalmkn+totalmnm

print("\nTotal harus Dibayar: Rp",totalsemua)
print("Kembalian :",kembalian)

print("\n==================================")
print("========== S T R U K   P E M B A Y A R A N =========")
print("==================================")
print ("Nama\t\t:",pembeli)
print ("Beli\t\t:",porsi,mkn,"( $", totalmkn,")")
print ("\t\t ",gelas,mnm,"( $", totalmnm,")")
print ("Tagihan\t\t: $",totalsemua)
print ("Dibayar\t\t: $",uang)
print ("Kembalian\t: $0",kembalian)
print("==================================")