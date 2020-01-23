import os
from river_dolphin import RiverDolphin

def feeding_animals(animal):
    os.system('cls' if os.name == 'nt' else 'clear')
    for index, prey in enumerate(animal.__prey, 1):
        print(f"{index}. {prey}")
    choice = input(f"What is on the menu for the {animal.name} today? >")
    if choice == f"{index}":
        animal.feed(prey)

def feed_animal():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("1. Gold Dust Day Gecko")
    print("2. River Dolphin")
    print("3. Nene Goose")
    print("4. Kikakapu")
    print("5. Pueo")
    print("6. 'Ulae")
    print("7. Ope'ape'a")
    print("8. Happy-Face Spider")

    choice = input("Choose animal to feed. >")

    if choice == "1":
        g_d_d_gecko = Gold_Dust_Day_Gecko()
        pass
    if choice == "2":
        river_dolphin = RiverDolphin()
        feeding_animals(river_dolphin)
    if choice == "3":
        nene_goose = Nene_Goose()
        pass
    if choice == "4":
        kikakapu = Kikakapu()
        pass
    if choice == "5":
        pueo = Pueo()
        pass
    if choice == "6":
        ulae = Ulae()
        pass
    if choice == "7":
        opeapea = Opeapea()
        pass
    if choice == "8":
        hhfspider = Happy_Face_Spider()
        pass


feed_animal()