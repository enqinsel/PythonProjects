# print() fonksiyonu ve sep , end argümanları

print("HELLO AI ERA")

print("geleceği" , "yazanlar")

print("geleceği" , "yazanlar" , sep = "_") #argüman kullanarak biçimlendirme yaptık

#NOT: Fonksiyonların genel amaçlarını biçimlendirmek için kullanılan alt görev belirticilere argüman denir.

print("geleceği" , "yazanlar" , "kulübü" , sep = "_") #sep paratametresi, ifadeleri birleştirirken araya hangi karakterin gireceğini belirliyor.

print("geleceği" , sep = "_") # tek başına bir ifade etmiyor

print("birinci satır\nikinci satır\nüçüncü satır") #Bunu sep argümanı ile basitleştirebiliriz.

print("birinci satır" , "ikinci satır" , "üçüncü satır" , sep = ("\n")) # sep argümanının içine özel karakter yazdım.



print("Bugün günlerden Salı", end="\n") #end argümanının ön tanımlı değeri

print("Bugün günlerden Salı", end=".")

print("geleceği" , "yazanlar" , end=" kulübü") #end argümanı string ifadenin en sonuna belirlediğimiz şeyi ekleme yapar.




