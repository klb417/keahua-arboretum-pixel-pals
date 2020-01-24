import os
from plants import RainbowEucalyptusTree, Sliversword, MountainAppleTree, BlueJadeVine
from .get_plant_biomes import get_plant_biomes

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



# Function for adding a plant to the arboretum
def cultivate_plant(arboretum):

    # Clears the terminal of previous contents
    os.system("cls" if os.name == "nt" else "clear")

    # Printing menu options to the console
    print('''Plants
    ''')
    print("1. Rainbow Eucalyptus Tree")
    print("2. Silversword")
    print("3. Mountain Apple Tree")
    print("4. Blue Jade Vine")

    # Capturing user input and assigning it to "choice" variable
    choice = input('''
Choose a plant to cultivate, or
Type M to return to the main menu. > ''')

    # if statements check user input, when it evaluates to true the selected plant
    # is used as the basis for the next menu

    if choice == "1":
        plant = RainbowEucalyptusTree()
        plant_biomes = get_plant_biomes(plant, arboretum)
        show_plant_biomes(plant, plant_biomes)
    elif choice == "2":
        pass
    elif choice == "3":
        pass
    elif choice == "4":
        pass
    elif choice.lower() == "m":
        return
    else:
        cultivate_plant(arboretum)

