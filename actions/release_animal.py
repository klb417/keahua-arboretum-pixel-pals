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
        # clear the terminal
        os.system("cls" if os.name == "nt" else "clear")
        if arboretum.rivers == [] and arboretum.coastlines == []:
            os.system("cls" if os.name == "nt" else "clear")
            print("Uh Oh! There are no biomes for this animal to live in. Please go create a biome for this animal.")
            input("\n\nPress enter to continue...")

        else: 
            # combine the rivers and coastline lists
            new_list = arboretum.rivers + arboretum.coastlines
            for index, place in enumerate(new_list):
                print(f'{index + 1}. {place.name} ({len(place.animals)} animals)')
            print("Release the animal into which biome?")
            choice1 = input("> ")
            try:
                selection = new_list[int(choice1) - 1].id
                # search the river list for the selection
                river = list(filter(lambda x: x.id == selection, arboretum.rivers))
                # search the coast list for the selection
                coast = list(filter(lambda x: x.id == selection, arboretum.coastlines))
                if river != []:
                    # add the animal to the river that was found in the search
                    river[0].add_animal(animal)
                elif coast != []: 
                    # add the animal to the river that was found in the search
                    coast[0].add_animal(animal)
                os.system("cls" if os.name == "nt" else "clear")
                print(F'Success! The {animal.species} has been added to the biome!')
                input("\n\nPress enter to continue...")
            except: 
                release_animal(arboretum)

            # print(f"Ooops! That doesn't seem to be an option. Please select one of the menu options.")
        
            


    if choice == "2":
        os.system("cls" if os.name == "nt" else "clear")
        animal = GDDGecko()
        if arboretum.forests == []:
            os.system("cls" if os.name == "nt" else "clear")
            print("Uh Oh! There are no biomes for this animal to live in. Please go create a biome for this animal.")
            input("\n\nPress enter to continue...")
        else: 
            for index, forest in enumerate(arboretum.forests):
                print(f'{index + 1}. Forest ({len(forest.animals)} animals)')
            print("Release the animal into which biome?")

            choice2 = input("> ")

            try:
                arboretum.forests[int(choice2) - 1].add_animal(animal)
                os.system("cls" if os.name == "nt" else "clear")
                print(F'Success! The {animal.species} has been added to the biome!')
                input("\n\nPress enter to continue...")
            except: 
                release_animal(arboretum)




    if choice == "3":
        os.system("cls" if os.name == "nt" else "clear")
        animal = nenegoose()
        if arboretum.grasslands == []:
            os.system("cls" if os.name == "nt" else "clear")
            print("Uh Oh! There are no biomes for this animal to live in. Please go create a biome for this animal.")
            input("\n\nPress enter to continue...")
        else: 
            for index, grassland in enumerate(arboretum.grasslands):
                print(f'{index + 1}. Grassland ({len(grassland.animals)} animals)')
            print("Release the animal into which biome?")

            choice3 = input("> ")

            try: 
                arboretum.grasslands[int(choice3) - 1].add_animal(animal)
                os.system("cls" if os.name == "nt" else "clear")
                print(F'Success! The {animal.species} has been added to the biome!')
                input("\n\nPress enter to continue...")
            except: 
                release_animal(arboretum)




    if choice == "4":
        os.system("cls" if os.name == "nt" else "clear")
        animal = Kikakapu()
        if arboretum.rivers == [] and arboretum.swamps == []:
            os.system("cls" if os.name == "nt" else "clear")
            print("Uh Oh! There are no biomes for this animal to live in. Please go create a biome for this animal.")
            input("\n\nPress enter to continue...")

        else: 
            new_list = arboretum.rivers + arboretum.swamps
            for index, place in enumerate(new_list):
                print(f'{index + 1}. {place.name} ({len(place.animals)} animals)')
            print("Release the animal into which biome?")
            choice4 = input("> ")
            try: 
                selection = new_list[int(choice4) - 1].id
                swamp = list(filter(lambda x: x.id == selection, arboretum.swamps))
                river = list(filter(lambda x: x.id == selection, arboretum.rivers))

                if river != []:
                    river[0].add_animal(animal)
                if swamp != []: 
                    swamp[0].add_animal(animal)
                os.system("cls" if os.name == "nt" else "clear")
                print(F'Success! The {animal.species} has been added to the biome!')
                input("\n\nPress enter to continue...")
            except: 
                release_animal(arboretum)


    if choice == "5":
        os.system("cls" if os.name == "nt" else "clear")
        animal = Pueo()
        if arboretum.grasslands == [] and arboretum.forests == []:
            os.system("cls" if os.name == "nt" else "clear")
            print("Uh Oh! There are no biomes for this animal to live in. Please go create a biome for this animal.")
            input("\n\nPress enter to continue...")

        else: 
            new_list = arboretum.grasslands + arboretum.forests
            for index, place in enumerate(new_list):
                print(f'{index + 1}. {place.name} ({len(place.animals)} animals)')
            print("Release the animal into which biome?")
            choice5 = input("> ")
            try: 
                selection = new_list[int(choice5) - 1].id
                forest = list(filter(lambda x: x.id == selection, arboretum.forests))
                grassland = list(filter(lambda x: x.id == selection, arboretum.grasslands))

                if grassland != []:
                    grassland[0].add_animal(animal)
                if forest != []: 
                    forest[0].add_animal(animal)
                os.system("cls" if os.name == "nt" else "clear")
                print(F'Success! The {animal.species} has been added to the biome!')
                input("\n\nPress enter to continue...")
            except: 
                release_animal(arboretum)



    if choice == "6":
        os.system("cls" if os.name == "nt" else "clear")
        animal = Ulae()
        if arboretum.coastlines == []:
            os.system("cls" if os.name == "nt" else "clear")
            print("Uh Oh! There are no biomes for this animal to live in. Please go create a biome for this animal.")
            input("\n\nPress enter to continue...")
        else: 
            for index, coastline in enumerate(arboretum.coastlines):
                print(f'{index + 1}. Coastline ({len(coastline.animals)} animals)')
            print("Release the animal into which biome?")

            choice6 = input("> ")
            try: 
                arboretum.coastlines[int(choice6) - 1].add_animal(animal)
                os.system("cls" if os.name == "nt" else "clear")
                print(F'Success! The {animal.species} has been added to the biome!')
                input("\n\nPress enter to continue...")
            except: 
                release_animal(arboretum)


    if choice == "7":
        os.system("cls" if os.name == "nt" else "clear")
        animal = Opeapea()
        if arboretum.mountains == [] and arboretum.forests == []:
            os.system("cls" if os.name == "nt" else "clear")
            print("Uh Oh! There are no biomes for this animal to live in. Please go create a biome for this animal.")
            input("\n\nPress enter to continue...")

        else: 
            new_list = arboretum.mountains + arboretum.forests
            for index, place in enumerate(new_list):
                print(f'{index + 1}. {place.name} ({len(place.animals)} animals)')
            print("Release the animal into which biome?")
            choice7 = input("> ")
            try: 
                selection = new_list[int(choice7) - 1].id
                forest = list(filter(lambda x: x.id == selection, arboretum.forests))
                mountain = list(filter(lambda x: x.id == selection, arboretum.mountains))

                if mountain != []:
                    mountain[0].add_animal(animal)
                if forest != []: 
                    forest[0].add_animal(animal)
                os.system("cls" if os.name == "nt" else "clear")
                print(F'Success! The {animal.species} has been added to the biome!')
                input("\n\nPress enter to continue...")
            except: 
                release_animal(arboretum)


    if choice == "8":
        os.system("cls" if os.name == "nt" else "clear")
        animal = HHFSpider()
        if arboretum.swamps == []:
            os.system("cls" if os.name == "nt" else "clear")
            print("Uh Oh! There are no biomes for this animal to live in. Please go create a biome for this animal.")
            input("\n\nPress enter to continue...")
        else: 
            for index, swamp in enumerate(arboretum.swamps):
                print(f'{index + 1}. Swamp ({len(swamp.animals)} animals)')
            print("Release the animal into which biome?")

            choice8 = input("> ")
            try:
                arboretum.swamps[int(choice8) - 1].add_animal(animal)
                os.system("cls" if os.name == "nt" else "clear")
                print(F'Success! The {animal.species} has been added to the biome!')
                input("\n\nPress enter to continue...")
            except: 
                release_animal(arboretum)


