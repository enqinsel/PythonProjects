# Liste Metotları

liste = ["ali","veli","isik"]

dir(liste) # Bu liste ile kullanabileceğimiz metotların listesini çıkartır.

#append - eleman ekleme
liste.append("berkcan")
liste

#remove - eleman silme

liste.remove("berkcan")
liste

#clear - liste değişkenini silmez sadece içindekileri komple siler.

liste.clear()
liste

#copy - Herhangi bir değişkeni kopyalayıp, diğer değişkene atama yapabiliriz.

liste = ["ali","ahmet","mehmet"]

new_list = liste.copy()
new_list

#insert - indekse göre eleman ekler. Bulunduğu indeksteki eleman değiştirilmez.

liste = ["ali","veli","isik"]
liste

liste.insert(0, "ayşe") # Sıfırıncı indekse ayşe eklendi.
liste

liste.insert(1, "engin") # Birinci indekse engin eklendi. Diğer elemanlar silinmedi,değişmedi.
liste

    #Bazen son elemanın kaçıncı indekste olduğunu bilemezsin, bunun için len() yöntemi kullanılır.

liste = ["ali","veli","isik"]
liste

len(liste) # Son indeksimiz 3

liste.insert(len(liste),"beren") #En sona beren eklendi.
liste

#pop metodu - İndekse göre eleman siler.

liste = ["ayşe","ali","mehmet","isik","berk","beren","engin","ege","selin"]
liste

liste.pop(0) #Sıfırıncı indeksteki elemanı sildik. ayşe silindi
liste

liste.pop() # eğer indeks yazılmazsa, en sondaki elemanı siler. selin silindi.
liste

liste.pop(-1) # -1 indeksi , sıfırdan sola doğru gider. Mantık olarak en sondaki elemandır.
liste

liste.pop(-2) # En sağdan ikinci indeksli gibi düşün. beren silindi.
liste

#count metodu - Hani elemandan liste içinde kaç tane olduğunu söyler. Sayma metodudur.

liste = ["ali","veli","isik","ali","veli"]

liste.count("ali")  # ali iki tane var.
liste.count("isik") # isik bir tane var

#extend metodu - listeleri birleştirir

new_list = ["ali","kemal","ayşe"]
liste

liste.extend(new_list)
liste

    # içinde yeni bir listede oluşturabiliriz.

liste = ["ali","veli","isik","ali","veli"]

liste.extend([1,"a"])
liste

#index metodu - Bir elemanın hangi indekste olduğunu söyler.

liste = ["ali","veli","isik","ali","veli"]

liste.index("isik")
liste.index("veli") #ilk gördüğünü yazar.

#reverse metodu - Listenin elemanlarını terse çevirir.

liste = ["a","b","c","d","e"]

liste.reverse() #listeyi terse çevirdi. e,d,c,b,a oldu.
liste


#sort metodu - Sıralama yapmak için kullanılır.

liste = ["c","d","a","b","e"]

liste.sort() # Alfabetik sıraya göre sıraladı.
liste

liste = [10,4,50,1,90,-2,0]

liste.sort() #küçükten büyüğe doğru sıralar.
liste
        #Not: sort metodu çalışması için, liste içindekiler aynı veri tipinden olmak zorundalar.
        
        


