"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

autor: Renato Vítek
email: renev6548@gmail.com
"""
# import potřebných modulů 
import random


cara = "-" * 86

# Funkce pro pozdravení uživatele
def pozdrav_uzivatele():
    print(cara)
    print("Vítejte ve hře Bulls and Cows!")
    print(cara)
    print("Vaším úkolem je uhodnout tajný čtyřmístný kód.")
    print("Kód obsahuje čtyři unikátní číslice a nezačíná nulou.")
    print("Po každém pokusu obdržíte zpětnou vazbu ve formě počtu 'Byků' a 'Krav'.")
    print("Byci: Správné číslo na správné pozici.")
    print("Kravy: Správné číslo na špatné pozici.")
    print("Hodně štěstí!")
    print("Pokud chcete hru ukončit, zadejte misto kodu 'konec'.")
    print(cara)

# Funkce pro vygenerování tajného čtyřmístného kódu
def generuj_kod():
    prvni_cislice = random.choice(range(1, 10))  # První číslice nebude 0
    ostatni_cislice = random.sample(range(10), 3)  # Zbývající číslice
    while prvni_cislice in ostatni_cislice:  # Pojistka proti opakování číslic
        ostatni_cislice = random.sample(range(10), 3)
    return [prvni_cislice] + ostatni_cislice  # Vrátí seznam čtyř čísel

# Funkce pro vyhodnocení hádání
def vyhodnot_hadani(hadani, kod):
    bulls = sum(1 for i in range(4) if hadani[i] == kod[i])
    cows = sum(1 for i in range(4) if hadani[i] in kod and hadani[i] != kod[i])
    return bulls, cows

# Hlavní funkce hry
def hra():
    pozdrav_uzivatele()
    kod = generuj_kod()
    pokusy = 0

    while True:
        hadani = input("Zadejte svůj čtyřmístný odhad: ") # Získání vstupu od uživatele
        
        if hadani.lower() == "konec":  # Kontrola, zda uživatel zadal "konec"
            print("Hra byla ukončena. Děkujeme, že jste si zahráli!")
            break

        if len(hadani) != 4 or not hadani.isdigit() or len(set(hadani)) != 4 or hadani[0] == "0":
            print("Neplatný vstup. Zadejte čtyřmístné číslo s unikátními číslicemi, které nezačíná nulou.")
            continue

        hadani = [int(cislice) for cislice in hadani]  # Převedení na seznam čísel
        pokusy += 1
        bulls, cows = vyhodnot_hadani(hadani, kod)

        print(cara)
        print(f"Byci: {bulls}, Kravy: {cows}")
        print(cara)

        if bulls == 4:
            print(f"Gratulujeme! Uhodli jste kód {''.join(map(str, kod))} za {pokusy} pokusů.")
            break

# Spuštění hry
if __name__ == "__main__":
    hra()
    print(cara)
    print("Děkujeme, že jste si zahráli!")
    print(cara)
    print("Na shledanou!")
    print(cara)
