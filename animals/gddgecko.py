from animals import Animal
from interfaces import IWalking
from interfaces import Identifiable
from interfaces import ITerrestrial
class GDDGecko(Animal, IWalking, ITerrestrial, Identifiable):

    def __init__(self):
        Animal.__init__(self, "'Ulae")
        IWalking.__init__(self)
        Identifiable.__init__(self)
        ITerrestrial.__init__(self)
        self.__prey = { "Spider", "Worm", "Crunchberries", "Beetle" }

    @property
    def prey(self):
        return self.__prey

    def feed(self, prey):
        if prey in self.__prey:
            print(f"The Gold Dust Day Gecko ate {prey} for a meal")
        else:
            print(f"The Gold Dust Day Gecko rejects the {prey}")


    def __str__(self):
        return f"Gold Dust Day Gecko {self.id}. I want more Crunchberries!"