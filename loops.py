# Loops - for

ogrenciler = ["ali", "veli", "isik", "berk"]

ogrenciler[0]
ogrenciler[1]
ogrenciler[2]
ogrenciler[3]

# Bu işi pratikleştirmek için; for döngüsünü kullanalım.

for i in ogrenciler:
    print(ogrenciler.index(i),"-" , i)
   
# Döngü ve fonksiyonları birlikte kullanalım.


maaslar = [1000,2000,3000,4000,5000]

def kare_al(x):
    print((x*20)/100 + x)

for maas in maaslar:
    kare_al(maas)

#break&continue
    # break: döngü bitirilmek istenir, continue: şartı sağlayan eleman görmezden gelinmek istenir.

maaslar = [8000,5000,2000,1000,3000,7000,1000]

# amacımız: tüm değerleri gezicek ancak 3000 değerine geldiğinde çalışmayı bırakacak.
#yani maaşı 3000 tlye kadar olanlarla ilgilendiğimizi düşünelim.

maaslar.sort()
maaslar

for i in maaslar:
    if i == 3000:
        print("kesildi")
        break
    print(i)


for i in maaslar:
    if i == 3000:       # 3000'i görmezden geldi, atladı, döndürmedi
        continue
    print(i)




# While
    #Belirtildiği şart sağlandığı sürece demektir.

sayi = 1

while sayi < 10:
    sayi += 1
    print(sayi)






































