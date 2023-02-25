# tvorba funkce
# zápis pomocí def + název funkce (argument - proměnná, se kterou program pracuje)
def absolutni_hodnota(cislo):
    """
    #docstring - dokumentační řetězec
    funkce pro výpočet absolutní hodnoty
    :param cislo: cislo jehož absolutní hodnotu chci zjistit
    :return:
    """
    #za docstring body v písemce, psát vždy!!
    if cislo >= 0:
        return cislo #return - funkce vrátí číslo, které si dále můžeme uložit, zároveň ukončuje běh funkce
                    # pokud bychom chtěli něco tisknout musíme dát print před return
    else:

        return -cislo
    # pouze zadefinovaná funkce,musíme ji zavolat
vysledek = absolutni_hodnota(-5) #počet argumentů a parametrů můsí být téměř vždy shodný
print(vysledek)



def mocniny(seznam, mocnina):
    """
    funkce má umocnit seznam čísel na libovolnou kladnou hodnotu
    :param seznam:
    :param mocnina:
    :return:
    """
    umocneny_seznam = list()
    for prvek in seznam:
        umocneny_seznam.append(prvek ** mocnina)
    return umocneny_seznam

print(mocniny([1, 2, 3], 3)) #seznam čísel (1,2,3) mocnime číslem 3


#nepovinný parametr - do definice funkce přímo zvolíme parametr
def mocniny(seznam, mocnina=2):
    umocneny_seznam = list()
    for prvek in seznam:
        umocneny_seznam.append(prvek ** mocnina)
    return umocneny_seznam

print(mocniny([1, 2, 3]))

# nebo:

def mocniny(seznam, mocnina):
    umocneny_seznam = list()
    for prvek in seznam:
        umocneny_seznam.append(prvek ** mocnina)
    return umocneny_seznam

print(mocniny(mocnina=2, seznam=[2, 3, 4]))

#return - může vrátit cokoliv, textový řetězec, číslo, matematický operátor, cokoliv

#ukol:
def mocniny(seznam, mocnina):
    umocneny_seznam = list()
    for prvek in seznam:
        if isinstance(prvek, float) or isinstance(prvek, int):
            umocneny_seznam.append(prvek ** mocnina)
        else:
            return seznam, True, "Invalid data type.."
    return umocneny_seznam, False, "Mocnění hotovo."
vystup_fce = mocniny([5, 6, 7, "ahoj"], 2)
print(vystup_fce) #výstupem je n-tice o třech prvcích
#n-tice - neměnný obsah, lze indexovat - lze vytáhnout např. jeden prvek : vystup_fce = mocniny([5, 6, 7, "ahoj"], 2)[2]

#rozbalení n-tice
def mocniny(seznam, mocnina):
    umocneny_seznam = list()
    for prvek in seznam:
        if isinstance(prvek, float) or isinstance(prvek, int):
            umocneny_seznam.append(prvek ** mocnina)
        else:
            return seznam, True, "Invalid data type.."
    return umocneny_seznam, False, "Mocnění hotovo."
vystup_fce, chyba, zprava = mocniny([5, 6, 7], 2) #rozbalení do třech proměnných, které již můžeme měnit,..
print(vystup_fce)