import sqlite3
import time
class sarki():

    def __init__(self,isim,sanatci,album,sirket,sure):
        self.isim=isim
        self.sanatci=sanatci
        self.album=album
        self.sirket=sirket
        self.sure=sure

    def __str__(self):
        return("Şarkı İsmi:{} Sanatçı:{} Albüm:{} Şirket:{} Süre(sn):{}".format(self.isim,self.sanatci,self.album,self.sirket,self.sure))

class Veritabani():

    def __init__(self):

        self.baglanti_olustur()

    def baglanti_olustur(self):

        self.con=sqlite3.connect("Şarkılar.db")

        self.cursor=self.con.cursor()

        self.cursor.execute("Create Table If Not Exists Şarkılar(İsim TEXT,Sanatçı TEXT,Albüm TEXT,Şirket TEXT,Süre INT)")

        self.con.commit()

    def baglanti_kes(self):
        self.con.close()
        exit()
    def sureyi_hesapla(self):
        self.cursor.execute("Select * From Şarkılar")
        sure=self.cursor.fetchall()
        toplam=0
        if(len(sure)==0):
            print("Henüz yüklenmiş şarkı bulunmuyor.")
        else:
            for x in sure:
               x=list(x)
               toplam+=x[4]
        dakika=int(toplam/60)
        saniye=toplam%60
        print("Veritabanındaki tüm şarkılar {} saniye----->{} dakika {} saniye".format(toplam,dakika,saniye))
    def sarki_ekle(self,sinif):

        self.cursor.execute("INSERT INTO Şarkılar Values(?,?,?,?,?)",(sinif.isim,sinif.sanatci,sinif.album,sinif.sirket,sinif.sure))

        self.con.commit()


    def sarki_sil(self,isim):

        self.cursor.execute("Delete From Şarkılar where İsim=?",(isim,))

        self.con.commit()

    def sarkilari_goster(self):

        self.cursor.execute("Select * From Şarkılar")
        sark=self.cursor.fetchall()
        if(len(sark)==0):
            print("Sistemde henüz şarkı bulunmamaktadır.")
        else:
            for x in sark:
                yaz=sarki(x[0],x[1],x[2],x[3],x[4])
                print(yaz)
