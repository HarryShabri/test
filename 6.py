class bangundatar:
    def __init__(self,name,lingakaran,jajar_genjang,persegi,persegi_panjang):
        self.name = name
    def luas(self):
        

class menu:
    def __init__(self,bangun_datar,bangun_ruang):
        self.bangun_datar = bangun_datar
        self.bangun_ruang = bangun_ruang
    def tampilanbd(self):
        print('''
========================================
|| 1. Segitiga                        ||
|| 2. Lingkaran                       ||
|| 3. Jajar genjang                   ||
|| 4. Persegi                         ||
|| 5. Persegi panjang                 ||
|| 6. Kembali                         ||
========================================        
''')
        self.bangun_datar =  int(input('Masukkan menu yang diinginkan : '))
    def tampilanbr(self): 
        print('''
========================================
|| 1. Kubus                           ||
|| 2. Balok                           ||
|| 3. Tabung                          ||
|| 4. Bola                            ||
|| 5. Kerucut                         ||
|| 6. Kembali                         ||
========================================
''')
        self.bangun_ruang = int(input('Masukkan menu yang diinginkan : '))    
