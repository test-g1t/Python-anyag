# alap lista
numbers = [10, 5, 7, 2, 1]
print("Ez az eredeti lista", numbers)


newList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# az 1 ==> 0.-ik tag,
# 2 ==> az 1. tag
# és így tovább
# ez minden listában így van

numbers[0] = 111
###################################
# numbers[0] = x
# az x egy új lista tag ami lehet szám vagy szó is
# és nem kicsréli a 0.-ik tagot hanem beszúrja a mostani elé
###################################
print("Ez pedig a módosított lista", numbers)


###################################
# len(x) függvény
# x ==> a lista neve
# megszámlálja a lista hosszát
###################################


# Írassuk ki a programunkal a litának a hosszát
myList = [1, 2, "ListaElem", 20, 2.2]
print("A lista", len(myList), "tag hosszú.")
