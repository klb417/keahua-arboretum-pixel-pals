# FEEDING_THE_ANIMAL.PY
#
# This module is respossible for getting the list of prey that the animals can eat
# then calling the feed method attached to the animals. I also added exempts for 
# when people go off the golden path.
#
# Author(s): James Chapman

import os

def feeding_the_animal(animal):
        #once the number is found it will run the animal selected
        thisAnimal = animal()
        # I set up a variable for the prey of the animal specifically
        thePrey = tuple(thisAnimal.prey)
        os.system('cls' if os.name == 'nt' else 'clear')
        print( ''' +-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-+
 |  K  e  a  h  u  a    A  r  b  o  r  e  t  u  m  |
 +-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-+\n''')
        # this for loop goes through the prey and print it with a number that is the index +1 using the enumerate method
        for index, prey in enumerate(thePrey):
            print(f"{index + 1}. {prey}")
        print(f"\nWhat is on the menu for the {thisAnimal.species} today?\n")
        # a question is presented to the user then a variable is created for the choice of the input
        choice = input('''Type M to return to the main menu.
            
> ''')

        if choice.lower() == "m":
            return
        # a try and except is deployed to catch any errors when selecting a choice.
        try:
            # assuming the user selects a valid number the program excutes the feed method for the animal. Since we added 1 to the index we need to make sure to take it away again.
            thisAnimal.feed(thePrey[int(choice) - 1])
        except:
            os.system('cls' if os.name == 'nt' else 'clear')
            print( ''' +-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-+
 |  K  e  a  h  u  a    A  r  b  o  r  e  t  u  m  |
 +-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-+\n''')
            # this except was added incase someone types in/selects a number that is not on the list provided. This will also happen if they try to type in a word.
            print("pick a number on the list...")
            input("Press Enter to continue.")

            os.system('cls' if os.name == 'nt' else 'clear')
            print( ''' +-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-+
 |  K  e  a  h  u  a    A  r  b  o  r  e  t  u  m  |
 +-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-+\n''')
            for index, prey in enumerate(thePrey):
                print(f"{index + 1}. {prey}")
            print(f"\nWhat is on the menu for the {thisAnimal.species} today?\n")
            choice = input('''Type M to return to the main menu.
            
> ''')
            if choice.lower() == "m":
                return
       
            try:
                thisAnimal.feed(thePrey[int(choice) - 1])
            except:
                #this part is repeated so that if they keep selecting bad numbers or words that it will loop around
                os.system('cls' if os.name == 'nt' else 'clear')
                print( ''' +-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-+
 |  K  e  a  h  u  a    A  r  b  o  r  e  t  u  m  |
 +-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-+\n''')
                print("pick a number on the list...")
                input("Press Enter to continue.")
                feeding_the_animal(animal)