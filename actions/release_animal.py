# Author: Lauren Riddle
# Purpose: Holds the logic that creates a new animal and adds it to a biome
from animals import RiverDolphin, nenegoose, Ulae, Kikakapu, Pueo, Opeapea, HHFSpider, GDDGecko
import os
def release_animal(arboretum):
    animal = None
    # clears the screen
    os.system("cls" if os.name == "nt" else "clear")

    # Printing the header
    print( ''' +-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-+
 |  K  e  a  h  u  a    A  r  b  o  r  e  t  u  m  |
 +-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-+\n''')

    # creates the add animal menu
    print("1. River Dolphin")
    print("2. Gold Dust Day Gecko")
    print("3. Nene Goose")
    print("4. Kikakapu")
    print("5. Pueo")
    print("6. 'Ulae")
    print("7. Ope'ape'a")
    print("8. Happy-Face Spider")


    # Capturing user input and assigning it to "choice" variable
    choice = input('''
Choose an animal to release or
Type M to return to the main menu.

> ''')

    if choice == "1":
        animal = RiverDolphin()
        # clear the terminal
        os.system("cls" if os.name == "nt" else "clear")
        if arboretum.rivers == [] and arboretum.coastlines == []:
            # clear the screen and print an error
            os.system("cls" if os.name == "nt" else "clear")
            # Printing the header
            print( ''' +-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-+
 |  K  e  a  h  u  a    A  r  b  o  r  e  t  u  m  |
 +-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-+\n''')
            print("Uh Oh! There are no biomes for this animal to live in. Please go create a biome for this animal.")
            input("\n\nPress enter to continue...")

        else: 

            # combine the rivers and coastline lists
            new_list = []
            for river in arboretum.rivers:
                # add the river to the list if it has less than 12 animals in it
                if river.is_animals_full() == False:
                    new_list.append(river)
            for coast in arboretum.coastlines:
                # add the coastline to the list if it has less than 15 animals in it
                if coast.is_animals_full() == False:
                    new_list.append(coast)

            if new_list != []:
            # loop over list and display in terminal
                # Printing the header
                print( ''' +-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-+
 |  K  e  a  h  u  a    A  r  b  o  r  e  t  u  m  |
 +-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-+\n''')
                for index, place in enumerate(new_list):
                    print(f'{index + 1}. {place.name} ({place.current_animals} animals)')
                print("\nRelease the animal into which habitat?\n")
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
                    # Printing the header
                    print( ''' +-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-+
 |  K  e  a  h  u  a    A  r  b  o  r  e  t  u  m  |
 +-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-+\n''')
                    print(F'Success! The {animal.species} has been added to the biome!')
                    input("\n\nPress enter to continue...")
                except: 
                    # re-load the release animal function if the user enters a choice that is not on the list
                    release_animal(arboretum)
            else:
                # print this if there are biomes created but they are all full
                print("Uh-oh! It looks like all of the biomes are full! Please go create a new Habitat for this animal to live in.")
                input("\n\nPress enter to continue...")

            


    if choice == "2":
        os.system("cls" if os.name == "nt" else "clear")
        animal = GDDGecko()
        if arboretum.forests == []:
            # clear the screen and print an error
            os.system("cls" if os.name == "nt" else "clear")
            # Printing the header
            print( ''' +-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-+
 |  K  e  a  h  u  a    A  r  b  o  r  e  t  u  m  |
 +-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-+\n''')
            print("Uh Oh! There are no biomes for this animal to live in. Please go create a biome for this animal.")
            input("\n\nPress enter to continue...")
        else: 
            gecko_habitats = list()
            for forest in arboretum.forests:
                # if the biome has less than 20 animal in it, add it to the list
                if forest.is_animals_full() == False:
                    gecko_habitats.append(forest)
            if gecko_habitats != []:
                # loop over the biomes and display them in terminal
                # Printing the header
                print( ''' +-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-+
 |  K  e  a  h  u  a    A  r  b  o  r  e  t  u  m  |
 +-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-+\n''')
                for index, forest in enumerate(gecko_habitats):
                    print(f'{index + 1}. Forest ({forest.current_animals} animals)')
                print("\nRelease the animal into which habitat?\n")

                choice2 = input("> ")

                try:
                    # capture the selection 
                    selection = gecko_habitats[int(choice2) - 1].id
                    # filter the aboretum.forest list for the selection
                    forest = list(filter(lambda x: x.id == selection, arboretum.forests))
                    # append the animal to the biome list

                    forest[0].add_animal(animal)
                    # clear screen and print success message
                    os.system("cls" if os.name == "nt" else "clear")
                    # Printing the header
                    print( ''' +-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-+
 |  K  e  a  h  u  a    A  r  b  o  r  e  t  u  m  |
 +-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-+\n''')
                    print(F'Success! The {animal.species} has been added to the biome!')
                    input("\n\nPress enter to continue...")
                except: 
                    release_animal(arboretum)
            else: 
                # print this if there are biomes created but they are all full
                print("Uh-oh! It looks like all of the biomes are full! Please go create a new Habitat for this animal to live in.")
                input("\n\nPress enter to continue...")




    if choice == "3":
        os.system("cls" if os.name == "nt" else "clear")
        animal = nenegoose()
        if arboretum.grasslands == []:
            # clear the screen and print an error
            os.system("cls" if os.name == "nt" else "clear")
            # Printing the header
            print( ''' +-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-+
 |  K  e  a  h  u  a    A  r  b  o  r  e  t  u  m  |
 +-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-+\n''')
            print("Uh Oh! There are no biomes for this animal to live in. Please go create a biome for this animal.")
            input("\n\nPress enter to continue...")
        else: 
            nenegoose_habitats = list()
            for land in arboretum.grasslands:
                if land.is_animals_full() == False:
                    nenegoose_habitats.append(land)
            if nenegoose_habitats != []:
                # loop over the biomes and display them in terminal
                # Printing the header
                print( ''' +-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-+
 |  K  e  a  h  u  a    A  r  b  o  r  e  t  u  m  |
 +-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-+\n''')
                for index, grassland in enumerate(nenegoose_habitats):
                    print(f'{index + 1}. Grassland ({grassland.current_animals} animals)')
                print("\nRelease the animal into which habitat?\n")

                choice3 = input("> ")

                try: 
                    selection = nenegoose_habitats[int(choice3) - 1].id
                    # append the animal to the biome list
                    land = list(filter(lambda x: x.id == selection, arboretum.grasslands))

                    # append the animal to the biome list
                    land[0].add_animal(animal)
                    # clear screen and print success message
                    os.system("cls" if os.name == "nt" else "clear")
                    # Printing the header
                    print( ''' +-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-+
 |  K  e  a  h  u  a    A  r  b  o  r  e  t  u  m  |
 +-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-+\n''')
                    print(F'Success! The {animal.species} has been added to the habitat!')
                    input("\n\nPress enter to continue...")
                except: 
                    release_animal(arboretum)
            else: 
                # print this if there are biomes created but they are all full
                print("Uh-oh! It looks like all of the biomes are full! Please go create a new Habitat for this animal to live in.")
                input("\n\nPress enter to continue...")




    if choice == "4":
        os.system("cls" if os.name == "nt" else "clear")
        animal = Kikakapu()
        if arboretum.rivers == [] and arboretum.swamps == []:
            os.system("cls" if os.name == "nt" else "clear")
            # Printing the header
            print( ''' +-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-+
 |  K  e  a  h  u  a    A  r  b  o  r  e  t  u  m  |
 +-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-+\n''')
            print("Uh Oh! There are no biomes for this animal to live in. Please go create a biome for this animal.")
            input("\n\nPress enter to continue...")

        else: 
            Kikakapu_habitats = list()
            for river in arboretum.rivers:
                if river.is_animals_full() == False:
                    Kikakapu_habitats.append(river)
            for swamp in arboretum.swamps:
                if swamp.is_animals_full() == False:
                    Kikakapu_habitats.append(swamp)
            if Kikakapu_habitats != []:
                # Printing the header
                print( ''' +-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-+
 |  K  e  a  h  u  a    A  r  b  o  r  e  t  u  m  |
 +-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-+\n''')
                for index, place in enumerate(Kikakapu_habitats):
                    print(f'{index + 1}. {place.name} ({place.current_animals} animals)')
                print("\nRelease the animal into which habitat?\n")
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
                    # Printing the header
                    print( ''' +-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-+
 |  K  e  a  h  u  a    A  r  b  o  r  e  t  u  m  |
 +-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-+\n''')
                    print(F'Success! The {animal.species} has been added to the biome!')
                    input("\n\nPress enter to continue...")
                except: 
                    release_animal(arboretum)
            else: 
                # print this if there are biomes created but they are all full
                print("Uh-oh! It looks like all of the biomes are full! Please go create a new Habitat for this animal to live in.")
                input("\n\nPress enter to continue...")


    if choice == "5":
        os.system("cls" if os.name == "nt" else "clear")
        animal = Pueo()
        if arboretum.grasslands == [] and arboretum.forests == []:
            os.system("cls" if os.name == "nt" else "clear")
            # Printing the header
            print( ''' +-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-+
 |  K  e  a  h  u  a    A  r  b  o  r  e  t  u  m  |
 +-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-+\n''')
            print("Uh Oh! There are no biomes for this animal to live in. Please go create a biome for this animal.")
            input("\n\nPress enter to continue...")

        else: 
            pueo_habitats = list()
            for land in arboretum.grasslands:
                if land.is_animals_full() == False:
                    pueo_habitats.append(land)
            for forest in arboretum.forests:
                if forest.is_animals_full() == False:
                    pueo_habitats.append(forest)
            if pueo_habitats != []:
                # Printing the header
                print( ''' +-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-+
 |  K  e  a  h  u  a    A  r  b  o  r  e  t  u  m  |
 +-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-+\n''')
                for index, place in enumerate(pueo_habitats):
                    print(f'{index + 1}. {place.name} ({place.current_animals} animals)')
                print("\nRelease the animal into which habitat?\n")
                choice5 = input("> ")
                try: 
                    selection = pueo_habitats[int(choice5) - 1].id
                    forest = list(filter(lambda x: x.id == selection, arboretum.forests))
                    grassland = list(filter(lambda x: x.id == selection, arboretum.grasslands))

                    if grassland != []:
                        grassland[0].add_animal(animal)
                    if forest != []: 
                        forest[0].add_animal(animal)
                    os.system("cls" if os.name == "nt" else "clear")
                    # Printing the header
                    print( ''' +-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-+
 |  K  e  a  h  u  a    A  r  b  o  r  e  t  u  m  |
 +-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-+\n''')
                    print(F'Success! The {animal.species} has been added to the biome!')
                    input("\n\nPress enter to continue...")
                except: 
                    release_animal(arboretum)
            else: 
                # print this if there are biomes created but they are all full
                print("Uh-oh! It looks like all of the biomes are full! Please go create a new Habitat for this animal to live in.")
                input("\n\nPress enter to continue...")


    if choice == "6":
        os.system("cls" if os.name == "nt" else "clear")
        animal = Ulae()
        if arboretum.coastlines == []:
            os.system("cls" if os.name == "nt" else "clear")
            # Printing the header
            print( ''' +-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-+
 |  K  e  a  h  u  a    A  r  b  o  r  e  t  u  m  |
 +-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-+\n''')
            print("Uh Oh! There are no biomes for this animal to live in. Please go create a biome for this animal.")
            input("\n\nPress enter to continue...")
        else: 
            ulae_habitats = list()
            for coast in arboretum.coastlines:
                if coast.is_animals_full() == False:
                    ulae_habitats.append(coast)
            if ulae_habitats != []:
                # Printing the header
                print( ''' +-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-+
 |  K  e  a  h  u  a    A  r  b  o  r  e  t  u  m  |
 +-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-+\n''')
                for index, coastline in enumerate(ulae_habitats):
                    print(f'{index + 1}. Coastline ({coastline.current_animals} animals)')
                print("\nRelease the animal into which habitat?\n")

                choice6 = input("> ")
                try: 
                    selection = ulae_habitats[int(choice6) - 1].id
                    # append the animal to the biome list
                    coast = list(filter(lambda x: x.id == selection, arboretum.coastlines))

                    coast[0].add_animal(animal)
                    os.system("cls" if os.name == "nt" else "clear")
                    # Printing the header
                    print( ''' +-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-+
 |  K  e  a  h  u  a    A  r  b  o  r  e  t  u  m  |
 +-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-+\n''')
                    print(F'Success! The {animal.species} has been added to the biome!')
                    input("\n\nPress enter to continue...")
                except: 
                    release_animal(arboretum)
            else: 
                # print this if there are biomes created but they are all full
                print("Uh-oh! It looks like all of the biomes are full! Please go create a new Habitat for this animal to live in.")
                input("\n\nPress enter to continue...")

    if choice == "7":
        os.system("cls" if os.name == "nt" else "clear")
        animal = Opeapea()
        if arboretum.mountains == [] and arboretum.forests == []:
            os.system("cls" if os.name == "nt" else "clear")
            # Printing the header
            print( ''' +-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-+
 |  K  e  a  h  u  a    A  r  b  o  r  e  t  u  m  |
 +-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-+\n''')
            print("Uh Oh! There are no biomes for this animal to live in. Please go create a biome for this animal.")
            input("\n\nPress enter to continue...")

        else: 
            Opeapea_habitats = list()
            for mountain in arboretum.mountains:
                if mountain.is_animals_full() == False:
                    Opeapea_habitats.append(mountain)
            for forest in arboretum.forests:
                if forest.is_animals_full() == False:
                    Opeapea_habitats.append(forest)
            if Opeapea_habitats != []:
                # Printing the header
                print( ''' +-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-+
 |  K  e  a  h  u  a    A  r  b  o  r  e  t  u  m  |
 +-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-+\n''')
                for index, place in enumerate(Opeapea_habitats):
                    print(f'{index + 1}. {place.name} ({place.current_animals} animals)')
                print("\nRelease the animal into which habitat?\n")
                choice7 = input("> ")
                try: 
                    selection = Opeapea_habitats[int(choice7) - 1].id
                    forest = list(filter(lambda x: x.id == selection, arboretum.forests))
                    mountain = list(filter(lambda x: x.id == selection, arboretum.mountains))

                    if mountain != []:
                        mountain[0].add_animal(animal)
                    if forest != []: 
                        forest[0].add_animal(animal)
                    os.system("cls" if os.name == "nt" else "clear")
                    # Printing the header
                    print( ''' +-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-+
 |  K  e  a  h  u  a    A  r  b  o  r  e  t  u  m  |
 +-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-+\n''')
                    print(F'Success! The {animal.species} has been added to the biome!')
                    input("\n\nPress enter to continue...")
                except: 
                    release_animal(arboretum)
            else: 
                # print this if there are biomes created but they are all full
                print("Uh-oh! It looks like all of the biomes are full! Please go create a new Habitat for this animal to live in.")
                input("\n\nPress enter to continue...")

    if choice == "8":
        os.system("cls" if os.name == "nt" else "clear")
        animal = HHFSpider()
        if arboretum.swamps == []:
            os.system("cls" if os.name == "nt" else "clear")
            # Printing the header
            print( ''' +-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-+
 |  K  e  a  h  u  a    A  r  b  o  r  e  t  u  m  |
 +-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-+\n''')
            print("Uh Oh! There are no biomes for this animal to live in. Please go create a biome for this animal.")
            input("\n\nPress enter to continue...")
        else: 
            spider_habitats = list()
            for swamp in arboretum.swamps:
                if swamp.is_animals_full() == False:
                    spider_habitats.append(swamp)
            if spider_habitats != []:
                # Printing the header
                print( ''' +-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-+
 |  K  e  a  h  u  a    A  r  b  o  r  e  t  u  m  |
 +-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-+\n''')
                for index, swamp in enumerate(spider_habitats):
                    print(f'{index + 1}. Swamp ({swamp.current_animals} animals)')
                print("\nRelease the animal into which habitat?\n")

                choice8 = input("> ")
                try:
                    selection = spider_habitats[int(choice8) - 1].id
                    # append the animal to the biome list
                    swamp = list(filter(lambda x: x.id == selection, arboretum.swamps))

                    swamp[0].add_animal(animal)
                    os.system("cls" if os.name == "nt" else "clear")
                    # Printing the header
                    print( ''' +-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-+
 |  K  e  a  h  u  a    A  r  b  o  r  e  t  u  m  |
 +-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-+\n''')
                    print(F'Success! The {animal.species} has been added to the biome!')
                    input("\n\nPress enter to continue...")
                except: 
                    release_animal(arboretum)
            else: 
                # print this if there are biomes created but they are all full
                print("Uh-oh! It looks like all of the biomes are full! Please go create a new Habitat for this animal to live in.")
                input("\n\nPress enter to continue...")



