def kresli_sudoku(sudoku):

    index = 0
    for prvek in sudoku:
        if index < 9:
            print(prvek)
            index = index + 1
        else:
            print("\n")
            continue


    for i in range(len(sudoku)):
        for j in range(len(sudoku[i])):
            print(sudoku[i][j], end=" ")
        print()



def dopln_zadane_cislo(sudoku, indexSloupce, indexRadku, zadaneCislo):
    sudoku[indexRadku][indexSloupce] = zadaneCislo
    return sudoku



def over_vstup(sudoku, indexSloupce, indexRadku, zadaneCislo):
    ok = True
    if(zadaneCislo >= 9) and (zadaneCislo <= 1):
        ok = False
    if (sudoku[indexRadku][indexSloupce] != "?"):
        ok = False
    for i in range(len(sudoku)-1):
        if zadaneCislo == sudoku[indexRadku][i]:
            ok = False
        if zadaneCislo == sudoku[i][indexSloupce]:
            ok = False


    return ok


def main(sudoku):
    pocet_otazniku = 0
    cisla = []
    for radek in sudoku:
        for index in radek:
            if index == "?":
                pocet_otazniku = pocet_otazniku + 1

    while pocet_otazniku > 0:
        kresli_sudoku(sudoku)
        zadaneCislo = int(input("zadej cislo ktere chces vlozit: "))
        index_radku = input("zadej cislo radku vkladaného čísla: ")
        index_radku = int(index_radku)-1
        index_sloupce = input("zadej cislo sloupce -=-: ")
        index_sloupce = int(index_sloupce)-1

        if over_vstup(sudoku, index_sloupce, index_radku, zadaneCislo):
            cisla.append(zadaneCislo)
            sudoku = dopln_zadane_cislo(sudoku, index_sloupce, index_radku, zadaneCislo)
            pocet_otazniku = pocet_otazniku -1
            if pocet_otazniku == 0:
                print("konec hry vyhral jsi")
                break

        else:
            print("špatné číslo")
            print("pokud nechces dale hrad zadej 'N', v druhem pripada zadej ENTER")
            if str(input()) == "N":
                print(f"prohral jsi, pocet doplnenich cisel: {len(cisla)}")
                break
            else:
                continue
        print()


if __name__ == '__main__':
    sudoku = [["?",6,4,"?","?","?",1,2,"?"],["?","?","?",4,"?",9,"?","?","?"],[7,9,"?","?",1,"?","?",3,4],[4,"?",1,"?",9,"?",3,"?",8],[9,"?","?","?",7,"?","?","?",2],[8,"?",3,"?",4,"?",7,"?",5],[2,1,"?","?",6,"?","?",7,3],["?","?","?",8,"?",7,"?","?","?"],["?",4,7,"?","?","?",9,8,"?"]]
    main(sudoku)
