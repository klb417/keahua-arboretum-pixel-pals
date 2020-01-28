# Author: Lauren Riddle
# Purpose: Holds the choices that call the create a new animal function
from animals import RiverDolphin, nenegoose, Ulae, Kikakapu, Pueo, Opeapea, HHFSpider, GDDGecko
import os
from .create_animal import create_animal_two_habitats, create_animal_one_habitat
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
        create_animal_two_habitats(arboretum.rivers, arboretum.coastlines, arboretum, animal)


    if choice == "2":
        os.system("cls" if os.name == "nt" else "clear")
        animal = GDDGecko()
        create_animal_one_habitat(arboretum.forests, arboretum, animal)


    if choice == "3":
        os.system("cls" if os.name == "nt" else "clear")
        animal = nenegoose()
        create_animal_one_habitat(arboretum.grasslands, arboretum, animal)
        

    if choice == "4":
        os.system("cls" if os.name == "nt" else "clear")
        animal = Kikakapu()
        create_animal_two_habitats(arboretum.rivers, arboretum.swamps, arboretum, animal)


    if choice == "5":
        os.system("cls" if os.name == "nt" else "clear")
        animal = Pueo()
        create_animal_two_habitats(arboretum.grasslands, arboretum.forests, arboretum, animal)


    if choice == "6":
        os.system("cls" if os.name == "nt" else "clear")
        animal = Ulae()
        create_animal_one_habitat(arboretum.coastlines, arboretum, animal)
       
    if choice == "7":
        os.system("cls" if os.name == "nt" else "clear")
        animal = Opeapea()
        create_animal_two_habitats(arboretum.mountains, arboretum.forests, arboretum, animal)

    if choice == "8":
        os.system("cls" if os.name == "nt" else "clear")
        animal = HHFSpider()
        create_animal_one_habitat(arboretum.swamps, arboretum, animal)