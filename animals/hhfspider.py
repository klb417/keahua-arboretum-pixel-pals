from animals import Animal
from interfaces import IWalking
from interfaces import Identifiable
from interfaces import ITerrestrial
class HHFSpider(Animal, IWalking, ITerrestrial, Identifiable):

    def __init__(self):
        Animal.__init__(self, "Hawaiian Happy-Face Spider")
        IWalking.__init__(self)
        Identifiable.__init__(self)
        ITerrestrial.__init__(self)
        self.__prey = { "Flies", "Crunchberries", "Wasp" }

    @property
    def prey(self):
        return self.__prey

    def feed(self, prey):
        if prey in self.__prey:
            print(f"The Hawaiian Happy-Face Spider ate {prey} for a meal")
        else:
            print(f"The Hawaiian Happy-Face Spider rejects the {prey}")


    def __str__(self):
        return f"Hawaiian Happy-Face Spider {self.id}. Give me Flies!"