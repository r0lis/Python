most_wanted = {"Pablo Escobar": 150, "Joaqim Guzmán": 125} #klíč:jeho hodnota
print(most_wanted["Pablo Escobar"]) #chci zjistit hodnotu, která odpovídá klíči

#vložení nového prvku
most_wanted = {"Pablo Escobar": 150, "Joaqim Guzmán": 125}
most_wanted["Ismael Gracia"] = (52, 50, 63)
print(most_wanted)

#uprava prvku
most_wanted = {"Pablo Escobar": 150, "Joaqim Guzmán": 125}
most_wanted["Pablo Escobar"] = (163, 35)
print(most_wanted)


#vymazání prvku
most_wanted = {"Pablo Escobar": 150, "Joaqim Guzmán": 125}
del most_wanted["Joaqim Guzmán"]
print(most_wanted)


#spojení seznamů - operace zip
names = ["Pablo Escobar", "Joaqim Guzmán", "Ismael Garcia"]
production = [(138, 164, 151), (125, 113, 113), (52, 50, 63)]
most_wanted = dict(zip(names, production))
print(most_wanted)


""" 

dict_keys = most_wanted.keys() #klíče slovníku
dict_values = most_wanted.values() #hodnoty slovníku 

for key in most_wanted:
    print(key)                      ---prochází klíče--
for key in most_wanted.keys():
    print(key)
for value in most_wanted.values():     --prochází hodnoty---
    print(value)
for key, value in most_wanted.items():   --metoda .items - dvě hodnoty - klíč, hodnota -- 
    print(f"{key}: {value}")

"""