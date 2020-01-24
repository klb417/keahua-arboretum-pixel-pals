from animals import RiverDolphin, nenegoose, Ulae, Kikakapu, Pueo, Opeapea, HHFSpider, GDDGecko

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
        if arboretum.rivers == [] and arboretum.coastlines == []:
            print("Please go create a location for this animal.")
            input("\n\nPress any key to continue...")

        else: 
            new_list = arboretum.rivers + arboretum.coastlines
            for index, place in enumerate(new_list):
                print(f'{index + 1}. {place.name} {place.id} ({len(place.animals)} animals)')
            print("Release the animal into which biome?")
            choice = input("> ")
            selection = new_list[int(choice) - 1].id
            river = list(filter(lambda x: x.id == selection, arboretum.rivers))
            coast = list(filter(lambda x: x.id == selection, arboretum.coastlines))
            if river != []:
                river[0].add_animal(animal)
            elif coast != []: 
                coast[0].add_animal(animal)


    if choice == "2":
        animal = GDDGecko()
        if arboretum.forests == []:
            print("Please go create a location for this animal.")
        else: 
            for index, forest in enumerate(arboretum.forests):
                print(f'{index + 1}. Forest ({len(forest.animals)} animals)')
            print("Release the animal into which biome?")

            choice = input("> ")

            arboretum.forests[int(choice) - 1].animals.append(animal)




    if choice == "3":
        animal = nenegoose()
        if arboretum.grasslands == []:
            print("Please go create a location for this animal.")
        else: 
            for index, grassland in enumerate(arboretum.grasslands):
                print(f'{index + 1}. Grassland {grassland.id}')
            print("Release the animal into which biome?")

            choice = input("> ")

            arboretum.grasslands[int(choice) - 1].animals.append(animal)




    if choice == "4":
        animal = Kikakapu()
        if arboretum.rivers == [] and arboretum.swamps == []:
            print("Please go create a location for this animal.")
            input("\n\nPress any key to continue...")

        else: 
            new_list = arboretum.rivers + arboretum.swamps
            for index, place in enumerate(new_list):
                print(f'{index + 1}. {place.name} {place.id} ({len(place.animals)} animals)')
            print("Release the animal into which biome?")
            choice = input("> ")
            selection = new_list[int(choice) - 1].id
            swamp = list(filter(lambda x: x.id == selection, arboretum.swamps))
            river = list(filter(lambda x: x.id == selection, arboretum.rivers))

            if river != []:
                river[0].add_animal(animal)
            if swamp != []: 
                swamp[0].add_animal(animal)

    if choice == "5":
        animal = Pueo()
        if arboretum.grasslands == [] and arboretum.forests == []:
            print("Please go create a location for this animal.")
            input("\n\nPress any key to continue...")

        else: 
            new_list = arboretum.grasslands + arboretum.forests
            for index, place in enumerate(new_list):
                print(f'{index + 1}. {place.name} {place.id} ({len(place.animals)} animals)')
            print("Release the animal into which biome?")
            choice = input("> ")
            selection = new_list[int(choice) - 1].id
            forest = list(filter(lambda x: x.id == selection, arboretum.forests))
            grassland = list(filter(lambda x: x.id == selection, arboretum.grasslands))

            if grassland != []:
                grassland[0].add_animal(animal)
            if forest != []: 
                forest[0].add_animal(animal)



    if choice == "6":
        animal = Ulae()
        if arboretum.coastlines == []:
            print("Please go create a location for this animal.")
        else: 
            for index, coastline in enumerate(arboretum.coastlines):
                print(f'{index + 1}. Coastline {coastline.id}')
            print("Release the animal into which biome?")

            choice = input("> ")

            arboretum.coastlines[int(choice) - 1].animals.append(animal)

    if choice == "7":
        animal = Opeapea()
        if arboretum.mountains == [] and arboretum.forests == []:
            print("Please go create a location for this animal.")
            input("\n\nPress any key to continue...")

        else: 
            new_list = arboretum.mountains + arboretum.forests
            for index, place in enumerate(new_list):
                print(f'{index + 1}. {place.name} {place.id} ({len(place.animals)} animals)')
            print("Release the animal into which biome?")
            choice = input("> ")
            selection = new_list[int(choice) - 1].id
            forest = list(filter(lambda x: x.id == selection, arboretum.forests))
            mountain = list(filter(lambda x: x.id == selection, arboretum.mountains))

            if mountain != []:
                mountain[0].add_animal(animal)
            if forest != []: 
                forest[0].add_animal(animal)
        
    if choice == "8":
        animal = HHFSpider()
        if arboretum.swamps == []:
            print("Please go create a location for this animal.")
        else: 
            for index, swamp in enumerate(arboretum.swamps):
                print(f'{index + 1}. Swamp {swamp.id}')
            print("Release the animal into which biome?")

            choice = input("> ")

            arboretum.swamps[int(choice) - 1].animals.append(animal)


