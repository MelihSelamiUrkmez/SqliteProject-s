import sqlite3

class Yazdir():

    def __init__(self,isim,stok,fiyat):
        self.isim=isim
        self.stok=stok
        self.fiyat=fiyat
    def __str__(self):
        return("Ürün:{} Stok{} Satış Fiyatı:{}".format(self.isim,self.stok,self.fiyat))

class Veri():

    def __init__(self):
        self.baglanti_olustur()

    def baglanti_olustur(self):

        self.con=sqlite3.connect("Ürünler.db")

        self.cursor=self.con.cursor()

        self.cursor.execute("CREATE TABLE IF NOT EXISTS Ürünler(İsim TEXT,Stok INT,Fiyat INT)")

        self.con.commit()
    def baglanti_kes(self):
        self.con.close()
        exit()
    def urunleri_goster(self):

        self.cursor.execute("Select * From Ürünler")

        urun=self.cursor.fetchall()

        if(len(urun)==0):
            print("Henüz daha ürün girişi yapılmadı.")
        else:
            for x in urun:
                sinif=Yazdir(x[0],x[1],x[2])
                print(sinif)
    def fiyat_ogren(self,isim):
        self.cursor.execute("Select * From Ürünler where İsim=?",(isim,))
        fiyat=self.cursor.fetchall()
        if(len(fiyat)==0):
            print("Mağazamızda böyle bir ürün bulunmamaktadır.")
        else:
            print("Ürünün satış fiyatı:{}".format(fiyat[0][2]))
    def stok_yorumla(self):

        self.cursor.execute("Select * From Ürünler")

        stok=list(self.cursor.fetchall())

        if(len(stok)==0):
            print("Depoda ürün bulunmuyor.")
        else:
            for x in stok:
                if(x[1]<10):
                    print("{} Ürünün stoğu 10un altına düşmüş.Sipariş VER!".format(x[0],))
                else:
                    print("{} Ürünün stoğu iyi durumda.".format(x[0],))
    def fiyat_listesi_olustur(self):
        self.cursor.execute("Select İsim,Fiyat From Ürünler")
        liste=list(self.cursor.fetchall())

        for x in liste:
            print("{} Ürününün Satış Fiyatı={}".format(x[0],x[1]))
    def urun_ekle(self,sinif):
        self.cursor.execute("INSERT INTO Ürünler Values(?,?,?)",(sinif.isim,sinif.stok,sinif.fiyat))
        self.con.commit()
    def urun_sil(self,isim):
        self.cursor.execute("Select * From Ürünler where İsim=?",(isim,))
        urun=self.cursor.fetchall()
        if(len(urun)==0):
            print("Böyle bir ürün bulunmuyor.")
        else:
            self.cursor.execute("Delete From Ürünler where İsim=?",(isim,))
            self.con.commit()
    def urun_guncelle(self,isim,fiyat):
        self.cursor.execute("Select * From Ürünler where İsim=?",(isim,))
        urun=self.cursor.fetchall()
        guncel=urun[0][2]
        guncel=(guncel-urun[0][2])+fiyat
        if(len(urun)==0):
            print("Depoda böyle bir ürün bulunmuyor.")
        else:
            self.cursor.execute("Update Ürünler set Fiyat=? where İsim=?",(guncel,isim))
            self.con.commit()
