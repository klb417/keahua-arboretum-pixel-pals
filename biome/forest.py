from interfaces import Identifiable
from interfaces import IContainsAnimals
from interfaces import IContainsPlants
from .biome import Biome


class Forest(IContainsAnimals, IContainsPlants, Identifiable, Biome):

    def __init__(self, name):
        IContainsAnimals.__init__(self, 20)
        IContainsPlants.__init__(self, 32)
        Identifiable.__init__(self)
        Biome.__init__(self, name)

    def add_animal(self, animal):
        # Add in checks for animal type
        self.animals.append(animal)


    def add_plant(self, plant):
        # Add in checks for plant type
        self.plants.append(plant)
   