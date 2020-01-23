from animals import Animal
from interfaces import IFreshwater
from interfaces import Identifiable
class Nene_Goose(Animal, IFreshwater, Identifiable):

    def __init__(self):
        Animal.__init__(self, "Nene Goose")
        IFreshwater.__init__(self)
        Identifiable.__init__(self)
        self.__prey = { "Grass", "Weedy Plants", "Berries" }

    @property
    def prey(self):
        return self.__prey

    def feed(self, prey):
        if prey in self.__prey:
            print(f"The Nene Goose ate {prey} for a meal")
        else:
            print(f"The Nene Goose rejects the {prey}")


    def __str__(self):
        return f"Nene Goose {self.id}. Can we buy some more Weedy plants, please! I'm sick of eating grass!!!!"