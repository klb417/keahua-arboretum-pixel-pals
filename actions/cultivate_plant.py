import os
from plants import RainbowEucalyptusTree, Sliversword, MountainAppleTree, BlueJadeVine
from .get_plant_biomes import get_plant_biomes
from .show_plant_biomes import show_plant_biomes

# Function for displaying a menu for adding a plant to the arboretum.
def cultivate_plant(arboretum):
    '''Function for displaying a menu for adding a plant to the arboretum.
    Takes input from a user and calls the get_plant_biomes function and
    the show_plant_biomes functions.

    ARGUMENTS:
    arboretum (object)
    '''

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
        plant = Sliversword()
        plant_biomes = get_plant_biomes(plant, arboretum)
        show_plant_biomes(plant, plant_biomes)
    elif choice == "3":
        plant = MountainAppleTree()
        plant_biomes = get_plant_biomes(plant, arboretum)
        show_plant_biomes(plant, plant_biomes)
    elif choice == "4":
        plant = BlueJadeVine()
        plant_biomes = get_plant_biomes(plant, arboretum)
        show_plant_biomes(plant, plant_biomes)
    elif choice.lower() == "m":
        return
    else:
        cultivate_plant(arboretum)

