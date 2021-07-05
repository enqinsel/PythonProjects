# Type Dönüşümleri - Input

toplama_bir = input()
toplama_iki = input()

type(toplama_bir) # str değişken

toplama_bir + toplama_iki #str değişken olduğu için yan yana yazdı.

int(toplama_bir) + int(toplama_iki) # 3+4 = 7 , integer tipe dönüştürüldü.

int(11.323) #float sayısını integera dönüştürdük.

float(12) # Burada da integer tipi float tipine dönüştürdük.

str(12) # Konsolda da göründüğü gibi '12' tırnak içinde string bir ifadeye dönüştü.

type(str(12)) #16.satırı kanıtladık. String tipinde olduğunu gördük.

