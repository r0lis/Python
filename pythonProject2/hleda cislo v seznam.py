list = [1, 2, 3, 4, 5, 6, 7]
search = 5
index = 0
while search != list[index]:

    index = index + 1

    if index == len(list) - 1:
        print("cislo neni v seznamu")
        break

if search == list[index]:
    print(search)