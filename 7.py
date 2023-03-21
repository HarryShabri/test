class bangundatar:
    def __init__(self,name):
        self.name = name
    def luaspersegi(self,sisi):
        luas = sisi * sisi
        print('luas '+self.name+' adalah ',luas)
    def kelilingpersegi(self,sisi):
        keliling = 4 * sisi
        return(keliling)
    def luaspersegipanjang(self,panjang, lebar):
        luas = panjang * lebar
        print('luas '+self.name+' adalah ',luas)
    def kelilingpersegipanjang(self,panjang, lebar):
        keliling = 2*(panjang+lebar)
        return(keliling)
    def luassegitiga(self,alas, tinggi):
        luas = 0.5*alas*tinggi
        print('luas '+self.name+' adalah ',luas)
    def kelilingsegitiga(self,sisi1, sisi2, sisi3):
        keliling = sisi1+sisi2+sisi3
        return(keliling)
    def luaslingkaran(self,r):
        luas = 3.14*r*r
        return(luas)
    def kelilinglingkaran(self,r):
        keliling = 2*3.14*r
        print('keliling '+self.name+' adalah ',keliling)
    def luasjajargenjang(self,alas, tinggi):
        luas = alas*tinggi
        print('luas '+self.name+' adalah ',luas)
    def kelilingjajargenjang(self,alas, sisimiring):
        keliling = 2*(alas+sisimiring)
        print('keliling '+self.name+' adalah ',keliling)

