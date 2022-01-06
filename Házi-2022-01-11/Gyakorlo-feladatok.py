# #1. feladat > Helló világ: Készíts programot, mely kiírja a képernyőre azt a szöveget, hogy „Hello World”!
# print("Hello World!")

# #2. feladat >  Készíts programot, amely bekéri a felhasználó nevét, majd üdvözli őt a nevén szólítva!
# name = input("Add meg a neved> ")
# print("Üdvözöllek,", name)

# #3. feladat > Készíts programot, mely bekéri a felhasználótól, hogy a kasszában hány 100, 200 és 500 Ft-os található. A program számolja ki, hogy mennyi a beírt pénz összege!
# szazasok = int(input("Add meg a Százasok számoát> "))
# ketszazasok = int(input("Add meg a Kétszázasok számoát> "))
# otszazasok = int(input("Add meg a Ötszázasok számoát> "))

# ertek100 = szazasok * 100
# ertek200 = ketszazasok * 200
# ertek500 = otszazasok * 500

# result = ertek100 + ertek200 + ertek500
# print(result)

# # #4 feladat > Készíts programot, amely bekér a felhasználótól egy valós számot (Celsius fok), az eredményt átváltja Fahrenheit értékbe, és kiírja az eredményt a képernyőre (0°C=32°F, 40°C=104°F, lineáris)! Írd meg ugyanezt fordítva is!
# celsius = int(input("Add meg a celsius fokot> "))
# if celsius == 0:
#     print(32)
# else:
#     print((celsius * 1.8) + 32)


# #5 feladat >  Készíts programot, mely két időpontot kérdez a felhasználótól (óra, perc, másodperc külön), majd kiszámítja a két időpont közötti időtartamot másodpercben, és az eredményt kiírja a képernyőre.
# #-----------Eggyik óra-----------------------
# ora1 = int(input("Az első idő órája> "))
# perc1 = int(input("Az első idő perce?> "))
# masodperc1 = int(input("Az első idő másodperce?> "))

# OraInSec1 = (ora1 * 60) * 60
# MinInSec1 = perc1 * 60

# result1 = OraInSec1 + MinInSec1 + masodperc1
# #---------------------------------------------

# #---------Másik óra---------------------------
# ora2 = int(input("A második idő órája?> "))
# perc2 = int(input("Az második idő perce?> "))
# masodperc2 = int(input("A második idő másodperce?> "))

# OraInSec2 = (ora2 * 60) * 60
# MinInSec2 = perc2 * 60

# result2 = OraInSec2 + MinInSec2 + masodperc2
# #---------------------------------------------

# if result1 > result2:
#     print(result1 - result2)
# else:
#     print(result2 - result1)


# # 6 feladat >  Készíts programot, mely a felhasználótól bekért számról megállapítja, hogy az a.) pozitív, negatív vagy nulla, b.) egész vagy nem egész. Az eredményt a képernyőre szöveges válasz formájában írja ki!


# #7 feladat > Készíts programot, mely beolvas a felhasználótól egy fizetést, és a fizetés nagyságától függően kiírja, hogy az alacsony, átlagos, vagy magas! A kategóriákat a saját preferenciád alapján határozhatod meg! :D

# fizetes = int(input("Add meg a fizetésed> "))

# if fizetes <= 185000:
#     print("Kevés")
# elif fizetes > 185000 >= 270000:
#     print("átlagos")
# elif fizetes > 270000:
#     print("Magas")
# # -------

# # 8 feladat  > Egy turkálóban minden póló darabja 500 Ft. Ha egy vásárlás során valaki több darabot is vesz, a második ára már csak 450 Ft, a harmadik pedig 400 Ft, de a negyedik és további darabok is ennyibe kerülnek, tehát az ár a harmadik vásárlása után már nem csökken tovább. Írj programot, amely a vásárolt pólók darabszámának ismeretében megmondja, hogy mennyit fizet a vásárló!

# ammount = int(input("Add meg a vásálandó pólók darabszámát> "))
# price = 500
# counter = 0
# result = 0

# for i in range(ammount):
#    while counter != 2:
#        result += price
#        price
#        counter += 1

# # 9 feladat >9) Számok kiírása: Az ábrán egy program algoritmusa látható, amely kiírja a számokat 1-től 20-ig.

# num = 1

# while num != 20 + 1:
# 	print(num)
# 	num += 1

# # 10 feladat >Írj programot, amely hatványozni képes! Kérdezze meg az alapot (valós) és a kitevőt (egész), és írja képernyőre a hatvány értékét!

# alap = float(input("Add meg a hatványalapot> "))
# kitevo = int(input("Add meg a kitevőt"))

# result = alap ** kitevo

# print(result)

# 11 feladat >  Készíts programot, amely egy pozitív egész számról négyzetgyökvonás nélkül eldönti, hogy négyzetszám-e!

# This is a test

