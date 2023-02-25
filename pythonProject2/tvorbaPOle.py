import numpy as np

pole = np.array([0, 1, 2, 3]) #tvorba pole na základě nějakých vstupních dat
print(pole)

pole = np.zeros(5) #pole o velikosti 5 plné 0
print(pole)

pole = np.ones(5)
print(pole)

pole = np.random.rand(3) #pole s náhodnýma prvkama o velikosti 3
print(pole)

pole = np.arange(1, 6, 2) #pole s nějakým určitým rozsahem - od 1 do 6, beru každé druhé čislo
print(pole)

pole = np.array([1, 2, 3, 4, 5])
for prvek in pole:
    print(prvek)


# 2D pole:
pole = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]) #matice
print(pole)

#indexovani:
pole = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(pole[0, 2]) #první index jaký vnořený seznam, druhý index jaký prvek + možný i rozsah (0, 1:3)

#3D pole:
pole = np.random.rand(2, 3, 2) #(sloupce, řádky, vrstvy)
print(pole)
print(pole[0, 1, 0])


pole = np.array([0, 1, 2, 3])
vynasobene = pole * 5 #každý prvek z pole je vynásobený 5
print(vynasobene)

pole = np.array([0, 1, 2, 3])
podminka = pole > 1 #výstup - logické hodnoty, dle podmínky
print(podminka)


pole1 = np.array([0, 1, 2, 3])
pole2 = np.array([4, 5, 6, 7])
print(pole1 + pole2)

pole = np.array([2, 4, 6, 8, 10, 12, 14, 16])
indexy = np.array([1, 3, 4])
print(pole[indexy])

pole = np.array([2, 4, 6, 8, 10])
indexy = np.array([False,True, True, False, False])
print(pole[indexy])

#podmíněné indexování!!!:
pole = np.array([2, 4, 6, 8, 10])
hodnoty = pole[pole > 5]
print(hodnoty)

#požadavky na datové typy:
pole = np.ones(4, dtype=float)
print(pole.dtype)

pole_int = pole.astype(int) #přepis na integer
print(pole_int.dtype)

#změna velikosti:
pole = np.array([[0, 1, 2, 3], [4, 5, 6, 7]])
velikost = pole.shape
print(velikost)

""" pole = pole.reshape([4, 2])
print(pole)
velikost = pole.shape
print(velikost) """