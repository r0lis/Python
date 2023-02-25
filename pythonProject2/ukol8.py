import numpy as np
import matplotlib.pyplot as plt

SIGNAl_THRESHOLD = -0.15
IMAGE_THRESHOLD = 0.25

def read_data(pacient):
    txtsoubor = "input_data/pacient_"+str(pacient)+".txt"

    with open(txtsoubor, mode="r") as txt:
        signal_str = txt.read()

    signal_str = signal_str.split(", ")
    signal_str = list(signal_str)

    i=0
    for prvek in signal_str:
        signal_str[i] = float(prvek)
        i+=1

    signal_pole = np.array(signal_str)

    pngpath = "input_data/pacient_"+str(pacient)+".png"
    obraz = plt.imread(pngpath, format="png")

    return obraz, signal_pole


def analyze_image(obraz):
    maska = obraz < IMAGE_THRESHOLD

    pole1 = np.sum(maska)
    poleCele = np.shape(maska)
    pomerPlocha = (pole1/(poleCele[0]*poleCele[1]))
    poleIntenzita = obraz[maska]
    intenzita = np.mean(poleIntenzita)

    return maska, pomerPlocha, intenzita

def analyze_signal(signal):
    Rvlny = signal < SIGNAl_THRESHOLD
    i = 0
    for prvek in Rvlny:
        if prvek == True:
            if Rvlny[i+1]==True:
                Rvlny[i] = False
        i+=1
    Rvlny[-1] = False

    pocetR = np.sum(Rvlny)
    tepFrekvence = (pocetR/10)*60

    return Rvlny, tepFrekvence

def main():
    cislaPole = [0,1,2]

    for prvek in cislaPole:
        pacient = prvek

        obraz, signal = read_data(pacient)

        maska, pomerPlocha, intenzita = analyze_image(obraz)

        Rvlny, tepFrekvence = analyze_signal(signal)

        print(f"číslo pacienta: {pacient}")
        print(f"Poměrná plocha cév: {pomerPlocha}")
        print(f"Průměrná intenzita: {intenzita}")
        print(f"Tepová frekvence: {tepFrekvence}")
        plt.imshow(obraz)
        plt.show()
        plt.imshow(maska)
        plt.show()
        plt.plot(signal)
        plt.show()
        plt.plot(Rvlny)
        plt.show()

if __name__ == "__main__":
    main()