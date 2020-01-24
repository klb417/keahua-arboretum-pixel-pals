import os


# Function for displaying the possible biomes a plant can be added to
def show_plant_biomes(plant, biome_list):
    # Clears the terminal of previous contents
    os.system("cls" if os.name == "nt" else "clear")
    if biome_list:
        print('Cultivate Plant \n \n')
        for index, biome in enumerate(biome_list):
            print(f'{index + 1}. {biome.name} ( plants)')
        
        choice = input(f'''
Where would you like to cultivate the {plant.species}?
Type M to return to the main menu. > ''')
    else:
        input(f'''Whoops!

There are no available habitats in the arboretum that are suitable for {plant.species}.

Press any key to return to the main menu. ''')