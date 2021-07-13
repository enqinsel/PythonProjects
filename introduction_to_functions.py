#FONKSIYONLARA GIRIŞ VE FONKSIYON OKURYAZARLIĞI

?print #Bu komut print fonksiyonun dokümantasyonunu çıkartır. Bir nevi kullanımı hakkında detaylı bilgi verir.

print(" a","b" , end = "*")


# MATEMATİKSEL İŞLEMLER

4*4
4/4
5-1
6+2
3**2
3**3

# FONKSİYON NASIL YAZILIR ?
    # def komutu ile fonksiyon tanımlayabiliriz.
    
    
def kare_al(x):
    print("Sonuç: " , x**2)
    
kare_al(3)    


def kare_al(x):
    print("Sonuç: " + str(x**2)) # Bu şekilde de yapılabilir.
    
kare_al(3) 



def kare_al(x):
    print("Girilen Sayı:" + str(x) + " , Karesi: " + str(x**2)) 
    
kare_al(3)


# İki argümanlı fonksiyon tanımlama

def carpma_yap(x,y):
    print("Çarpmak istediğin sayılar: " + str(x) + " ve " + str(y))
    print("Çarpım Sonucu: " + str(x*y))

carpma_yap(4,5)

# Ön tanımlı argumanlar

def carpma_yap(x,y=1):  #Eğer kullanıcı ikinci argümanı girmediyse; o argumana ön tanımı atarız. Buradaki y gibi
    print(x*y)

carpma_yap(4)
carpma_yap(4,5) # Yukarıda y=1 yazmamız sadece y argumanı kullanıcı tarafından girilmediğinde geçerlidir. Burada 4*5 işlemi olur.

# Argumanların Sıralaması


def carpma_yap(x,y=1):
    print(x*y)

carpma_yap(y = 4 , x = 5) #Bu aslında 5*4 tür diyebiliriz.


def cikarma_yap(x,y=0):
    print(y-x)              #İlk yazdığı sayı y olsun ve x'den çıkarılsın.

cikarma_yap(y = 4 , x = 1)

?cikarma_yap # Böylelikle kendi oluşturduğumuz fonksiyonunun dokümantasyonunu okumuş oluruz.

# Ne zaman fonksiyon yazılır ?
    #Örnek üzerinden;

# Bir sokak lambasına ilişkin; isi, nem, sarj gibi değişkenlerimiz olsun.Bunlara göre sokak lambamızın değerini ölçelim.

(40+25)/90 #isi:40 , nem:25 , sarj:90 Sokak lambasının değerini ölçmek için böyle bir işlem yaptık.

# Peki diyelim ki; elimizde bir değilde yüzlerce binlerce sokak lambası olsaydı; her defasında böyle değişkenleri alıp, işlememi sokacaktık ? -Tabii ki hayır.

    #Bu işlemi bir fonksiyon yani metot'a çevirelim. Bir fonksiyona giydirelim.
    
def direkt_hesap(isi,nem,sarj):
    print((isi+nem)/sarj)

direkt_hesap(40, 25, 90)


    # Özetle; Fonksiyonları, sık tekrar eden işlemlerden ya da uzun işlemlerden kurtulmak için yazarız.

#Çıktıyı girdi olarak kullanmak(return)


def direkt_hesap(isi,nem,sarj):
    return (isi+nem)/sarj

cikti = direkt_hesap(25, 40, 70)
cikti
print("Çıktı: " , cikti)
direkt_hesap(25, 40, 70)*9


















