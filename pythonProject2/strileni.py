import random

print("napis pocet tercu")
pocetTercu = int(input())
zasobnikNaboje = 8
print(zasobnikNaboje)
zasah = 0
vedle = 0

for terc in range(pocetTercu):
    for naboje in range(zasobnikNaboje):
        rnd = random.randrange(0, 101)
        if(rnd > 45):
            zasah = zasah + 1
            print("zasah")
        else:

            print("vedle")


zasobnikNaboje = 8
procent = ((zasah * 100) / 8) / pocetTercu
print(f"vase procentualni uspesnost je {procent}%")




