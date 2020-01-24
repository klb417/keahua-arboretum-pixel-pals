from animals import Animal
from interfaces import ITerrestrial
from interfaces import IFlying
from interfaces import Identifiable
class Pueo(Animal, ITerrestrial, Identifiable):

    def __init__(self):
        Animal.__init__(self, "Pueo")
        ITerrestrial.__init__(self)
        Identifiable.__init__(self)
        self.__prey = { "Mice", "Rabbits", "Squirrels" }

    @property
    def prey(self):
        return self.__prey

    def feed(self, prey):
        if prey in self.__prey:
            print(f"The Pueo ate {prey} for a meal")
            input("Press any button to continue...")
        else:
            print(f"The Pueo rejects the {prey}")


    def __str__(self):
        return f"Pueo {self.id}. I need to go catch some moths!"