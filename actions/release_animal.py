from animals import RiverDolphin, nenegoose, Ulae, Kikakapu, Pueo, Opeapea, HHFSpider, GDDGecko
import os
def release_animal(arboretum):
    animal = None
    os.system("cls" if os.name == "nt" else "clear")


    print("1. River Dolphin")
    print("2. Gold Dust Day Gecko")
    print("3. Nene Goose")
    print("4. Kikakapu")
    print("5. Pueo")
    print("6. 'Ulae")
    print("7. Ope'ape'a")
    print("8. Happy-Face Spider")


    choice = input("Choose animal to release > ")

    if choice == "1":
        animal = RiverDolphin()
        def release_dolphin():
            os.system("cls" if os.name == "nt" else "clear")
            if arboretum.rivers == [] and arboretum.coastlines == []:
                os.system("cls" if os.name == "nt" else "clear")
                print("Uh Oh! There are no biomes for this animal to live in. Please go create a biome for this animal.")
                input("\n\nPress any key to continue...")

            else: 
                new_list = arboretum.rivers + arboretum.coastlines
                for index, place in enumerate(new_list):
                    print(f'{index + 1}. {place.name} ({len(place.animals)} animals)')
                print("Release the animal into which biome?")
                choice = input("> ")
                selection = new_list[int(choice) - 1].id
                river = list(filter(lambda x: x.id == selection, arboretum.rivers))
                coast = list(filter(lambda x: x.id == selection, arboretum.coastlines))
                if river != []:
                    river[0].add_animal(animal)
                elif coast != []: 
                    coast[0].add_animal(animal)
                os.system("cls" if os.name == "nt" else "clear")
                print(F'Success! The {animal.species} has been added to the biome!')
                input("\n\nPress any key to continue...")
        try:
            release_dolphin()
        except:
            os.system("cls" if os.name == "nt" else "clear")
            print(f"Ooops! That doesn't seem to be an option. Please select one of the menu options.")
            release_dolphin()
            


    if choice == "2":
        os.system("cls" if os.name == "nt" else "clear")
        animal = GDDGecko()
        if arboretum.forests == []:
            os.system("cls" if os.name == "nt" else "clear")
            print("Uh Oh! There are no biomes for this animal to live in. Please go create a biome for this animal.")
            input("\n\nPress any key to continue...")
        else: 
            for index, forest in enumerate(arboretum.forests):
                print(f'{index + 1}. Forest ({len(forest.animals)} animals)')
            print("Release the animal into which biome?")

            choice = input("> ")

            arboretum.forests[int(choice) - 1].animals.append(animal)
            os.system("cls" if os.name == "nt" else "clear")
            print(F'Success! The {animal.species} has been added to the biome!')
            input("\n\nPress any key to continue...")



    if choice == "3":
        os.system("cls" if os.name == "nt" else "clear")
        animal = nenegoose()
        if arboretum.grasslands == []:
            os.system("cls" if os.name == "nt" else "clear")
            print("Uh Oh! There are no biomes for this animal to live in. Please go create a biome for this animal.")
            input("\n\nPress any key to continue...")
        else: 
            for index, grassland in enumerate(arboretum.grasslands):
                print(f'{index + 1}. Grassland ({len(grassland.animals)} animals)')
            print("Release the animal into which biome?")

            choice = input("> ")

            arboretum.grasslands[int(choice) - 1].animals.append(animal)
            os.system("cls" if os.name == "nt" else "clear")
            print(F'Success! The {animal.species} has been added to the biome!')
            input("\n\nPress any key to continue...")



    if choice == "4":
        os.system("cls" if os.name == "nt" else "clear")
        animal = Kikakapu()
        if arboretum.rivers == [] and arboretum.swamps == []:
            os.system("cls" if os.name == "nt" else "clear")
            print("Uh Oh! There are no biomes for this animal to live in. Please go create a biome for this animal.")
            input("\n\nPress any key to continue...")

        else: 
            new_list = arboretum.rivers + arboretum.swamps
            for index, place in enumerate(new_list):
                print(f'{index + 1}. {place.name} ({len(place.animals)} animals)')
            print("Release the animal into which biome?")
            choice = input("> ")
            selection = new_list[int(choice) - 1].id
            swamp = list(filter(lambda x: x.id == selection, arboretum.swamps))
            river = list(filter(lambda x: x.id == selection, arboretum.rivers))

            if river != []:
                river[0].add_animal(animal)
            if swamp != []: 
                swamp[0].add_animal(animal)
            os.system("cls" if os.name == "nt" else "clear")
            print(F'Success! The {animal.species} has been added to the biome!')
            input("\n\nPress any key to continue...")

    if choice == "5":
        os.system("cls" if os.name == "nt" else "clear")
        animal = Pueo()
        if arboretum.grasslands == [] and arboretum.forests == []:
            os.system("cls" if os.name == "nt" else "clear")
            print("Uh Oh! There are no biomes for this animal to live in. Please go create a biome for this animal.")
            input("\n\nPress any key to continue...")

        else: 
            new_list = arboretum.grasslands + arboretum.forests
            for index, place in enumerate(new_list):
                print(f'{index + 1}. {place.name} ({len(place.animals)} animals)')
            print("Release the animal into which biome?")
            choice = input("> ")
            selection = new_list[int(choice) - 1].id
            forest = list(filter(lambda x: x.id == selection, arboretum.forests))
            grassland = list(filter(lambda x: x.id == selection, arboretum.grasslands))

            if grassland != []:
                grassland[0].add_animal(animal)
            if forest != []: 
                forest[0].add_animal(animal)
            os.system("cls" if os.name == "nt" else "clear")
            print(F'Success! The {animal.species} has been added to the biome!')
            input("\n\nPress any key to continue...")


    if choice == "6":
        os.system("cls" if os.name == "nt" else "clear")
        animal = Ulae()
        if arboretum.coastlines == []:
            os.system("cls" if os.name == "nt" else "clear")
            print("Uh Oh! There are no biomes for this animal to live in. Please go create a biome for this animal.")
            input("\n\nPress any key to continue...")
        else: 
            for index, coastline in enumerate(arboretum.coastlines):
                print(f'{index + 1}. Coastline ({len(coastline.animals)} animals)')
            print("Release the animal into which biome?")

            choice = input("> ")

            arboretum.coastlines[int(choice) - 1].animals.append(animal)
            os.system("cls" if os.name == "nt" else "clear")
            print(F'Success! The {animal.species} has been added to the biome!')
            input("\n\nPress any key to continue...")

    if choice == "7":
        os.system("cls" if os.name == "nt" else "clear")
        animal = Opeapea()
        if arboretum.mountains == [] and arboretum.forests == []:
            os.system("cls" if os.name == "nt" else "clear")
            print("Uh Oh! There are no biomes for this animal to live in. Please go create a biome for this animal.")
            input("\n\nPress any key to continue...")

        else: 
            new_list = arboretum.mountains + arboretum.forests
            for index, place in enumerate(new_list):
                print(f'{index + 1}. {place.name} ({len(place.animals)} animals)')
            print("Release the animal into which biome?")
            choice = input("> ")
            selection = new_list[int(choice) - 1].id
            forest = list(filter(lambda x: x.id == selection, arboretum.forests))
            mountain = list(filter(lambda x: x.id == selection, arboretum.mountains))

            if mountain != []:
                mountain[0].add_animal(animal)
            if forest != []: 
                forest[0].add_animal(animal)
            os.system("cls" if os.name == "nt" else "clear")
            print(F'Success! The {animal.species} has been added to the biome!')
            input("\n\nPress any key to continue...")

    if choice == "8":
        os.system("cls" if os.name == "nt" else "clear")
        animal = HHFSpider()
        if arboretum.swamps == []:
            os.system("cls" if os.name == "nt" else "clear")
            print("Uh Oh! There are no biomes for this animal to live in. Please go create a biome for this animal.")
            input("\n\nPress any key to continue...")
        else: 
            for index, swamp in enumerate(arboretum.swamps):
                print(f'{index + 1}. Swamp ({len(swamp.animals)} animals)')
            print("Release the animal into which biome?")

            choice = input("> ")

            arboretum.swamps[int(choice) - 1].animals.append(animal)
            os.system("cls" if os.name == "nt" else "clear")
            print(F'Success! The {animal.species} has been added to the biome!')
            input("\n\nPress any key to continue...")

