Uppercase_Alphabets = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
cislo = input("zadej pismeno ja ho prevedu do ascci sracky: ")
if int(cislo) > 0 and int(cislo) <= 26:
    asccicislofake = Uppercase_Alphabets[int(cislo) - 1]
    print(f"cislo {cislo} je v ascci: {asccicislofake}")

else:
    cislo = input("zadej pismeno ja ho prevedu do ascci sracky: ")
    asccicislofake = Uppercase_Alphabets[int(cislo) - 1]
    print(f"cislo {cislo} je v ascci: {asccicislofake}")






