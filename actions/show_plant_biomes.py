import os


# Function for displaying the possible biomes a plant can be added to
def show_plant_biomes(plant, biome_list):
    '''Function that displays a menu for selecting which biome a plant
    should be cultivated in.

    ARGUMENTS:
    plant (object)
    biome_list (list of objects)
    '''

    # Clears the terminal of previous contents
    os.system("cls" if os.name == "nt" else "clear")
    if biome_list:
        print('Cultivate Plant \n \n')
        for index, biome in enumerate(biome_list):
            # Example menu:     1. Forest (0 plants)
            #                   2. Forest (2 plants)
            print(f'{index + 1}. {biome.name} ({biome.current_plants} plants)')
        
        choice = input(f'''\nWhere would you like to cultivate the {plant.species}?
Type M to return to the main menu. > ''')

        if choice.lower() == "m":
            return
        else:
            try: 
                # checks to make sure that the choice the user entered can be
                # turned into an integer, and if so, that the choice is an
                # index that is not out of range of the biome_list.
                selected_biome = biome_list[int(choice) -1]
                # if selected_biome does not throw an error, the code below will
                # add the plant object to the biome that was selected by user.
                selected_biome.add_plant(plant)
                print(f"\nThe {plant.name} was added to {selected_biome.name}.")
                input('\n\n Type any key to return to the main menu.')
            except:
                show_plant_biomes(plant, biome_list)

    else:
        input(f'''Whoops!\n
There are no available habitats in the arboretum that are suitable for {plant.species}.
\nPress any key to return to the main menu. ''')