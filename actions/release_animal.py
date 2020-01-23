from animals import RiverDolphin

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
                print(f'{index + 1}. River {river}')

            print("Release the animal into which biome?")
            choice = input("> ")

            arboretum.rivers[int(choice) - 1].animals.append(animal)

    if choice == "2":
        pass

    if choice == "3":
        pass

    if choice == "4":
        pass

    if choice == "5":
        pass

    if choice == "6":
        pass

    if choice == "7":
        pass

    if choice == "8":
        pass

    if arboretum.rivers == []:
        print("Please go create a location for this animal.")
    else: 
        for index, river in enumerate(arboretum.rivers):
            print(f'{index + 1}. River {river}')

        print("Release the animal into which biome?")
        choice = input("> ")

        arboretum.rivers[int(choice) - 1].animals.append(animal)


