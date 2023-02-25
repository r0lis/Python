WORDS = {
    "B": ["byt", "bydlit", "obyvatel", "byt", "pribytek", "nabytek", "dobytek", "obycej", "bystry", "bylina", "kobyla",
          "byk", "Pribyslav"],
    "L": ["slyset", "mlyn", "blyskat se", "polykat", "plynout", "plytvat", "vzlykat", "lysy", "lytko", "lyko", "lyze",
          "pelynek", "plys"],
    "M": ["my", "myt", "myslit", "mylit se", "hmyz", "mys", "hlemyzd", "mytit", "zamykat", "smykat", "dmychat",
          "chmyri", "nachomytnout se", "Litomysl"],
    "P": ["pycha", "pytel", "pysk", "netopyr", "slepys", "pyl", "kopyto", "klopytat", "trpytit se", "zpytovat", "pykat",
          "pyr", "pyrit se", "cepyrit se"],
    "S": ["syn", "syty", "syr", "syrovy", "sychravy", "usychat", "sykora", "sycek", "sysel", "sycet", "sypat"],
    "V": ["vy", "vysoky", "vyt", "vyskat", "zvykat", "zvykat", "vydra", "vyr", "vyzle", "povyk", "vyhen"],
    "Z": ["brzy", "jazyk", "nazyvat", "Ruzyne"]
}

BAD_WORDS = {
    "B": "bivak",
    "L": "liska",
    "M": "mince",
    "P": "pivo",
    "S": "simona",
    "V": "vidle",
    "Z": "zitra",
}


def generate_bad_word(chosen_letter):
    bad_word = BAD_WORDS[chosen_letter]

    return bad_word


def generate_orig_words(chosen_letter):
    chosen_words = WORDS[chosen_letter].copy()

    return chosen_words