

x = [2, 10, 5, 6, 17, 21]
y = [2, 8, 10, 11, 12, 16, 20]
z = []
pos = 0
maxi = x[0]


for i in range(len(y)):
  x.append(y[i])

for j in range(len(x)-1):
    maxi = x[0]
    for i in range(len(x)):

        if maxi < x[i]:
            maxi = x[i]
            pos = i

    if maxi not in z:
        z.append(maxi)

    del x[pos]

z.sort()
print('z: '+str(z))
pocet = len(z)

if (pocet % 2) == 0:
    K = 2

    strt_idx = (len(z) // 2) - (K // 2)
    end_idx = (len(z) // 2) + (K // 2)

    middle_element2 = z[strt_idx: end_idx]
    print(middle_element2)
    middle_element = middle_element2[0]
else:
    middle_element = (len(z) -1) // 2

print("kdyz je vyspledne pole sude najdu 2 prostredni prvky v seznamu z ale vezmu to prvni od zacatku")

print("tady je to prvni ze zacatku de")


print(middle_element)

if middle_element > 1:
    # check for factors
    for i in range(2, middle_element):
        if (middle_element % i) == 0:
            print(middle_element, "is not a prime number")
            print(i, "times", middle_element // i, "is", middle_element)
            break
    else:
        print(middle_element, "is a prime number")

# if input number is less than
# or equal to 1, it is not prime
else:
    print(middle_element, "is not a prime number")




