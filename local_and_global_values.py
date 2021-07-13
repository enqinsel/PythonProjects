# Local etki alanından, Global etki alanını değiştirmek

x = []      # Global alan; genellikle fonksiyonların dışındaki alan global alan olur.

def eleman_ekle(y):
    x.append(y)                                 #Local alan.
    print("'"+str(y)+"'" + " ifadesi eklendi")


eleman_ekle(2)
eleman_ekle("ali")
x


# =============================================================================
# Çalışma mantığı: Python öncelikle local etki alanındaki değişkenleri tarar,arar ve bulmaya çalışır.
# Yukarıdaki örnekte eleman_ekle fonksiyonu tarandığında x değişkenini gördüğünde,
# önce local etki alanında satır satır tarayacaktır. Eğer bulamazsa; local etki alanındaki aramasını 
# bitirecek ve global etki alanına çıkacak. Globalde bu x'i bulacağından dolayı, append metodunu 
# bu listeye uygulayarak, fonksiyonu çalışır hale getirecek. Yani fonksiyonun içerisinde girmiş 
# olduğumuz değeri, bu listeye eklemiş olacak. Eğer; ikisinde de x değişkenini bulamazsa,
# NameError hatası verir. Böylece local etki alanından, global etki alanını 
# kolayca etkilemiş, müdahale etmiş olacağız.
# =============================================================================



