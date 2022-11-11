
#1 Zadaca: Da se napravi programa vo koja korisnikot ke vnese 2 broevi i da se proveri dali zbirot e pomal od 100
"""broj1 = int(input("Vnesete go prviot broj "))
broj2 = int(input("Vnesete go vtoriot broj "))
zbir = broj1 + broj2 
print ("Zbirot na dvata broja e {}".format(zbir))

if zbir < 100:
    print ("Zbirot na dvata broja {} e pomal od 100". format(zbir))
else:
    print ("Zbirot na dvata broja {} e pogolem od 100".format(zbir))"""


#2 Zadaca: Da se napravi programa vo koja korisnikot ke vnese godina na ragjanje, ke se presmeta kolku godini e i da se odredi dali e maloleten ili polnoleten
"""x=0
Ime = input("Vnesete go vaseto ime: ")
Prezime = input("Vnesete go vaseto prezime: ")
godina_raganje = int(input("Vnesete godina na ragjanje: "))
y = 2022 - godina_raganje
print("{} {} {} godini.".format(Ime, Prezime, y))
if y >= 18:
    print("{} {} e polnoleten.".format(Ime, Prezime))
else:
    print("{} {} e maloleten i ne gi ispolnuva uslovite.".format(Ime,Prezime))"""

#3 Zadaca: Da se napravi programa vo koja korisnikot ke vnese strani na dva pravoagolnici, da se presmeta plostinata i da se proveri koj pravoagolnik e pogolem
"""while True:
    x = int(input("Vnesete strana a na pravoagolnik: "))
    x1 = int(input("Vnesete strana b na pravoagolnik: "))
    plostina = x*x1
    print(plostina)
    y= int(input("Vnesete strana a na pravoagolnik: "))
    y1 = int(input("Vnesete strana b na pravoagolnik: "))
    plostina1 = y*y1
    print(plostina1)
    
    if plostina > plostina1:
        print ("Prviot pravoagolnik e pogolem od vtoriot")
    elif plostina < plostina1:
        print ("Vtoriot pravoagolnik e pogolem od prviot")
    d = input("Dali sakate da vnesete uste podatoci: ")
    if d.upper()=="DA":
        pass
    else:
        break
print("Uspesno vnesovte podatoci za dve pravoagolnici")"""

#4 Zadaca: Da se napravi programa vo koja korisnikot ke vnese goleminite na aglite na triagolnici, i da se proveri dali so tie golemini moze da se kreira triagolnik(zbirot treba da bide 180)
"""while True:
    x = int(input("Vnesete go prviot agol od triagolnikot: "))
    y = int(input("Vnesete go vtoriot agol od triagolnikot: "))
    z = int(input("Vnesete go tretiot agol od triagolnikot: "))
    zbir = x + y + z
    print ("Zbirot na trite agli od triagolnikot e {}".format(zbir))
    if zbir == 180:
        print ("Zbirot na trite agoli od triagolnikot iznesuva 180")
    elif zbir > 180:
        print("Zbirot na trite agli e pogolemo od 180")
    elif zbir < 180:
        print("Zbirot na trite agli e pomal od 180")
    d = input("Dali sakate da vnesete uste podatoci: ")
    if d.upper()=="DA":
        pass
    else:
        break
print ("Uspesno vnesovte podatoci za triagolnici")"""

#5 Zadaca: Da se napravi programa vo koja korisnikot ke vnese nekoe ime i da se proveri sekoga samoglaska kolku pati se pojavuva vo ime i od kolku karakteri e sostaveno toa ime
"""Ime = input("Vnesete go vaseto ime: ")
br_bukvi = len(Ime)
print("Brojot na bukvi vo vaseto ime e: {}".format(br_bukvi))
br_povtoruvanje = Ime.count("a")
br_povtoruvanje1 = Ime.count("i")
br_povtoruvanje3 = Ime.count("u")
br_povtoruvanje2 = Ime.count("e")
br_povtoruvanje4 = Ime.count("o")
zbir = br_povtoruvanje + br_povtoruvanje1 + br_povtoruvanje3 + br_povtoruvanje2 + br_povtoruvanje4
print("Vo vaseto ime imate {} samoglaski".format(zbir))"""
