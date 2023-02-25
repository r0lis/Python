
def kresli_sudoku(sudoku):
    index = 0
    for i in sudoku:

        if index < 9:
            print(i)
            index = index + 1
        else:
            print()
            continue

def dopln_zadane_cislo(sudoku, indexSloupce, indexRadku, zadaneCislo):
    delka = 9
    x = 0
    y = 0
    pomocna = 0
    while x + 1 == indexSloupce and y + 1 == indexRadku:
        for x in range(delka):
            for y in range(delka):
                vyslednyindex = [x,y]

    sudoku.pop(sudoku[vyslednyindex])
    sudoku[vyslednyindex] = zadaneCislo
    return  sudoku







def over_vstup(sudoku, indexSloupce, indexRadku, zadaneCislo):
    pravidla = 0
    if zadaneCislo > 1 and zadaneCislo < 9:
        pravidla = pravidla + 1
    elif  isinstance(zadaneCislo, str):
        pravidla = pravidla + 1
    elif indexRadku and indexSloupce == "?":
        pravidla = pravidla + 1
    startRow = 9 - 9 % 3
    startCol = 9 - 9 % 3
    for i in range(3):
        for j in range(3):
            if sudoku[i + startRow][j + startCol]:
                return False
    return True


    if pravidla == 5:
        return True



def main(sudoku):

    while True:
        print(kresli_sudoku(sudoku))
        indexSloupce = input("Napis index sloupce")
        indexRadku = input("Napis index radku")
        zadaneCislo = input("Napis cislo ktere chces pridat")
        print(dopln_zadane_cislo(sudoku, indexSloupce, indexRadku, zadaneCislo))

        for i in sudoku:
            if i == "?":
                otaznik = otaznik + 1
            elif otaznik == 1:
                otazka = input("chcete pokracovat? Y/N")
            elif otazka == "Y":
                continue
            elif otazka == "N":
                print("toto jste nezvladl/a")
                break
            elif otaznik == 0:
                print("gratuluji")



if __name__ == '__main__':
    sudoku = [["?",6,4,"?","?","?",1,2,"?"],["?","?","?",4,"?",9,"?","?","?"],[7,9,"?","?",1,"?","?",3,4],[4,"?",1,"?",9,"?",3,"?",8],[9,"?","?","?",7,"?","?","?",2],[8,"?",3,"?",4,"?",7,"?",5],[2,1,"?","?",6,"?","?",7,3],["?","?","?",8,"?",7,"?","?","?"],["?",4,7,"?","?","?",9,8,"?"]]
    main(sudoku)