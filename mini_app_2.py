#Mini uygulama- if-for-fonksiyonlar

#Soru: Maaşı 3 binden yüksek olanlara %10 zam, 3 bin ve daha az olanlara %20 zam yapılsın.

maaslar = [1000,2000,3000,4000,5000]

def on_zam(x):
    print(((x*10)/100) + x)

def yirmi_zam(y):
    print(((y*20)/100) + y)

for i in maaslar:
    if i > 3000:
        on_zam(i)
    elif i <= 3000:
        yirmi_zam(i)
        

#Sağlaması:

yirmi_zam(1000)
yirmi_zam(2000)
yirmi_zam(3000)
on_zam(4000)
on_zam(5000)