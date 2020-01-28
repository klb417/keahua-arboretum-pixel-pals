import os
from animals import RiverDolphin, GDDGecko, HHFSpider, Kikakapu, nenegoose, Opeapea, Pueo, Ulae
from .feeding_the_animal import feeding_the_animal

# def feeding_animals(animal):
#     os.system('cls' if os.name == 'nt' else 'clear')
#     for index, prey in enumerate(animal.prey):
#         print(f"{index + 1}. {prey}")
#     print(f"What is on the menu for the {animal.species} today? >")
#     choice = input("> ")



def feed_animal():
    os.system('cls' if os.name == 'nt' else 'clear')
    print( ''' +-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-+
 |  K  e  a  h  u  a    A  r  b  o  r  e  t  u  m  |
 +-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-+\n''')
    print("1. Gold Dust Day Gecko")
    print("2. River Dolphin")
    print("3. Nene Goose")
    print("4. Kikakapu")
    print("5. Pueo")
    print("6. 'Ulae")
    print("7. Ope'ape'a")
    print("8. Happy-Face Spider")

    print("\nChoose animal to feed.")
    choice = input('''Type M to return to the main menu.
    
> ''')

    if choice.lower() == "m":
        return
# once a number is chosen the program will go through this if else statement to find the number that was
    elif choice == "1":
        feeding_the_animal(GDDGecko)
        #original code before making feeding_the_animal module
#         #once the number is found it will run the animal selected
#         g_d_d_gecko = GDDGecko()
#         # I set up a variable for the prey of the animal specifically
#         gddgprey = tuple(g_d_d_gecko.prey)
#         os.system('cls' if os.name == 'nt' else 'clear')
#         print( ''' +-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-+
#  |  K  e  a  h  u  a    A  r  b  o  r  e  t  u  m  |
#  +-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-+\n''')
#         # this for loop goes through the prey and print it with a number that is the index +1 using the enumerate method
#         for index, prey in enumerate(gddgprey):
#             print(f"{index + 1}. {prey}")
#         print(f"\nWhat is on the menu for the Gold Dust Day Gecko today?\n")
#         # a question is presented to the user then a variable is created for the choice of the input
#         choice = input('''Type M to return to the main menu.
        
# > ''')

#         if choice.lower() == "m":
#             return
#         # print(choice, index, gddgprey)
#         # a try and except is deployed to catch any errors when selecting a choice.
#         try:
#             # assuming the user selects a valid number the program excutes the feed method for the animal. Since we added 1 to the index we need to make sure to take it away again.
#             print(gddgprey[int(choice) - 1])
#             print(type(gddgprey[int(choice) - 1]))
#             g_d_d_gecko.feed(gddgprey[int(choice) - 1])
#         except:
#             os.system('cls' if os.name == 'nt' else 'clear')
#             print( ''' +-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-+
#  |  K  e  a  h  u  a    A  r  b  o  r  e  t  u  m  |
#  +-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-+\n''')
#             # this except was added incase someone types in/selects a number that is not on the list provided. This will also happen if they try to type in a word.
#             print("pick a number on the list...")
#             input("Press any button to continue.")
#             # this will re start the feed animals module so that they could try again
#             return feed_animal()
        
    elif choice == "2":
        feeding_the_animal(RiverDolphin)

    elif choice == "3":
        feeding_the_animal(nenegoose)

    elif choice == "4":
        feeding_the_animal(Kikakapu)
        
    elif choice == "5":
        feeding_the_animal(Pueo)

    elif choice == "6":
        feeding_the_animal(Ulae)

    elif choice == "7":
        feeding_the_animal(Opeapea)

    elif choice == "8":
        feeding_the_animal(HHFSpider)

    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print( ''' +-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-+
 |  K  e  a  h  u  a    A  r  b  o  r  e  t  u  m  |
 +-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-+\n''')
        # this is a catch so that if a number is selected that is not on the list it will take them back to the beginning to try again
        print("Pick a number that is actually on the list...")
        input("Press Enter to continue.")
        return feed_animal()