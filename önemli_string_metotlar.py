#METOTLARA GENEL BAKIŞ

gel_yaz = "geleceği_yazanlar" # gel_yaz değişkenine atama yapıldı.

dir(gel_yaz) #Console bölümünde gel_yaz değişkeni ile çağırabileceğimiz tüm metotlar listelenir. Aynı zamanda gel_yaz. nokta koyup çıkan pencerede de görebilirsin.

#capitalize: İlk kelimenin baş harfini büyük yazar.
gel_yaz.capitalize()

#tittle: Tüm kelimelerin baş harfini büyük yazar.
gel_yaz.title()

#center: Metin ifadesine belirtilen sayı kadar boşluk ekleyip ifadeyi ortalamış olarak döndürür.
gel_yaz.center(50)

#count: Belirtilen metin ifadesi, ana metin ifadesinde kaç kere geçtiğini bulup döndürür.
a = "Bir berber bir berbere bre berber beri gel diye bar bar bağırmış"
a.count("berber")

#endswith: Metin ifadesi belirtilen metin ifadesi ile bitiyorsa TRUE değeri döndürür.Başlamıyorsa FALSE.
a.endswith("ş")
a.endswith("e")

#startswith: Metin ifadesi belirtilen metin ifadesi ile başlıyorsa TRUE değeri döndürür.Başlamıyorsa FALSE.
a.startswith("bir")
a.startswith("Bir")

#find: Metin ifadesi içerisinde belirtilen metin ifadesini arar ve bulduğu index değerini döndürür.
a.find("gel")
a.find("berber")

#index: Find metodu gibi çalışır. Metin ifadesi içerisinde belirtilen metin ifadesini arar ve bulduğu index değerini döndürür.
a.index("gel")
a.index("berber")

#format: Metin ifadesini biçimlendirir. Süslü parantezli yerleri doldururuz.Süslü parantezi istediğin kadar arttırabilirsin.
b="{} , {} ve {} iyi bir üçlüdür!"
b.format("engin", "ege" , "ahmet")

#isalnum: Metin ifadesindeki tüm karakterler alfanumerik yani sayı+harf ise TRUE değeri döndürür.Değilse FALSE.
c = "Company12"
c.isalnum()

#isalpha: Metin ifadesindeki tüm karakterler alfabetik ise TRUE değeri döndürür.Değilse FALSE.
d = "CompanyX"
d.isalpha()

#isdecimal: Metin ifadesindeki tüm karakterler sayı (kodlanmış olsa bile) ise TRUE değeri döndürür.	
e = "\u0033" #unicode
e.isdecimal()

#isdigit: Metin ifadesindeki tüm karakterler 0-9 arasındaki rakamlardan oluşan bir dize ise TRUE değeri döndürür.AYNI ZAMANDA ONDALIKLI SAYILARI VE NEGATİF SAYILARI KABUL ETMEZ.	
f = "50800"
f.isdigit() #TRUE
f = "50800 " #SONUNDA BOŞLUK VAR. 
f.isdigit() #FALSE
f = "-50800"
f.isdigit() #FALSE
f = "一二三四五" #Çinçe 12345
f.isdigit() #FALSE

#isnumeric: Dize herhangi bir sayısal karakter içeriyorsa (Ancak bu sayısal dediğimiz yine 0-9 arasındaki herhangi bir dildeki rakam olabilir.) TRUE değeri döndürür.
g = "123456"
g.isnumeric()

g = "一二三四五" #ÇİNCE 12345
g.isnumeric()   #TRUE

#Özetle isnumeric() fonksiyonu sadece 0-9 arasındaki rakamlar ve rakamlar yerine kullanılan başka bir dilden herhangi bir karakter içeriyorsa...

#isdigit kullanmak daha mantıklı olur çünkü ne istediğini daha açık ifade edebiliyorsun.

#isspace: Metin ifadesindeki tüm karakterler boşluk ise TRUE değeri döndürür.
h = "   "
h.isspace()

#istitle: Metin ifadesindeki her kelime büyük harf ile başlıyorsa TRUE değeri döndürür.	
j = "Hello, And Welcome To My World"
j.istitle()

#isupper: Metin ifadesindeki tüm karakterler büyük harf ise TRUE değeri döndürür.
k = "TÜRKİYE CUMHURİYETİ"
k.isupper()

#islower: Metin ifadesindeki tüm karakterler küçük harf ise TRUE değeri döndürür.	
k = "türkiye cumhuriyeti"
k.islower()

#join: Belirtilen bir karakteri kullanarak, bir dizgideki tüm öğeleri bir metin ifadesinde birleştir.
L = ("ID" , "Şifre" , "Yaş")
"-".join(L)

#swapcase: Metin ifadesindeki küçük harfleri büyük harfe veya tam dersi çekilde dönüştürür.	
j.swapcase()    

#strip: Metin ifadesini sağından ve solundan boşluk karakterlerini siler.	
m = "     muz  "
m.strip()

#replace: Metin ifadesinde, belirtilen metin ifadelerini değiştirir.	
j.replace("World", "Home") 






