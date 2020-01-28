from animals import RiverDolphin, nenegoose, Ulae, Kikakapu, Pueo, Opeapea, HHFSpider, GDDGecko
import os
from actions import release_animal

def create_animal_two_habitats(biome1, biome2, arb, animal):
    os.system("cls" if os.name == "nt" else "clear")
    if biome1 == [] and biome2 == []:
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
        for habitat1 in biome1:
            # add the river to the list if it has less than 12 animals in it
            if habitat1.is_animals_full() == False:
                new_list.append(habitat1)
        for habitat2 in biome2:
            # add the coastline to the list if it has less than 15 animals in it
            if habitat2.is_animals_full() == False:
                new_list.append(habitat2)

        if new_list != []:
            # Printing the header
            print( ''' +-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-+
 |  K  e  a  h  u  a    A  r  b  o  r  e  t  u  m  |
 +-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-+\n''')
            # loop over list and display in terminal
            for index, place in enumerate(new_list):
                print(f'{index + 1}. {place.name} ({place.current_animals} animals)')
            print("\nRelease the animal into which habitat?\n")
            choice1 = input('''Type M to return to the main menu.
                 
> ''')
            if choice1.lower() == "m":
                return
            try:
                selection = new_list[int(choice1) - 1].id
                # search the river list for the selection
                list1 = list(filter(lambda x: x.id == selection, biome1))
                # search the coast list for the selection
                list2 = list(filter(lambda x: x.id == selection, biome2))
                if list1 != []:
                    # add the animal to the river that was found in the search
                    list1[0].add_animal(animal)
                elif list2 != []: 
                    # add the animal to the river that was found in the search
                    list2[0].add_animal(animal)
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
                create_animal_two_habitats(biome1, biome2, arb, animal)
        else:
            # print this if there are biomes created but they are all full
            print("Uh-oh! It looks like all of the biomes are full! Please go create a new Habitat for this animal to live in.")
            input("\n\nPress enter to continue...")


def create_animal_one_habitat():
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

            choice2 = input("Type M to return to the main menu. > ")

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
