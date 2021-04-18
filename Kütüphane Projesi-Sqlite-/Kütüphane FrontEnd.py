from Modül import *

print("""
##################################################
#        NAMIK KEMAL İL HALK KÜTÜPHANESİ         # 
#                                                #
# 1)Kitap Ekle                                   #
# 2)Kitap Sorgula                                #
# 3)Kitap Sil                                    #
# 4)Kitapları Göster                             #
# 5)Kitap Baskı Güncelle                         #
#                                                #
# Product By:Melih Selami ÜRKMEZ                 #
##################################################
""")

kutuphane=Kutuphane()

while(1):
    secim=input("Lütfen yapmak istediğiniz işlem numarasını giriniz(Çıkış yapmak için 'q' basınız):")

    if(secim=='q'):
        kutuphane.baglanti_kopar()
        exit()
    elif(secim=="1"):
        isim=input("Eklemek istediğiniz kitabın ismini giriniz:")
        yazar=input("Eklemek istediğiniz kitabın yazarını giriniz:")
        yayinevi=input("Eklemek isediğiniz kitabın yayınevini giriniz:")
        tur=input("Eklemek istediğiniz kitabın türünü giriniz:")
        baski=int(input("Eklemek istediğiniz baskı sayısını giriniz:"))
        yeni_kitap=Kitap(isim,yazar,yayinevi,tur,baski)
        print("Kitap ekleme işlemi gerçekleştiriliyor.")
        time.sleep(2)
        kutuphane.kitap_ekle(yeni_kitap)
        print("Kitap başarılı bir şekilde eklendi.")
    elif(secim=="2"):
        isim=input("Aramak istediğiniz kitabın ismini giriniz:")
        kutuphane.kitap_sorgula(isim)
    elif(secim=="3"):
        isim=input("Silmek istediğiniz kitabın ismini giriniz:")
        kutuphane.kitap_sil(isim)
        print("Kitap silme işlemi gerçekleştirildi.")
    elif(secim=="4"):
        print("NAMIK KEMAL İL HALK KÜTÜPHANESİ KİTAP LİSTESİ:")
        kutuphane.kitaplari_goster()
    elif(secim=="5"):
        kullanici=input("Baskı sayısını güncellemek istediğiniz kitabın ismini giriniz:")
        print("Baskı sayısı 1 arttırılıyor.Lütfen Bekleyiniz..")
        time.sleep(2)
        kutuphane.baski_arttir(kullanici)
    else:
        print("Böyle bir seçenek otomasyonda bulunmamaktadır.")




