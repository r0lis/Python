import numpy as np

pole = np.arange(0, 21)
umocneny = pole ** 3
pole2 = umocneny
pole2[pole2 > 10] = 0
suma = np.sum(pole2)
maximum = np.max(pole2)
print(suma, maximum)