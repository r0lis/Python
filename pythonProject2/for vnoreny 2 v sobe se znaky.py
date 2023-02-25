for out_idx in range (3): #vnejsi cyklus
    print(f"Spouštím {out_idx}. běh vnějšího cyklu.")
    for in_idx in range (2): #vnitrni cyklus
        print(f"\tSpouštím {in_idx}. běh vnitřního cyklu.")


#ukol
CONSONANTS = "qwrtzpsdfghjklxcvbnmščřžďťř"
VOWELS = "aeiouyáéíóúůý"

cities = ["Brno", "Nezamyslice", "Ostrava"]
for city in cities: #vnejsi cyklus
    for char_index, char in enumerate(city.lower()): #vnitrni cyklus
        if char in VOWELS:
            print(f"{char_index}. znak {char} mesta {city} je samohlaska.")
        elif char in CONSONANTS:
            print(f"{char_index}. znak {char} mesta {city} je souhlaska.")
        else:
            print(f"{char_index}. znak {char} mesta {city} patri mezi ostatni znaky.")