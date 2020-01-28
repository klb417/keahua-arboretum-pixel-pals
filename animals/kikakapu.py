# Authors: Lauren and James
# defines a class for creating the Kikakapu
from animals import Animal
from interfaces import IFreshwater
from interfaces import Identifiable
import os

class Kikakapu(Animal, IFreshwater, Identifiable):

    def __init__(self):
        Animal.__init__(self, "Kikakapu")
        IFreshwater.__init__(self)
        Identifiable.__init__(self)
        self.__prey = { "Planktonic Animals", "Vegetation", "Trout", "Mackarel", "Salmon", "Sardine" }

    @property
    def prey(self):
        return self.__prey

    def feed(self, prey):
        os.system('cls' if os.name == 'nt' else 'clear')
        print( ''' +-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-+
 |  K  e  a  h  u  a    A  r  b  o  r  e  t  u  m  |
 +-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-+\n''')
        if prey in self.__prey:
            print(f"The Kikakapu ate {prey} for a meal")
            input("Press any button to continue...")
        else:
            print(f"The Kikakapu rejects the {prey}")


    def __str__(self):
        return f"Kikakapu {self.id}. I want more Planktonic Animals but...... Crunchberries will do!"