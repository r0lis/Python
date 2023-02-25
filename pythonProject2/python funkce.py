empty_list= list()
print(empty_list)
#tvorba seznamu - prazdny seznam

cisla = [202, 5, 33, 50]
print(cisla)
#seznam cisel - do hranatych zavorek vstup

retezce = ["prvni", "druhy", "treti"]
print(retezce)
#seznam

seznam = [20, 30.3, True, "text"]
print(seznam)
#vice datovych typu

number = [2, 3, 6]
names = ["Alice", "Thomas"]
results = [True, True, False]
print(names + results)
#spojeni vice vstupu
#pokud pouzijeme len(names) nebere pocet znaku, ale pocet jmen - vyslo by 2

week_days = ["pondeli", "utery", "streda", "ctvrtek", "patek", "sobota", "nedele"]
print(len(week_days[2]) == len(week_days[4]))
#zjistujeme jestli delka textoveho retezce 3. a 5. prvku je stejna

prvni_seznam = [True, True]
druhy_seznam = prvni_seznam
prvni_seznam[0] = False
print(prvni_seznam)
print(druhy_seznam)
#seznamy jsou mene - lze je menit - prepsat

#ukol1 - vypisovani cisel pomoci indexovani
my_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
print(my_numbers[5:10])
print(my_numbers[0:13:2])
print(my_numbers[1:12:2])
print(my_numbers[10:5:-1])
print(my_numbers[::-1])
print(my_numbers[::-2])
#pokud od zadu pisu napr. -1

#vnoreny seznam
nested_list = ["a", "b", ["cc", "dd", ["eee", "fyf"]], "g", "h"]
#indexovani vnoreneho seznamu pomoci vicenadobneho indexu
print(nested_list[2])
print(nested_list[2][0])
print(nested_list[2][2][0])
print(nested_list[2][2][1][1])
#druhym prvkem je cely vnoreny seznam cc,dd,eee,fff; pokud chci vypsat jen cc z celeho vnoreneho seznamu, musim dodat dalsi zavorku s O
#ve vnorenem seznamu znovu indexovani 0,1,2,..

#ukol2
nested_list = ["a", "b", ["cc", "dd", ["eee", "fyf"]], "g", "h"]
nested_list[2][1] = 0
nested_list[2][2][1] = 1
print(nested_list)

#metody
#blablabla.append - prida jako posledni do seznamu zadanou vec, dela vnoreny seznam
rings = ["legolas", "gimli"]
rings.append("aragorn")
print(rings)

#extend - vezme jednotlive prvky a rozsiri puvodni seznam, nedela vnoreny seznam
rings = ["aragorn"]
next_names = ["legolas", "gimli"]
rings.extend(next_names)
print(rings)

rings = ["aragorn"]
next_names = ["legolas", "gimli"]
rings.append(next_names)
print(rings)

#remove - odstraneni
rings = ["aragorn", "gimli", "legolas"]
rings.remove("gimli")
print(rings)

#pop - odstraneni nejakeho prvku, kdyz nevim co za orvek to je; v indexu uvedu jaky prvek chci odstranit
rings = ["aragorn", "gimli", "legolas"]
rings.pop(0)
print(rings)
#pop ma navratovou hodnotu, lze ulozit ten odstraneny prvek do promene
rings = ["aragorn", "gimli", "legolas"]
odstraneno = rings.pop(0)
print(odstraneno)

#insert - vlozeni prvku na zadany index - dva vstupni argumenty - prvni je index a druhy je objekt, ktery chceme do seznamu vlozit
rings = ["gimli", "legolas", "aragorn"]
rings.insert(0, "Frodo")
print(rings)