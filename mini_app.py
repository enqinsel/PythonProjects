sinir = 50000

magaza_adi = str(input("Mağazanızın Adı Nedir ?"))
gelir = int(input("Geliriniz nedir ?"))

if gelir < sinir:
    print("Üzgünüm! Geliriniz sınır değerinin altında!")
elif gelir == sinir:
    print("Geliriniz sınır değeri ile eşit!")
else:
    print("Tebrikler! Geliriniz sınır değerini aşmıştır.")