# Listeler - Eleman değiştirme - Eleman ekleme - Eleman silme

liste = ["ali","veli","berkcan","ayse"]
liste

#veli yerine velinin_babasi ismini yazmak istiyorsak:
    
liste[1] = "velinin_babasi" #liste[1] yani veli 'ye velinin_babasi değişkenini atadık.
liste

liste[1] = "veli"

liste[0:3] = "alinin_babasi" , "velinin_babasi" , "berkcanin_babasi" # bu yöntemle de birden fazla elemanı değiştirmiş olduk.
liste

# Liste'ye eleman ekleme 

#Listenin sonuna kemal eklemek için: 
    
liste = ["ali","veli","berkcan","ayse"]

liste = liste + ["kemal"]
liste

# Kemali başa eklemek için;

liste = ["ali","veli","berkcan","ayse"]

liste = ["kemal"] + liste
liste 

# Listeden eleman silmek için:

liste = ["ali","veli","berkcan","ayse"]    
liste

# berkcanı silmek için:

#del liste[2] #listenin 2.indeksteki değerini sildik.
liste    
