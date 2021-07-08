# Veri Yapıları - Tuple
    # Kapsayıcıdırlar, birbirinden farklı veri tiplerini barındırabilirler.
    # Sıralıdır, içerisinde indeks işlemleri yapılabilir.
    # Değiştirilemezler

#Tuple oluşturma-Kapsayıcıdırlar

t = ("ali","veli",1,2,3.2,[1,2,3,4]) # tuple normal parantez ile kapanır.

t2 = "ali","veli",1,2,3.2,[1,2,3,4]  # tuple parantez olmadanda olur.

#del t2
# Son olarak da tuple() şeklinde de oluşur.

t = ("eleman",) # tek elemanlı bir tuple oluşturulcaksa, sona bir virgül koyulmalı
type(t)

#Tuple Eleman işlemleri - Sıralıdırlar

t = ("ali","veli",1,2,3.2,[1,2,3,4])

t[1] #veli

t[0:3] # ali,veli,1

# Değiştirilemezler, içindeki elemanı değiştiremezsin. Metodlar ile bir değişiklik yapamazsın.

t[2] = 99 # Hata verir.
