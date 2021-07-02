#SAYILAR VE STRİNGLERE GİRİŞ
9 #F9 ile çalışır
9+9 #Sonuç 18, F9 ile çalışır
9*9 #Sonuç 81, F9 ile çalışır 



type(123) #integer veri tipidir
"123"    #Python bunu string olarak algılar.Tırnak içerisinde yazdığımız için
type("123") #Bu da 7.satırın kanıtı

"a" + "b"   #İki tane string ifadeyi birleştirir, toplama işlemi değildir!
"a" "b"     #12.Satır ile benzer işlem
"a" " b"    #Aralarında boşluk bırakmak için
"a" + "-b"  # - ile birleştirme
"a" - "b"  # typeerror hatası alırsın, çıkarma işlemi string değil nümerik ifadelerde olur
"a"*3    # çarpma işareti ifadeyi çoğaltır, çarpma işlemi değildir.
"a "*3  #boşluk bırakara 3 kere yanyana yazdırdık.
"a"/3  #type hatası verir.

#NOT: Karakter dizinlerinde, + ve * işaretleri kullanılır. - ve / kullanılmaz.
