import os
from plants import RainbowEucalyptusTree, Sliversword, MountainAppleTree, BlueJadeVine
from .get_plant_biomes import get_plant_biomes


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
        for pb in plant_biomes:
            print(pb.name)
        new_choice = input()
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

