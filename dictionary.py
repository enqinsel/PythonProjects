# Veri yapıları - Dictionary (Sözlük)
    #Kapsayıcıdırlar, birden farklı tipleri barındırırlar.  
    #Sırasızdır, indeks işlemleri yapılamaz
    #Değiştirilebilir
    #Anahtar ifadelerin bir arada tutulduğu referanslı bir veri yapısıdır.
    #Sözlük oluşturmak için süslü parantez {} kullanılır.

sozluk = {"REG" : "Regresyon Modeli",
          "LOJ" : "Lojistik Regresyon",
          "CART" : "Classification and Reg"} 
sozluk

len(sozluk) # cevap 3 çıkacaktır. Tek satır tek eleman gibi düşünülür.


sozluk = {"REG" : 10,
          "LOJ" : 20,
          "CART" : 30}
sozluk

sozluk = {"REG" : ["RMSE" ,10],
          "LOJ" : ["MSE"  ,20],
          "CART" : ["SSE" ,30]}
sozluk


# Eleman İşlemleri

sozluk = {"REG" : ["RMSE" ,10],
          "LOJ" : ["MSE"  ,20],
          "CART" : ["SSE" ,30]}

# Sözlükler sırasız olduğu için, eleman seçimi indek ile yapılamaz.

sozluk[0] #hata verecektir. keyError

    # Eleman seçmek istiyorsak, sözlükteki keyleri kullanırız. Yani, REG,LOJ,CART gibi...
    
sozluk["REG"]
sozluk["LOJ"]


sozluk = {1 : ["RMSE" ,10],
          "LOJ" : ["MSE"  ,20],
          "CART" : ["SSE" ,30]}
sozluk
sozluk[1] #Keylere sayıda verebilirsin.


    #iç içe sözlükler de olabilir.

sozluk = {"REG" : {"RMSE" : 10,
                   "MSE"  : 20,
                   "SSE"  : 30},
          
          "LOJ" : {"RMSE" : 10,
                   "MSE"  : 20,
                   "SSE"  : 30},
          
          "CART" : {"RMSE" : 10,
                    "MSE"  : 20,
                    "SSE"  : 30}
          }

sozluk

sozluk["REG"]["SSE"] #Sözlüğün içindeki sözlüğe eriştik. Sonuç:30


# Eleman ekleme - Eleman değiştirme


sozluk = {"REG" : "Regresyon Modeli",
          "LOJ" : "Lojistik Regresyon",
          "CART" : "Classification and Reg"}
 
sozluk["GBM"] = "Gradient Boosting Machine" #en sona eklendi.
sozluk

    #Değiştirmede ise; key değerlerini yazıp atama işlemi gerçekleştircez.

sozluk["REG"] = "Çoklu Doğrusal Regresyon"
sozluk

    # Key değerleri sadece sabit veri yapılarıyla oluşturulabilir.Yani string veya integer tipler olabilir.  
    
l = [1,"a"] #liste oluşturuldu.

sozluk[l] = "yeni bir sey" # sözlüğe yeni bir key girilmek isteniyor. Ancak liste olduğu için hata verir.   


    # Listeyi kabul etmemesi; keylerin sabit olması gerektiğinden kaynaklanıyor. Referans değerlerdir.
    
    #Yukarıdaki açıklamaya istinaden; tuple veri yapısı key olabilir. Çünkü tuplelar sabittir.Değiştirilemezler.    

t = ("tuple",40) #tuple oluşturuldu

sozluk[t] = "yeni bir sey"
sozluk











