import math
import sys

def carp(x,y):
    return x*y

def bol(x,y):
    return x/y

def topla(x,y):
    return x+y

def cikar(x,y):
    return x-y

def yuzde(x,y):
    return (x*y)/100

def fakt(x):
    return math.factorial(x)

def log(x,y):
    return math.log(x,y)

def us_alma(x,y):
    return math.pow(x, y)

def kok_alma(x):
    return math.sqrt(x)

def sin(x):
    return math.sin(x)

def cos(x):
    return math.cos(x)

def tan(x):
    return math.tan(x)

def ebob(x,y):
    return math.gcd(x, y)

def mod(x,y):
    return math.fmod(x, y)

def cot(x):
    return cos(x)/sin(x)


options = """
(q) Çıkış
(1) Toplama hesaplama
(2) Çıkarma hesaplama
(3) Çarpma hesaplama
(4) Bölme hesaplama
(5) Yüzde hesaplama
(6) Karekök hesaplama
(7) Faktöriyel hesaplama
(8) Logaritma hesaplama
(9) Üs hesaplama
(10) Sinüs hesaplama
(11) Kosinüs hesaplama
(12) Tanjant hesaplama
(13) Kotanjant hesaplama
(14) Mod hesaplama
(15) EBOB hesaplama
"""


while True:
    print(options)

    soru = input("Yapmak istediğiniz işlemi seçiniz: ")

    if soru == "1":
                sayi1 = int(input("Toplama işlemi için ilk sayıyı girin: "))
                sayi2 = int(input("Toplama işlemi için ikinci sayıyı girin: "))
                print(sayi1 , "+", sayi2, "=", topla(sayi1, sayi2))
            
    elif soru == "q":
                print("Çıkış Yapıldı...")
                sys.exit()
        
    elif soru == "2":
                sayi3 = int(input("Çıkarma işlemi için ilk sayıyı girin: "))
                sayi4 = int(input("Çıkarma işlemi için ikinci sayıyı girin: "))
                print(sayi3 , "-", sayi4, "=", cikar(sayi3, sayi4))
        
    elif soru == "3":
                sayi5 = int(input("Çarpma işlemi için ilk sayıyı girin: "))
                sayi6 = int(input("Çarpma işlemi için ikinci sayıyı girin: "))
                print(sayi5 , "*", sayi6, "=", carp(sayi5, sayi6))
        
    elif soru == "4":
        try:
                sayi7 = int(input("Bölme işlemi için ilk sayıyı girin: "))
                sayi8 = int(input("Bölme işlemi için ikinci sayıyı girin: "))
                print(sayi7 , "/", sayi8, "=", bol(sayi7, sayi8))
        except ZeroDivisionError:
            print("Paydaya Sıfır Girilmez, Sıfır(0) dışında bir rakam giriniz!")
            
    elif soru == "5":
                sayi9 = int(input("Yüzde işlemi için ilk sayıyı girin: "))
                sayi10 = int(input("Yüzde işlemi için ikinci sayıyı girin: "))
                print(sayi9 , "%", sayi10, "=", yuzde(sayi9, sayi10))
        
    elif soru == "6":
                sayi11 = int(input("Karekök işlemi için sayı girin: "))
                print("√","(",sayi11,")"  ,"=", kok_alma(sayi11))
        
    elif soru == "7":
                sayi12 = int(input("Faktöriyel işlemi için sayı girin: "))
                print(sayi12,"!" ,"=", fakt(sayi12))   
        
    elif soru == "8":
                sayi13 = int(input("Logaritma işlemi için ilk sayıyı girin: "))
                sayi14 = int(input("Logaritma işlemi için ikinci sayıyı girin: "))
                print(sayi13 , "log","(",sayi14,")", "=", log(sayi13, sayi14))
        
    elif soru == "9":
                sayi15 = int(input("Üs işlemi için ilk sayıyı girin: "))
                sayi16 = int(input("Üs işlemi için ikinci sayıyı girin: "))
                print(sayi15 , "^", sayi16, "=", us_alma(sayi15, sayi16))
        
    elif soru == "10":
                sayi17 = int(input("Sinüs işlemi için sayı girin: "))
                print("sin","(",sayi17,")"  ,"=", sin(sayi17))
        
    elif soru == "11":
                sayi18 = int(input("Kosinüs işlemi için sayı girin: "))
                print("cos","(",sayi18,")"  ,"=", cos(sayi18))
        
    elif soru == "12":
                sayi19 = int(input("Tanjant işlemi için sayı girin: "))
                print("tan","(",sayi19,")"  ,"=", tan(sayi19))
        
    elif soru == "13":
                sayi20 = int(input("Kotanjant işlemi için sayı girin: "))
                print("cot","(",sayi20,")"  ,"=", cot(sayi20))
        
    elif soru == "14":
                sayi21 = int(input("Mod işlemi için ilk sayıyı girin: "))
                sayi22 = int(input("Mod işlemi için ikinci sayıyı girin: "))
                print(sayi21 , "mod", sayi22, "=", mod(sayi21, sayi22))    
        
    elif soru == "15":
                sayi23 = int(input("EBOB işlemi için ilk sayıyı girin: "))
                sayi24 = int(input("EBOB işlemi için ikinci sayıyı girin: "))
                print("EBOB","(",sayi23,",",sayi24,")", "=", ebob(sayi23, sayi24))







