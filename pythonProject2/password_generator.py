
import random
SYMBOL_GROUPS1 = ['/#&@@{@}()','QWERTZUIOPLKJHGFDSAYXCVBNM','qwertzuioplkjhgfdsaxycvbnm','1236547890']
SYMBOL_GROUPS2 = ['QWERT','qwert','.,:-_']

def check_if_contains_any(heslo, skupina):

    """
    funkce má za úkol kontrolovat, zda se nachází symbol v hesle
    :param heslo: dané heslo
    :param skupina: skupina symbolů
    :return: True - pokud se symbol v hesle nachází, False - pokud ne
    """


    for index in skupina:
        if index in heslo:

            print(True)
        else:

            print(False)
        return

def validate_password(heslo, list, len_x):

    """
    funkce kontroluje jak dlouhé je heslo a jestli obsahuje alespoň jeden znak z jednotlivých skupin znaků
    :param heslo: vstupem je dané heslo
    :param list: vstupní parametr obsahující skupinu symbolů
    :param len_x: vstupní parametr minimální délky hesla
    :return: True - pokud heslo splňuje všechny podmínky, False - pokud ne
    """

    is_ok = True
    if (len(heslo) != len_x):
        is_ok = False
    for skupina in list:
        is_ok2 = False
        for znak in skupina:
            if znak in heslo:
                is_ok2 = True
        if is_ok2 == False:
            is_ok = False
    return is_ok

def generate_password(len_x, list):

    """
    funkce generuje náhodné heslo
    :param len_x: vstupní parametr minimální délky hesla
    :param list: vstupní parametr skupiny symbolů, kde každý prvek obsahuje řetězec skupiny znaků
    :return: výstupem je vygenerované heslo
    """

    nove_heslo = ""
    for i in range(len_x):
        skupina = list[random.randint(0, len(list) -1)]
        znak = skupina[random.randint(0, len(skupina) -1)]
        nove_heslo = nove_heslo + znak

    return nove_heslo


def main(len_x, list):

    """
    řídí celý program, vygeneruje náhodné heslo a následně jej ověří, do té doby, než heslo splní požadavky
    :param len_x:  požadovaná délka hesla
    :param list: skupiny symbolů
    :return: výstupem je vygenerované heslo
    """

    ok = False
    heslo = ""
    while (not ok):
        heslo = generate_password(len_x, list)
        ok = validate_password(heslo, list, len_x)
    return heslo
    heslo12 = "ahoj"
    print(check_if_contains_any(heslo12, symbol_groups))

if __name__ == '__main__':


    length = 5
    symbol_groups = SYMBOL_GROUPS1
    symbol_groups = SYMBOL_GROUPS2
    password = main(length, symbol_groups)
    print(password)