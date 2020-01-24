from animals import RiverDolphin, nenegoose, Ulae, Kīkākapu, Pueo, Opeapea, HHFSpider, GDDGecko

def release_animal(arboretum):
    animal = None

    print("1. River Dolphin")
    print("2. Gold Dust Day Gecko")
    print("3. Nene Goose")
    print("4. Kīkākapu")
    print("5. Pueo")
    print("6. 'Ulae")
    print("7. Ope'ape'a")
    print("8. Happy-Face Spider")


    choice = input("Choose animal to release > ")

    if choice == "1":
        animal = RiverDolphin()
        if arboretum.rivers == []:
            print("Please go create a location for this animal.")
        else: 
            for index, river in enumerate(arboretum.rivers):
                print(f'{index + 1}. River ({len(river.animals)} animals)')
            print("Release the animal into which biome?")
            choice = input("> ")
            if len(arboretum.rivers[int(choice) - 1].animals) < 2:
                arboretum.rivers[int(choice) - 1].animals.append(animal)
            else:
                print("****   That biome is not large enough   ****       ****    Please choose another one      ****")
                for index, river in enumerate(arboretum.rivers):
                    print(f'{index + 1}. River ({len(river.animals)} animals)')
                choice = input("> ")
                if len(arboretum.rivers[int(choice) - 1].animals) < 2:
                    arboretum.rivers[int(choice) - 1].animals.append(animal)



    if choice == "2":
        animal == GDDGecko()
        if arboretum.forests == []:
            print("Please go create a location for this animal.")
        else: 
            for index, forest in enumerate(arboretum.forests):
                print(f'{index + 1}. Forest ({len(forest.animals)} animals)')
            print("Release the animal into which biome?")

            choice = input("> ")

            arboretum.forests[int(choice) - 1].animals.append(animal)
    if choice == "3":
        animal == nenegoose()
        if arboretum.grasslands == []:
            print("Please go create a location for this animal.")
        else: 
            for index, grassland in enumerate(arboretum.grasslands):
                print(f'{index + 1}. Grassland {grassland.id}')
            print("Release the animal into which biome?")

            choice = input("> ")

            arboretum.grasslands[int(choice) - 1].animals.append(animal)

    if choice == "4":
        animal == Kīkākapu()


    if choice == "5":
        animal == Pueo()

    if choice == "6":
        animal == Ulae()

    if choice == "7":
        animal == Opeapea()

    if choice == "8":
        animal == HHFSpider()

    # if arboretum.rivers == []:
    #     print("Please go create a location for this animal.")
    # else: 
    #     for index, river in enumerate(arboretum.rivers):
    #         print(f'{index + 1}. River {river}')

    #     print("Release the animal into which biome?")
    #     choice = input("> ")

    #     arboretum.rivers[int(choice) - 1].animals.append(animal)


