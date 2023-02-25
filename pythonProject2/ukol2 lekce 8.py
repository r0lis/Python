def number_of_unique_items(visitor_ip):
    unikatni = list()
    pocet = 0
    for prvek in visitor_ip:
        if prvek not in unikatni:
            unikatni.append(prvek)
            pocet += 1
    return pocet, unikatni

def main (vstup):
    print(number_of_unique_items(vstup))

if name == 'main':
    visitor_ip = ["198.125.1.000", "198.253.100.100", "120.5.5.5", "53.130.0.0", "120.5.5.5"]
    main(visitor_ip)