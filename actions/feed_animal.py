import os
from animals import RiverDolphin, GDDGecko, HHFSpider, Kikakapu, nenegoose, Opeapea, Pueo, Ulae
# def feeding_animals(animal):
#     os.system('cls' if os.name == 'nt' else 'clear')
#     for index, prey in enumerate(animal.prey):
#         print(f"{index + 1}. {prey}")
#     print(f"What is on the menu for the {animal.species} today? >")
#     choice = input("> ")



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

    print("Choose animal to feed.")
    choice = input("> ")

    if choice == "1":
        g_d_d_gecko = GDDGecko()
        gddgprey = tuple(g_d_d_gecko.prey)
        for index, prey in enumerate(gddgprey):
            print(f"{index + 1}. {prey}")
        print(f"What is on the menu for the Gold Dust Day Gecko today?")
        choice = input("> ")

        # print(choice, index, gddgprey)

        g_d_d_gecko.feed(gddgprey[int(choice) - 1])
    if choice == "2":
        river_dolphin = RiverDolphin()
        rvrdolprey = tuple(river_dolphin.prey)
        for index, prey in enumerate(rvrdolprey):
            print(f"{index + 1}. {prey}")
        print(f"What is on the menu for the River Dolphin today?")
        choice = input("> ")

        river_dolphin.feed(rvrdolprey[int(choice) - 1])
    if choice == "3":
        nene_goose = nenegoose()
        neneprey = tuple(nene_goose.prey)
        for index, prey in enumerate(neneprey):
            print(f"{index + 1}. {prey}")
        print(f"What is on the menu for the Nene Goose today?")
        choice = input("> ")

        nene_goose.feed(neneprey[int(choice) - 1])
    if choice == "4":
        kikakapu = Kikakapu()
        kikaprey = tuple(kikakapu.prey)
        for index, prey in enumerate(kikaprey):
            print(f"{index + 1}. {prey}")
        print(f"What is on the menu for the Kikakapu today?")
        choice = input("> ")

        kikakapu.feed(kikaprey[int(choice) - 1])
    if choice == "5":
        pueo = Pueo()
        pueoprey = tuple(pueo.prey)
        for index, prey in enumerate(pueoprey):
            print(f"{index + 1}. {prey}")
        print(f"What is on the menu for the Pueo today?")
        choice = input("> ")

        pueo.feed(pueoprey[int(choice) - 1])
    if choice == "6":
        ulae = Ulae()
        ulaeprey = tuple(ulae.prey)
        for index, prey in enumerate(ulaeprey):
            print(f"{index + 1}. {prey}")
        print(f"What is on the menu for the 'Ulae today?")
        choice = input("> ")

        ulae.feed(ulaeprey[int(choice) - 1])
    if choice == "7":
        opeapea = Opeapea()
        opeprey = tuple(opeapea.prey)
        for index, prey in enumerate(opeprey):
            print(f"{index + 1}. {prey}")
        print(f"What is on the menu for the Ope'ape'a today?")
        choice = input("> ")

        opeapea.feed(opeprey[int(choice) - 1])
    if choice == "8":
        hhfspider = HHFSpider()
        hhfsprey = tuple(hhfspider.prey)
        for index, prey in enumerate(hhfsprey):
            print(f"{index + 1}. {prey}")
        print(f"What is on the menu for the Happy-Face Spider today?")
        choice = input("> ")

        hhfspider.feed(hhfsprey[int(choice) - 1])

