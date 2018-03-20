k=koltukSayisi=50
y=yatakSayisi=20
d=dolapSayisi=40
def donemBasiStok(koltukSayisi,yatakSayisi,dolapSayisi):
    global donemBasiStok
    donemBasiStok=(koltukSayisi+yatakSayisi+dolapSayisi)
    return donemBasiStok
def donemIciStok(koltukSayisi,yatakSayisi,dolapSayisi):
    global donemIciStok
    donemIciStok=((koltukSayisi+10)+(yatakSayisi+15)+(dolapSayisi+5))
    return donemIciStok
def donemSonuStok(koltukSayisi,yatakSayisi,dolapSayisi):
    global donemSonuStok
    donemSonuStok=((koltukSayisi+10-25)+(yatakSayisi+15-20)+(dolapSayisi+5-10))
    return donemSonuStok
def ortalamaStok(donemBasiStok,donemSonuStok):
    ortalamaStok=(donemBasiStok+donemSonuStok)/2
    return ortalamaStok
x=donemBasiStok(koltukSayisi,yatakSayisi,dolapSayisi)
y=donemSonuStok(koltukSayisi,yatakSayisi,dolapSayisi)
z=ortalamaStok(donemBasiStok,donemSonuStok)
z=(x+y)/2
print (z)
