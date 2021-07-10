#Veri Yapıları - Setler(Kümeler)
    # Sınırsızdırlar yani, indeksizdir.
    # Değerler eşsizdir, yani tekrar eden değerlerden oluşamaz.
    # Değiştirilebilirdir. 
    # Farklı veri tipleri barındırabilirler.
    # Performans odaklı bir veri tipidir
    # Matematiksel anlamda kümelere benzer.
    
#Set oluşturmak    
s = set()
s

l = [1, "a", "ali", 123]
s = set(l)
s


t = ("a", "ali")
s = set(t)
s

ali = "lutfen_ata_bakma_uzaya_git"
type(ali)

s = set(ali) # Bütün elemanları parçalayarak, birden fazla olanları çıkartarak döndürdü,tekilleştirdi.
s

l = ["ali", "lütfen", "ata", "bakma", "uzaya", "git", "git", "ali", "git"]
s = set(l) # Yukarıdaki örnek gibi, tekrar edenleri almadı
s

len(s) # 6 eleman sayar, tekrar edenleri saymaz. Bu yüzden performansı olumlu yönde etkiler.

s[0] #Sırasız oldukları için, indeksle elemanlarını seçemeyiz.


# Eleman ekleme ve çıkarma 

l = ["gelecegi", "yazanlar"]

s = set(l)
s

s.add("ile")
s

s.add("gelecege_git")
s

s.add("ile") # Önceden ile ifadesi eklendiği için ikinciye izin vermiyor. Bir tane kabul eder.
s

s.remove("gelecegi")
s

s.discard("gelecegi") # Buda silme işlemi gerçekleştirir. Ancak remove dan tek farkı; sileceğin eleman setin içinde olmasa bile silmiş gibi gösterir, hata vermez. Remove da olmayan bir elemanı silersen hata verir. Kod akışı için önemli.
s

#Klasik küme işlemleri

# =============================================================================
# difference() ile iki kümenin farkını ya da "-" ifadesi,
# intersection() iki küme kesişimi ya da "&" ifadesi,
# union() iki kümenin birleşimi,                      CTRL+4 ile çoklu yorum satırı yapıldı.
# symmetric_difference() ikisinde de olmayanları.
# =============================================================================


# difference()
    #Kümelerdeki A-B mantığı; A'da olub b'de olmayan
set1 = set([1,3,5])
set2 = set([1,2,3])

set1.difference(set2) # set1-set2; set1 de olup, set2 de olmayan 5'dir.
set2.difference(set1) # set2-set1; 2

    # Daha pratik yolu; "-" ifadesi ile de farkını bulabiliriz.

set1 - set2 # set1-set2; set1 de olup, set2 de olmayan 5'dir.
set2 - set1 # set2-set1; 2

   # Bu tabii ki toplama,çarpma ve bölme de yapabileceğimiz anlamına gelmez.

    # symmetric_difference()
        #İkisinde de, yani birbirlerinde olmayanlar

set1.symmetric_difference(set2) #Sonuç: 2, 5 ; 2 set1'de yok, 5 set2'de yok.


# intersection() & union() Küme kesişimi - Küme birleşimi

    # intersection; iki kümenin kesişimini verir, yani ortak elemanlarını.
    
set1 = set([1,3,5])
set2 = set([1,2,3])

set1.intersection(set2) # 1,3 iki kümenin kesişimidir.
set2.intersection(set1) # Mantıken aynı sonuç çıkacaktır. 1,3

    # Daha pratik yolu; "&" operatörü ile de kesişimini bulabiliriz.

set1 & set2 # Sonuç yine 1,3 olacaktır.

# intersection_update; Kesişimin sonucunu, belirttiğimiz set ile değiştirir.
set1.intersection_update(set2) #Normalde kesişim 1,3; set1 ise 1,3,5; Bu komut ile set1 1,3 olur.
set1

    #union; iki kümenin birleşimini verir. Yani tüm elemanları döndürür.
    
set1.union(set2)  # Sonuç: 1,2,3,5  
set2.union(set1)  # Yine aynı sonuç olarak; 1,2,3,5
    
    # Not: her bir elemanı bir kere alıp, öyle birleştirir. Set olduğu için...
          
# Set Sorgu İşlemleri

set1 = set([7,8,9])
set2 = set([5,6,7,8,9,10])    

    # İki kümenin kesişiminin boş olup olmadığının sorgulanması:

set1.isdisjoint(set2) # İki kümenin kesişimi boş mu ? diyor. True dönerse;evet boş. False dönerse; boş değil.

    # Bir kümenin bütün elemanlarının başka bir küme içerisinde yer alıp almadığı:

set1.issubset(set2) # Diyor ki; set1, set2'nin alt kümesi mi ? True dönerse;evet. False dönerse hayır.

    # Bir kümenin, diğer kümeyi kapsayıp kapsamadığı,altkümenin tersi:

set2.issuperset(set1) # set2, set1'i kapsıyor mu ? diye sordu.True dönerse;evet. False dönerse hayır.
set1.issuperset(set2) #Sonuç false olur. set1, set2'yi kapsamıyor.






