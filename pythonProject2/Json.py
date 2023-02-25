import json #pojí se se slovníkem

json_string = """
    {"name": ["Jiri", "Michal"], "age": [30, 25], "city": ["Praha", "Brno"]}
"""
persons = json.loads(json_string) #přetvoření do slovníku
print(persons)

"""
 with open("personal_data.json") as data_file:
    data = json.load(data_file)
--při práci s textovými soubory - načtení dat z JSON souboru 
"""

with open("personal_data.json", mode="w") as json_file: #režim "W" - můžeme do něho zapisovat
    json.dump(persons, json_file, indent=4, sort_keys=True)