#množiny obsahují pouze unikátní prvky, nelze indexovat
#množiny - pomocí složených závorek; intersection(průnik), union(sjednocení), difference(rozdíl)

duck_family = {"Huey", "Dewey", "Louie", "Louie"}
print(duck_family)

duck_family = {"Huey", "Dewey", "Louie", "Louie"}
print("Huey" in duck_family) #nachází se prvek v množině?


duck_family = {"Huey", "Dewey", "Louie", "Louie"}
duck_family.add("Daisy")
print(duck_family)

duck_family = {"Huey", "Dewey", "Louie", "Louie"}
duck_family.remove("Dewey")
print(duck_family)

duck_family = {"Huey", "Dewey", "Louie", "Louie"}
odstraneny = duck_family.pop() #odstraní vždy jiný prvek, jelikož jsou prvky vždy jinak poskládané
print(odstraneny, duck_family)

#pokud chceme z množiny odstranit prvek, o kterem nevíme, zda v množině je použijeme funkci discard
duck_family = {"Huey", "Dewey", "Louie", "Louie"}
duck_family.discard("utery") #program nevyhodí žádnou chybu, běží dál
print(duck_family)


seznam = [2, 3, 4, 5, 6, 4, 3]
mnozina = set(seznam) #odstranění duplicit - převedení na množinu
print(mnozina)