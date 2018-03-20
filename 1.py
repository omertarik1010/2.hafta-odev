#a=katmadegerciro
#b=toplamsatismiktari
#c=hammaddemaliyeti
#d=bakimonarimgiderleri
#e=sevkiyatgiderleri
#f=satinalinanhizmetgiderleri

def katmadegerciroHesapla(b,c,d,e,f):
    global a
    a=b-(c+d+e+f)
    if(a>1000):
        print("İşletme katma değer cirosu yüksektir.")
    elif(500<a<999):
        print("İşletme katma değer cirosu normaldir.")
    else:
        print("İşletme katma değer cirosu düşüktür.")
        return a
print("Lütfen değerleri giriniz.")
b=int(input("toplam satış miktarı giriniz:"))
c=int(input("hammadde maliyeti giriniz:"))
d=int(input("bakım onarım giderlerini giriniz:"))
e=int(input("Sevkiyat giderlerini giriniz:"))
f=int(input("satın alınan hizmetleri giriniz:"))
a=katmadegerciroHesapla(b,c,d,e,f)
print(a)
