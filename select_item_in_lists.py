# Listeler - Eleman Seçimi

liste = [10,20,30,40,50]

liste[0] #10
liste[1] #20
liste[2] #30
liste[3] #40
liste[4] #50


liste[0:2] # sol taraf dahil, sağ taraf dahil değil. Sonuç: [10,20]

liste[:2] # 12. satırdaki ile aynı. Anlamı şu: ilk indeksten, 2. indekse kadar, 2.indeks hariç.
liste[2:] # Bu da tam tersi, 2'den son indekse kadar. Son indeks hariç!

yeni_liste = ["a",10,[20,30,40,50,"b"]]
yeni_liste

yeni_liste[2]
yeni_liste[0:2]

yeni_liste[2][1] #Bu şu demek: Listenin içinde var olan yeni listenin elemanlarına erişmektir. 1.indeksli 30 elemanına ulaştık.
yeni_liste[2][4] # "b" elemanına ulaştık.
 
type(yeni_liste[2])
type(yeni_liste[2][4]) # "b" harfinin tipi str dir.



