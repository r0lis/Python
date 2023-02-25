
def id_is_valid(personal_id, control_number=11):
    """
    kontrola rodného čísla
    :param personal_id: rodné číslo, které se kontroluje
    :param control_number: čislo, pomocí kterého se kontroluje
    :return:
    """
    delka = len(personal_id)

    if (delka == 9) or (delka == 10):
        if (int(personal_id) % control_number) == 0:
            return True, "Úspěšně ověřeno."
        else:
            return False, "Rodné číšlo není dělitelné."
    else:
        return False, "Toto je špatná délka."

rodne_cislo = "0000000012"
control_number = 11 #pokud bychom ji chtěli tisknout, musí být zde uvedena, jinak je proměnná pouze uvnitř funkce
print(id_is_valid(rodne_cislo))
print(control_number)
#namespace - jmený prostor, patří funkci, to co je uvnitř funkce, je pouze uvnitř funkce


def local_id():
    personal_id = "local_id" #stejná proměnná jako dole, ale nijak to neovlivňuje, protože je uvnitř funkce v namespace
    print(personal_id)
local_id()