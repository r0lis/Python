def vytvorhlediste(pocetsedadelvrade, pocetrad):
    hlediste = []
    hotovo = int(pocetrad)
    sedla = int(pocetsedadelvrade)

    index = 0
    if (int(pocetsedadelvrade) * int(pocetrad)) > 150:
        return False


    for rady in range(int(pocetrad)):
        for sedadla in range(sedla):

            if int(pocetsedadelvrade) == sedadla:
                print()
                continue
            else:
                hlediste.extend("0")
                sedadla = False
                sedla = sedla - 1
                continue

        Vystuphlediste = hlediste
        print(Vystuphlediste)




















def main():
    pocetsedadelvrade = input("napis pocet sedadel v rade: ")
    pocetrad = input("napis pocet rad: ")
    print(vytvorhlediste(pocetsedadelvrade, pocetrad))





print(main())
