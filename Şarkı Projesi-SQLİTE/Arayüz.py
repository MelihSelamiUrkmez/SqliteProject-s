from Sarki import *


print("""
------------------------------------------------
|            TUBİDY ŞARKI PROGRAMI             |
|                                              |
| 1--->Şarkı Ekle                              |
|                                              |
| 2--->Şarkı Sil                               |
|                                              |
| 3--->Şarkı Sürelerini Hesapla                |
|                                              |
| 4--->Şarkıları Göster                        |
------------------------------------------------
""")

veri=Veritabani()

while(1):
    islem=input("İşlem yapacağınız numarayı giriniz(Çıkmak için 'q' tuşuna basınız):")

    if(islem=="q"):
        print("Oturumunuz Sonlandırılıyor...")
        time.sleep(2)
        print("Tekrar Bekleriz.")
        veri.baglanti_kes()
        exit()
    elif(islem=="1"):
        isim=input("Eklemek istediğiniz şarkının ismini giriniz:")
        sanatci=input("Eklemek istediğiniz şarkının sanatçısını giriniz:")
        album=input("Eklemek istediğiniz şarkının albümünü giriniz:")
        sirket=input("Eklemek istediğiniz şarkının şirketini giriniz:")
        sure=int(input("Eklemek istediğiniz şarkının süresini sn cinsinden giriniz:"))
        clas=sarki(isim,sanatci,album,sirket,sure)
        print("Bilgiler sisteme ekleniyor.Lütfen bekleyiniz..")
        time.sleep(2)
        veri.sarki_ekle(clas)
        print("Şarkı başarı ile sisteme aktarıldı.")
    elif(islem=="2"):
        isim=input("Silmek istediğiniz şarkının ismini giriniz:")

        print("-----Sarki Siliniyor-----")
        time.sleep(2)
        veri.sarki_sil(isim)
    elif(islem=="3"):
        print("Veride bulunan şarkı süreleri hesaplanıyor.Lütfen Bekleyiniz...")

        time.sleep(4)

        veri.sureyi_hesapla()
    elif(islem=="4"):
        print("Evet işte karşında müzik listen!")
        veri.sarkilari_goster()

    else:
        print("Böyle bir seçeneğim bulunmuyor.Tekrar mı denesen?")



