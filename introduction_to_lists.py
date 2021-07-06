# Veri Yapıları - lists
    # Değiştirilebilirdir
    # Kapsayıcıdır(Farklı tipte verileri tutabilir)
    # Sıralıdır
    # [] ve list() şeklinde iki farklı biçimde liste oluşturulabilir
    # list bir veri yapısıdır, bunun içinde string ve sayısal değerlerde olabilir.Satır 11
    # Bir liste içerisine başka bir liste'de ekleyebiliriz. Satır 11      

notlar = [90,80,70,50]
type(notlar)


liste = ["a",12.5,90,[1,2,3],notlar] # Farklı veri tipleri bulundurur ve içinde bir liste de oluşturabiliriz.

len(liste) # 5 elemanlıdır, listenin içerisindeki listeyi tek elemanlı olarak sayarız.

# Liste içerisindeki elemanların tipini bulmak için;

type(liste[0]) # 0. indeksli 1. eleman "a" nın tipi str.
type(liste[1]) # 1. indeksli 2. eleman 12.5 in tipi float.
type(liste[2]) # 2. indeksli 3. eleman 90 nın tipi int.
type(liste[3]) # 3. indeksli 4. eleman [1,2,3] tipi list.
type(liste[4]) # 4. indeksli 5. eleman notlar yani [90,80,70,50] tipi list.


# notlar ve liste listelerini birleştirelim.

tum_liste = [notlar, liste]

# Herhangi bir listeyi silmek için del komutunu kullanırız.

#del tum_liste (işimiz bittikten sonra komut satırı içine almak daha doğru olur.)


