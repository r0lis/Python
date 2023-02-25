#cykly foor, loop
#for - presny pocet opakovani, o kterem vime
#promenna iterabilni - pomoci ni ukazujeme na urcite prvky
#ridici promenna - do ni se prirazuji postupně polozky z promenne iterabilni

game_of_houses = ["Lanister", "Stark", "Tyrell", "Martel", "Tarly", "Bolton"]
print(f"I support {game_of_houses[0]} family.")
print(f"I support {game_of_houses[1]} family.")
print(f"I support {game_of_houses[2]} family.")


game_of_houses = ["Lanister", "Stark", "Tyrell", "Martel", "Tarly", "Bolton"]
for house_name in game_of_houses:
    print(f"I support {house_name} family.")

#rizeni cyklu
#pomoci podminky a break
#nebo pomoci podminky a continue


#vypsat prvni tri prvky
game_of_houses = ["jedna", "dva", "tri", "ctyri", "pet", "sest"]
for house_name in game_of_houses:
    if house_name == game_of_houses[3]:
        break
    print(f"I support {house_name} family.")


#program preskoci prvni dva prvky
game_of_houses = ["sedm", "osm", "devet", "deset", "jedenact", "dvanact"]
for house_name in game_of_houses:
    if house_name == game_of_houses[1] or house_name == game_of_houses[-1]:
       continue
    print(f"I support {house_name} family.")


#funkce range
#pokud neco opakujeme n-krat muzeme pouzit tuto funkci, ktera vraci sekvenci cisel
#pro prevedeni na seznam musime pouzit jeste funkci list
print(list(range(5)))


for number in range(5):
    print("hello")
    print(number)

#konkretni rozsahy funkce range
for number in range(0, 5, 2):
    print(number)

#cisla od 6 do 10
for number in range(6, 11):
    print(number)

#licha cisla od 1 do 12
for number in range(1, 13, 2):
    print(number)