#tuples - datova struktura n-tic
day_tuple = (0, "Monday")
print(day_tuple)

day = day_tuple[1]
print(day)

#u n-tic nelze dodatecne menit
#day_tuple[1] = "Tuesday" nelze
#stejne tak nefunguje napr. metoda append
#day_tuple.append("28.2.2022")

index, day = day_tuple
print(day)
print(index)

#funkce enumerate - ocislovani sekvence
days = ["monday", "tuesday", "wednesday", "thu", "fri", "sat", "sun"]
print(list(enumerate(days)))

for day_index, day in enumerate(days):
    print(f"{day_index + 1}. day of the week is {day}.")


#funkce zip - prochazi vice seznamu soucasne
cities = ["Tokyo", "Stockholm", "London"]
countries = ["Japan", "Sweden", "UK"]
print(list(zip(cities, countries)))


cities = ["Tokyo", "Stockholm", "London", "Vatican"]
countries = ["Japan", "Sweden", "UK"]
numbers = range(3)

for city, country, number in zip(cities, countries, numbers):
    print(f"{number + 1}. {city} is in {country}")
