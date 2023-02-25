#cyklus while - ukončen podmínkou
# while (condition):

number = 1
max_number = 7
while number <= max_number:
    print(number)
    number = number + 1
#cyklus se provádí do doby, kdy platí podmínka

""" 
number = 1
max_number = 7
while number <= max_number:
    if number % 2 == 0:
        print(number)
    number = number + 1
print(number)
# cyklus vypisuje suda cisla 
"""

#řízení cyklů
# break ukončí celý cyklus
#continue ukončí aktuální iteraci, ne celý cyklus
MAX_NUMBER_OF_GUESS = 5
number_of_guess = 0

while True:
    number_of_guess = number_of_guess + 1
    print(number_of_guess)
    if number_of_guess == MAX_NUMBER_OF_GUESS:
        break


list_of_tuples = [(1, 2, 3), (3, 4, 5), (5, 6, 7)]
while list_of_tuples:
    numbers = list_of_tuples.pop(0) #metoda pop vybere prvek (nejdřive zavorku 1,2,3; pak 3,4,5,..)
                                    # a uloží do proměnné numbers
    for number in numbers:
        if number == 3:
            break
        print(f"Processing {number}")

#misto if cyklus while
data_stream = [0, 3, 10, "null", -5, 23, "null", -8, "error", 13, 0, 0]
data = []

while data_stream:
    element = data_stream.pop(0)
    if isinstance(element, str) == True:
        if element == "error":
            break
        else:
            continue
    if element < 0:
        element = element * (-1)
    data.append(element)
print(data)