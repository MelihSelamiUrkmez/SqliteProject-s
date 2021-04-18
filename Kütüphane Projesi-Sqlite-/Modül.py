import sqlite3
import time

class Kitap():

    def __init__(self,isim,yazar,yayinevi,tur,baski):
        self.isim=isim
        self.yazar=yazar
        self.yayinevi=yayinevi
        self.tur=tur
        self.baski=baski

    def __str__(self):
        return ("Kitap Adı:{} Kitap Yazarı:{} Yayınevi={} Tür:{} Baskı:{}".format(self.isim,self.yazar,self.yayinevi,self.tur,self.baski))

class Kutuphane():

    def __init__(self):

        self.baglanti_olustur()

    def baglanti_olustur(self):

        self.con=sqlite3.connect("Kütüphane.db")

        self.cursor=self.con.cursor()

        komut="Create Table If Not Exists Kitaplar(İsim TEXT,Yazar TEXT,Yayınevi TEXT,Tür TEXT,Baskı INT)"

        self.cursor.execute(komut)

        self.con.commit()

    def baglanti_kopar(self):

        self.con.close()

    def kitaplari_goster(self):

        self.cursor.execute("Select * From Kitaplar")

        kitap=self.cursor.fetchall()

        if(len(kitap)==0):
            print("Henüz kütüphanede kitap bulunmamaktadır.")
        else:
            for x in kitap:
                string=Kitap(x[0],x[1],x[2],x[3],x[4])
                print(string)
    def kitap_sorgula(self,isim):

        self.cursor.execute("Select * From Kitaplar where İsim=?",(isim,))

        yer=self.cursor.fetchall()

        if(len(yer)==0):
            print("Böyle bir kitap bulunamadı.")
        else:
            kitap=Kitap(yer[0][0],yer[0][1],yer[0][2],yer[0][3],yer[0][4])
            print(kitap)
    def kitap_ekle(self,sinif):

        self.cursor.execute("INSERT INTO Kitaplar Values(?,?,?,?,?)",(sinif.isim,sinif.yazar,sinif.yayinevi,sinif.tur,sinif.baski))

        self.con.commit()

    def kitap_sil(self,isim):

        self.cursor.execute("Delete From Kitaplar where İsim=?",(isim,))
        self.con.commit()

    def baski_arttir(self,isim):

        self.cursor.execute("Select * From Kitaplar where İsim=?",(isim,))

        kitap=self.cursor.fetchall()

        if(len(kitap)==0):
            print("Böyle bir kitap bulunamadı.")
        else:
            baski=kitap[0][4]
            baski+=1
            self.cursor.execute("Update Kitaplar set Baskı=? where İsim=?",(baski,isim))

            self.con.commit()







