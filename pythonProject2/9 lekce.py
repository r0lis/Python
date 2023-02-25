import os
import json

# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    file_path = os.path.join(cwd_path, file_name) #cwd_path - cesta k souboru
    if field not in {"unordered_numbers", "ordered_numbers", "dna_sequence"}:
        return None

    with open(file_path, mode="r") as file:
        slovnik = json.load(file)
    return slovnik[field]


def linear_search(seq, cislo):

    cetnost=0
    indexy = []

    pozice=0
    for prvek in seq:
        if prvek == cislo:
            indexy.append(pozice)
            cetnost += 1
        pozice += 1

    slovnik = {"positions": indexy, "count": cetnost}
    return slovnik

#nejlepší a nejhorší scénář je stejný - vždy musí projít celou sekvenci - složitost omikron(n) - linearní závislost

def pattern_search(sek, vzor):
    delka_vzoru = len(vzor)
    vyskyty = set()
    levy_okraj = 0
    pravy_okraj = delka_vzoru
    while pravy_okraj < len(sek):
        for idx in range(delka_vzoru):
            if vzor[idx] != sek[levy_okraj + idx]:
                break
        else:
            vyskyty.add(levy_okraj + delka_vzoru // 2)
        levy_okraj += 1
        pravy_okraj += 1
    return vyskyty

#složitost - sekvence je delky n - omikron(n); vnitřni for cyklus - delka vzoru m - m se provede n-krát -->
# --> složitost vnitřního cyklu = m.n (nejhorší případ)
#nejlepší případ - pouze v případě, že hned na první pozici neni shoda - omikron(n)

def binary_search(seznam, number):
    delka = len(seznam)
    levy = 0
    pravy = delka - 1

    while levy <=  pravy:
        prostredni = (levy + pravy) // 2

        if seznam[prostredni] == number:
            return prostredni

        if seznam[prostredni] > number:
            pravy = prostredni - 1
        elif seznam[prostredni] < number:
            levy = prostredni + 1

    return None
#asymptoticka složitost:
#nejhorší případ: projede se celý seznam a není tam hledane čislo - omikron(log(n))
# --> po prvni iteraci ---n/2
#--> po druhe iteraci --- n/4
#---> po treti iteraci ---n/8
# po k-té iteraci --- n/2na-k ;  n=2na-k --- log(n) = log(2na-k) --> log(n)= k.log(2) --- k = log(n)

#nejlepší případ - omikron(1) - trefime se napoprve


def main():
    file_name = "sequential.json"
    seq = read_data(file_name, "unordered_numbers")
    print(seq)


    cislo = 9
    slovnik = linear_search(seq, cislo)
    print(slovnik)


    sek = read_data(file_name, "dna_sequence")
    res_2 = pattern_search(sek, "ATA")
    print(res_2)

    seznam = read_data(file_name, "ordered_numbers")
    hledane = binary_search(seznam, number = 4)
    print(hledane)

    pass


if __name__ == '__main__':
    main()