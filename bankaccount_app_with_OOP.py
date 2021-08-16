class BankAccount:
    
    #Yapıcı Fonksiyon
    def __init__(self):
        self.password = int(input("Şifrenizi Giriniz: "))
        self.balance = 0.0
    
    #Bakiye Görüntüleme
    def getBalance(self):
        return self.balance
    
    #Para yatırma
    def deposit(self):
        amount = float(input("Yatıracağınız miktarı girin: "))
        self.balance += amount
        return amount
    
    #Para çekme
    def withdraw(self):
        amount = float(input("Çekeceğiniz miktarı girin: "))
        self.balance -= amount
        return amount
    

options = """
    (0) Çıkış
    (1) Para Yatırma
    (2) Para Çekme
    (3) Bakiye Görüntüleme
    """
hesap = BankAccount()
    
while True:
    print(options)
    
    user = int(input("Yapmak istediğiniz işlemi seçiniz: "))
    
    if user == 1:
        print(f"Hesabınıza {hesap.deposit()}₺ eklendi.\nSon Bakiye: {hesap.getBalance()} ")
    
    elif user == 2:
        print(f"Hesabınızdan {hesap.withdraw()}₺ çekildi.\nSon Bakiye: {hesap.getBalance()} ")
    
    elif user == 3:
        print("Son bakiye: " , hesap.getBalance())
    
    elif user == 0:
        print("Hesabınızdan Çıkış Yapıldı.")
        break







