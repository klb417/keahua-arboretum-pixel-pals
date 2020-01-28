# Authors: Lauren and James
# defines a class for creating the Opeapea
from animals import Animal
from interfaces import ITerrestrial
from interfaces import IFlying
from interfaces import Identifiable
import os

class Opeapea(Animal, IFlying, Identifiable):

    def __init__(self):
        Animal.__init__(self, "Opeapea")
        IFlying.__init__(self)
        Identifiable.__init__(self)
        self.__prey = { "Moths", "Beetles", "Termites" }

    @property
    def prey(self):
        return self.__prey

    def feed(self, prey):
        os.system('cls' if os.name == 'nt' else 'clear')
        print( ''' +-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-+
 |  K  e  a  h  u  a    A  r  b  o  r  e  t  u  m  |
 +-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-+\n''')
        if prey in self.__prey:
            print(f"The Opeapea ate {prey} for a meal")
            input("Press any button to continue...")
        else:
            print(f"The Opeapea rejects the {prey}")


    def __str__(self):
        return f"Opeapea {self.id}. I need to go catch some moths!"