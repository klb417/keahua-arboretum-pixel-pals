from animals import Animal
from interfaces import ITerrestrial
from interfaces import IFlying
from interfaces import Identifiable
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
        if prey in self.__prey:
            print(f"The Opeapea ate {prey} for a meal")
            input("Press any button to continue...")
        else:
            print(f"The Opeapea rejects the {prey}")


    def __str__(self):
        return f"Opeapea {self.id}. I need to go catch some moths!"