print("----------------------------------------------------------------------\n*Oyundan çıkmak için, '+0'a basmanız yeterli olacaktır.\n*Oyun iki kişi ile oynanır.\n*İlk Kullanıcı: Aklından rastgele 10 tane sayı girer. \n*İkinci Kullanıcı: İlk kullanıcı'nın girdiği sayıları 3 deneme ile tahmin etmeye çalışır.\n----------------------------------------------------------------------")

import sys
tus = input("Merhaba, Oyunu başlatmak için '+1'e, çıkış yapmak için '+0'a bas.>>> ")

while True:
    if tus == "+1":
        print("\nOyun Başladı...")
        break
    if tus == "+0":
        print("Çıkış Yapıldı!!!")
        sys.exit()
    else:
        print("Lütfen, tekrar başlatın ve bir seçim yapın.")
        sys.exit()
        
sayilarin_listesi = set()
print("\n>>> İlk Oyuncu Oyuna Başladı...\n\nLütfen rastgele 10 sayı gir >>>")
for i in range(10):
    user1 = int(input(" {}. sayı: ".format(i+1)))
    if user1 == +0:
        print("Çıkış Yapıldı!!!")
        sys.exit()
    sayilarin_listesi.add(user1) 


tahmin = set()
print("\n>>> İkinci Oyuncu Oyuna Başladı...\n\nLütfen,tahmin ettiğiniz 3 sayıyı girin >>>")
for i in range(3):
    user2 = int(input(" {}. sayı: ".format(i+1)))
    if user2 == +0:
        print("Çıkış Yapıldı!!!")
        sys.exit()
    tahmin.add(user2)

sayilarin_listesi.intersection(tahmin)


if len(sayilarin_listesi.intersection(tahmin)) == 1:
        print("\nŞanslısın! 3'te 1!" , "\n\nİlk Oyuncunun Sayıları: " , sayilarin_listesi , "\nİkinci Oyuncunun Tahmin Ettikleri: " , tahmin)     
elif len(sayilarin_listesi.intersection(tahmin)) == 2:
        print("\nHarikasın!! 3'te 2!!" , "\n\nİlk Oyuncunun Sayıları: ", sayilarin_listesi , "\nİkinci Oyuncunun Tahmin Ettikleri: " , tahmin)
elif len(sayilarin_listesi.intersection(tahmin)) == 3:
        print("\nWaoow!!! Sen Bu İş İçin Yaratılmışsın, 3'te 3!!!" , "\n\nİlk Oyuncunun Sayıları: " , sayilarin_listesi , "\nİkinci Oyuncunun Tahmin Ettikleri: " , tahmin)
else:
    print("\nAhh!!! Üzgünüm, 3'te 0! Lütfen tekrar dene, BAŞARABİLİRSİN!!" , "\n\nİlk Oyuncunun Sayıları: " , sayilarin_listesi , "\nİkinci Oyuncunun Tahmin Ettikleri: " , tahmin)