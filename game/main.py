import os
os.system('cls')
class karakter:
    def __init__(self,name,health,attack,armor,menu,weapon):
        self.name = name
        self.health = health
        self.attack = attack
        self.armor = armor
        self.menu = menu
        self.weapon = weapon
    def serang(self,lawan):
        print(self.name+' menyerang '+lawan.name)
        lawan.diserang(self, self.attack)
    def diserang(self,lawan,attack_lawan):
        print(self.name + ' diserang '+lawan.name)
        damage_diterima = attack_lawan/self.armor
        print('Terkena serangan sebesar : '+str(damage_diterima))
        self.health = self.health - damage_diterima
        print('sisa darah '+self.name,' adalah : '+str(self.health))    
    def equipweapon(self,weaponname):
        self.weaponname = weaponname
        self.attack +=10
        print('\nkamu menggunakan senjata : '+self.weaponname+', dengan stat : attack +10\n')
    def info(self):
        print('Name   : '+self.name)
        print('Health : '+str(self.health))
        print('Attack : '+str(self.attack))
        print('Armor  : '+str(self.armor))
        print('Weapon : '+str(self.weaponname))
    def Getselfhealth(self):
        return self.health
    def Getattackbuff(self):
        self.attack = self.attack + 10
        return self.attack
    def Getarmorbuff(self):
        self.armor = self.armor + 10
        return self.armor
    def Getselfattack(self):
        return self.attack
    def Getselfarmor(self):
        return self .armor
    def Getselfhealthbuff(self):
        self.health = self.health + 10
        return self.health
print('''
*****GAME SIMPEL*****
=====================
1. Start
2. exit
=====================
''')
menu_utama = int(input('Masukkan menu yang diinginkan : '))
while menu_utama != 0: 
    if menu_utama == 1:       
        print('''
Karakter
--------------------
1.buat karakter baru
--------------------
        ''')
        
        player1 = int(input("\nPilih karakter player 1 : "))
        if player1 == 1:
            player1 = karakter(input('\nMasukkan nama karakter player 1 : '),
            int(input('\nJumlah darah : ')),
            int(input('\nJumlah attack : ')),
            int(input('\nJumlah armor : ')),
            print('''
list senjata
---------------
1.Sniper
2.Shotgun
3.smg
---------------
        '''),
            int(input('\nPilih senjata player 1 : ')))
            if player1.weapon == 1:
                player1.equipweapon('sniper')
            elif player1.weapon == 2:
                player1.equipweapon('shotgun')
            elif player1.weapon == 3:
                player1.equipweapon('smg')
            else:
                print('Senjata tidak tersedia')
        else: 
            print('Karakter tidak tersedia ')
        os.system('cls')
        print('\nINFO PLAYER 1')
        player1.info()
        print('''
Karakter
---------------
1.buat karakter baru
---------------
        ''')
        player2 = int(input("\nPilih karakter player 2 : "))
        if player2 == 1:
            player2 = karakter(input('\nMasukkan nama karakter player 2 : '),
            int(input('\nJumlah darah : ')),
            int(input('\nJumlah attack : ')),
            int(input('\nJumlah armor : ')),
            print('''
list senjata
---------------
1.Sniper
2.Shotgun
3.smg
---------------
        '''),
            int(input('\nSenjata yang digunakan : ')))
            if player2.weapon == 1:
                player2.equipweapon('sniper')
            elif player2.weapon == 2:
                player2.equipweapon('shotgun')
            elif player2.weapon == 3:
                player2.equipweapon('smg')
            else:
                print('Senjata tidak tersedia')
        else: 
            print('Karakter tidak tersedia ')
        print('\nINFO PLAYER 2')
        os.system('cls')
        player2.info()
        for i in range(0,10):
            print('\nBabak ke - '+str(i+1)+'\n')
            print('\nGiliran player 1\n')
            print('''
1. Buff Health
2. Buff Attack
3. Buff Armor
        ''')
            player1buff = int(input("\nPilih buff untuk player 1 : "))
            if player1buff == 1:
                    player1.Getselfhealthbuff()
            elif player1buff == 2:
                    player1.Getattackbuff()
            elif player1buff == 3:
                    player1.Getarmorbuff()
            else:
                print('Buff tidak tersedia')
            player1.serang(player2)
            print('\nINFO PLAYER 1')
            player1.info()
            print('\nGiliran player 2\n')
            print('''
1. Buff Health
2. Buff Attack
3. Buff Armor
        ''')
            player2buff = int(input("\nPilih buff untuk player 2 : "))
            if player2buff == 1:
                player2.Getselfhealthbuff()
            elif player2buff == 2:
                player2.Getattackbuff()
            elif player2buff == 3:
                player2.Getarmorbuff()
            else:
                print('Buff tidak tersedia')
            player2.serang(player1)
            print('\nINFO PLAYER 2')
            player2.info()          
    elif menu_utama == 2:
        print("Terimakasih telah menggunakan !")
        break
    else:
        print('Menu tidak tersedia')
    print('\nGame selesai\n')
    if player1.Getselfhealth() > player2.Getselfhealth():
        print('player 1 win')
    else:
        print('player 2 win')
else:
    print('menu tidak tersedia')