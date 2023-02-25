import random
from seznam import generate_bad_word, generate_orig_words



POSSIBLE_LETTERS = ["B", "L", "M", "P", "S", "V", "Z"]
def choose_set(pismeno):

    slovo = generate_bad_word(pismeno)
    abeceda = generate_orig_words(pismeno)
    delkaAbecedy = len(abeceda)
    rnd = random.randint(0, delkaAbecedy)
    abeceda.insert(rnd, slovo)
    return abeceda




def find_bad_word(abeceda , pismeno):
    i = 0
    for slovo in abeceda:
        if (pismeno.lower() + "i") in slovo:
            return slovo, i
        i += 1


def main():
    while True:
        chosen_letter = str(input("napis pismeno "))
        chosen_letter = chosen_letter.upper()
        if chosen_letter in POSSIBLE_LETTERS:
            print(f"Pismeno {chosen_letter} je v pořádku")
            abeceda = choose_set(chosen_letter)
            pozice = find_bad_word(abeceda, chosen_letter)
            break
        else:
            print(f"Pismeno {chosen_letter} neni spravne")






if __name__ == '__main__':
    main()