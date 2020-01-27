# Author: Lauren Riddle
# Purpose: Holds the logic that creates a new animal and adds it to a biome
from animals import RiverDolphin, nenegoose, Ulae, Kikakapu, Pueo, Opeapea, HHFSpider, GDDGecko
import os
def release_animal(arboretum):
    animal = None
    # clears the screen
    os.system("cls" if os.name == "nt" else "clear")

    # creates the add animal menu
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
            # clear the screen and print an error
            os.system("cls" if os.name == "nt" else "clear")
            print("Uh Oh! There are no biomes for this animal to live in. Please go create a biome for this animal.")
            input("\n\nPress enter to continue...")

        else: 

            # combine the rivers and coastline lists
            new_list = []
            for river in arboretum.rivers:
                # add the river to the list if it has less than 12 animals in it
                if len(river.animals) < 12:
                    new_list.append(river)
            for coast in arboretum.coastlines:
                # add the coastline to the list if it has less than 15 animals in it
                if len(coast.animals) < 15:
                    new_list.append(coast)

            if new_list != []:
            # loop over list and display in terminal
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
                        # clear screen and print success message
                    os.system("cls" if os.name == "nt" else "clear")
                    print(F'Success! The {animal.species} has been added to the biome!')
                    input("\n\nPress enter to continue...")
                except: 
                    # re-load the release animal function if the user enters a choice that is not on the list
                    release_animal(arboretum)
            else:
                # print this if there are biomes created but they are all full
                print("Uh-oh! It looks like all of the biomes are full! Please go create a new Biome for this animal to live in.")
                input("\n\nPress enter to continue...")

            


    if choice == "2":
        os.system("cls" if os.name == "nt" else "clear")
        animal = GDDGecko()
        if arboretum.forests == []:
            # clear the screen and print an error
            os.system("cls" if os.name == "nt" else "clear")
            print("Uh Oh! There are no biomes for this animal to live in. Please go create a biome for this animal.")
            input("\n\nPress enter to continue...")
        else: 
            gecko_habitats = list()
            for forest in arboretum.forests:
                if len(forest.animals) < 20:
                    gecko_habitats.append(forest)
            if gecko_habitats != []:
                # loop over the biomes and display them in terminal
                for index, forest in enumerate(gecko_habitats):
                    print(f'{index + 1}. Forest ({len(forest.animals)} animals)')
                print("Release the animal into which biome?")

                choice2 = input("> ")

                try:
                    selection = gecko_habitats[int(choice2) - 1].id
                    # append the animal to the biome list
                    forest = list(filter(lambda x: x.id == selection, arboretum.forests))

                    forest[0].add_animal(animal)
                    # clear screen and print success message
                    os.system("cls" if os.name == "nt" else "clear")
                    print(F'Success! The {animal.species} has been added to the biome!')
                    input("\n\nPress enter to continue...")
                except: 
                    release_animal(arboretum)
            else: 
                # print this if there are biomes created but they are all full
                print("Uh-oh! It looks like all of the biomes are full! Please go create a new Biome for this animal to live in.")
                input("\n\nPress enter to continue...")




    if choice == "3":
        os.system("cls" if os.name == "nt" else "clear")
        animal = nenegoose()
        if arboretum.grasslands == []:
            # clear the screen and print an error
            os.system("cls" if os.name == "nt" else "clear")
            print("Uh Oh! There are no biomes for this animal to live in. Please go create a biome for this animal.")
            input("\n\nPress enter to continue...")
        else: 
            nenegoose_habitats = list()
            for land in arboretum.grasslands:
                if len(land.animals) < 22:
                    nenegoose_habitats.append(land)
            if nenegoose_habitats != []:
                # loop over the biomes and display them in terminal
                for index, grassland in enumerate(nenegoose_habitats):
                    print(f'{index + 1}. Grassland ({len(grassland.animals)} animals)')
                print("Release the animal into which biome?")

                choice3 = input("> ")

                try: 
                    selection = nenegoose_habitats[int(choice3) - 1].id
                    # append the animal to the biome list
                    land = list(filter(lambda x: x.id == selection, arboretum.grasslands))

                    land[0].add_animal(animal)
                    # append the animal to the biome list
                    arboretum.grasslands[int(choice3) - 1].add_animal(animal)
                    # clear screen and print success message
                    os.system("cls" if os.name == "nt" else "clear")
                    print(F'Success! The {animal.species} has been added to the biome!')
                    input("\n\nPress enter to continue...")
                except: 
                    release_animal(arboretum)
            else: 
                # print this if there are biomes created but they are all full
                print("Uh-oh! It looks like all of the biomes are full! Please go create a new Biome for this animal to live in.")
                input("\n\nPress enter to continue...")




    if choice == "4":
        os.system("cls" if os.name == "nt" else "clear")
        animal = Kikakapu()
        if arboretum.rivers == [] and arboretum.swamps == []:
            os.system("cls" if os.name == "nt" else "clear")
            print("Uh Oh! There are no biomes for this animal to live in. Please go create a biome for this animal.")
            input("\n\nPress enter to continue...")

        else: 
            Kikakapu_habitats = list()
            for river in arboretum.rivers:
                if len(river.animals) < 2:
                    Kikakapu_habitats.append(river)
            for swamp in arboretum.swamps:
                if len(swamp.animals) < 2:
                    Kikakapu_habitats.append(swamp)
            if Kikakapu_habitats != []:
                for index, place in enumerate(Kikakapu_habitats):
                    print(f'{index + 1}. {place.name} ({len(place.animals)} animals)')
                print("Release the animal into which biome?")
                choice4 = input("> ")
                try: 
                    selection = Kikakapu_habitats[int(choice4) - 1].id
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
            else: 
                # print this if there are biomes created but they are all full
                print("Uh-oh! It looks like all of the biomes are full! Please go create a new Biome for this animal to live in.")
                input("\n\nPress enter to continue...")


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


