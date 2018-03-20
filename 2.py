#a=müsterilerlecalısmasuresi
#b=calisilansure
#c=toplammusterisayisi

def müsterilerlecalısmasuresi2016yiliHesapla(b,c):
    global a
    a=b/c
    return a
def müsterilerlecalısmasuresi2017yiliHesapla(b,c):
    global z
    z=(b+50)/(c+20)
    return z
b=170
c=50
x=müsterilerlecalısmasuresi2016yiliHesapla(b,c)
y=müsterilerlecalısmasuresi2017yiliHesapla(b,c)
print (x-y)
