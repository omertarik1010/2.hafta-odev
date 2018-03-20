#b=yazilimgelirleri
#c=finansmangelirleri
#d=ürünsatisgelirleri
#e=calisanmaaslari
#f=donanimmaliyeti
#h=sponsorlukgeliri
#i=eticaretgeliri
#k=bakimmaliyeti
#l=kiragideri

def ilkaykarHesapla(b,c,d,e,f,l):
    global kar
    kar=(b+c+d)-(e+f+l)
    return kar
def sonkarHesapla(b,h,i,d,e,l,k):
    global z
    z=(b+h+i+d)-(e+l+k)
    return z
print("lütfen değerleri giriniz:")
b=int(input("yazılım gelirlerini giriniz:"))
c=int(input("finansman gelirlerini giriniz:"))
d=int(input("ürün satış gelirlerini giriniz:"))
e=int(input("çalışan maaşlarını giriniz:"))
f=int(input("donanım maliyetlerini giriniz:"))
h=int(input("sponsorluk gelirlerini giriniz:"))
i=int(input("eticaret gelirlerini yazınız:"))
k=int(input("bakım maliyetlerini yazınız:"))
l=int(input("kira gideri yazınız:"))
x=ilkaykarHesapla(b,c,d,e,f,l)
y=sonkarHesapla(b,h,i,d,e,l,k)
print(x-y)
if(x-y>5000):
    print("işletme çok karlı.")
elif(1000<x-y<5000):
    print("işletme karı normal.")
else:
    print("işletme yeterince karda değil.")
