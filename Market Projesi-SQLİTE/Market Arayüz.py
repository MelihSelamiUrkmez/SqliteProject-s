import time
from Market import *
print("""
************************************************
*                 MET TEKEL BAYİ               *                                           *
* 1)Ürün Ekle                                  *
* 2)Ürün Sil                                   *
* 3)Ürün Güncelle                              *
* 4)Ürünleri Yazdır                            *
* 5)Fiyat Listesi Oluştur                      *
* 6)Fiyat Öğren                                *
* 7)Stok Yorumla                               *
* 8)Çıkış                                      *
************************************************

""")

veri=Veri()

while(1):
    secim=int(input("Lütfen işlem yapmak istediğiniz numarayı giriniz:"))

    if(secim==8):
        print("Programdan çıkış yapılıyor.")
        time.sleep(2)
        veri.baglanti_kes()
    elif(secim==1):
        isim=input("Eklemek istediğiniz ürünün ismini giriniz:")
        adet=int(input("Eklemek istediğiniz ürünün stok adetini giriniz:"))
        fiyat=float(input("Eklemek istediğiniz ürünün fiyatını giriniz:"))
        urun=Yazdir(isim,adet,fiyat)
        print("Ürün sisteme ekleniyor.Lütfen Bekleyiniz.")
        veri.urun_ekle(urun)
        time.sleep(2)
        print("#Ürün Başarıyla Eklendi.#")
    elif(secim==2):
        isim=input("Silmek istediğiniz ürünün ismini giriniz:")
        veri.urun_sil(isim)
        print("#Ürün Başarıyla Silindi.#")
    elif(secim==3):
        isim=input("Fiyatını güncellemek istediğiniz ürünün ismini giriniz:")
        fiyat=float(input("Yeni fiyatı giriniz:"))
        veri.urun_guncelle(isim,fiyat)
    elif(secim==4):
        print("MET TEKEL DEPO STOK BİLGİLERİ:")
        veri.urunleri_goster()
    elif(secim==5):
        print("MET TEKEL 2021 GÜNCEL SATIŞ LİSTESİ:")
        veri.fiyat_listesi_olustur()
    elif(secim==6):
        isim=input("Fiyatını öğrenmek istediğiniz ürünün ismini giriniz:")
        veri.fiyat_ogren(isim)
    elif(secim==7):
        print("Stoklarınız kontrol ediliyor.Lütfen bekleyiniz.")
        time.sleep(4)
        veri.stok_yorumla()
    else:
        print("Böyle bir seçeneğimiz bulunmamaktadır.")
