def update_ascending_sequence(sequence, to_add_seq):
    """
    Returns updated number sequence in ascending order
    :param list sequence: Sequence of input numbers
    :param list to_add_seq: Randomized generated numbers to add to the input sequence
    :rtype: (list, int, bool)
    :return: A list with randomized numbers added to correct position of input sequence,
    value of middle element and True if middle element is a prime number
    """

    # Muzes si pro zacatek zadefinovat nektere promenne, ale tez nemusis

    pos = 0
    sop = 0
    while(pos != len(to_add_seq)):
        while (sop != len(sequence)):
                sop = sop + 1
        sequence.insert(sop , to_add_seq[pos])
        pos = pos + 1
        sop = 0
    sequence.sort()
    sequence = list(dict.fromkeys(sequence))


    pocet = len(sequence)



    # Jednotlive prvky ze seznamu to_add_seq pridavej postupne na spravna mista seznamu sequence tak,
    # aby byla zachovana posloupnost cisel.


    # Zjisti hodnotu prostredniho prvku

    if (pocet % 2) == 0:
        K = 2
        strt_idx = (len(sequence) // 2) - (K // 2)
        end_idx = (len(sequence) // 2) + (K // 2)

        middle_element = sequence[strt_idx: end_idx]

        middle_element = middle_element[0]
    else:
        middle_element = sequence[int((len(sequence)-1)/2)]


    # Zjisti, jestli je prostredni prvek prvocislo

    if middle_element > 1:
        for i in range(2, middle_element):
            if (middle_element % i) == 0:
                is_prime = False
                break
        else:
            is_prime = True

    else:
        is_prime = True



    return sequence, middle_element, is_prime


if __name__ == "__main__":
    input_sequence = [2, 8, 10, 11, 12, 16, 20]
    print(f"Input sequence: {input_sequence}")
    to_add = [2, 10, 5, 6, 17]
    print(f"Random list: {to_add}")
    final_sequence, middle, is_middle_prime = update_ascending_sequence(input_sequence, to_add)
    print(f"Your merged list: {final_sequence} \nMiddle element {middle} is prime: {is_middle_prime}")