# Vücut Kitle endeksi
import sys

def whatBMI():
    print('''
   Kilonuzu boyunuzun metre cinsinden karesine böldüğünüz zaman ortaya çıkan rakamdır.
Vücut kitle indeksi (VKİ) İngilizce’de Body Mass Index (BMI) olarak ifade edilir.
          ''')

def whatVKI():
    print('''
   Dünya sağlık teşkilatına göre;
VKI'nin 18.5'den düşük olması "düşük kilolu",
18.5-24.9 arasında olması “normal”,
25-29.9 arasında olması “kilolu”, 
30-34.9 arasında olması  tip 1 obez ya da  “şişman”, 
35-39.9 arasında olması “tip II veya ileri obez”, 
40’ın üstünde olması ise  “morbid obezite” yani hastalık kabul edilecek düzeyde şişman olmak anlamını taşır.
          ''')

def calculate():
    global bmi
    size = int(input("Lütfen Boyunucuz 'cm' türünden giriniz.(Örn:174): "))/100
    kilo = int(input("Lütfen Kilonuzu 'kg' türünden giriniz.(Örn:75): "))
    bmi=round(kilo/((size)**2), 2)
    return bmi


while True:
    print('''
          1) BMI Nedir ?
          2) VKI Değer Aralıkları Ne Anlama Gelir ?
          3) Vücut Kitle Endeksi(VKI) Hesapla
          0) Çıkış
          ''')
    
    user = int(input("Yapmak istediğiniz işlemi seçiniz: "))
    
    if user == 1:
        whatBMI()
    elif user == 2:
        whatVKI()
    elif user == 3:
        calculate()
        if 18.5>bmi:
            print(f"\n>> Vücut Kitle Endeksiniz: {bmi}\n>> Sonuç:'Düşük Kilolu'")
        elif 18.5<bmi<24.9:
            print(f"\n>> Vücut Kitle Endeksiniz: {bmi}\n>> Sonuç:'Normal'")
        elif 25<bmi<29.9:
            print(f"\n>> Vücut Kitle Endeksiniz: {bmi}\n>> Sonuç:'Kilolu'")
        elif 30<bmi<34.9:
            print(f"\n>> Vücut Kitle Endeksiniz: {bmi}\n>> Sonuç:'Tip1-Obez ya da Şişman'")
        elif 35<bmi<39.9:
            print(f"\n>> Vücut Kitle Endeksiniz: {bmi}\n>> Sonuç:'Tip2 - İleri Obez'")
        elif 40<bmi:
            print(f"\n>> Vücut Kitle Endeksiniz: {bmi}\n>> Sonuç:'Morbid Obezite - Hastalık Derecesinde'")
    elif user == 0:
        print("Çıkış Yapıldı!")
        sys.exit()




    


