from interfaces import Identifiable
from interfaces import IContainsAnimals
from interfaces import IContainsPlants
from .biome import Biome

class Grassland(IContainsAnimals, IContainsPlants, Identifiable, Biome):

    def __init__(self, name):
        IContainsAnimals.__init__(self)
        IContainsPlants.__init__(self)
        Identifiable.__init__(self)
        Biome.__init__(self, name)

    def add_animal(self, animal):
        self.animals.append(animal)

    def add_plant(self, plant):
        # Add in checks for plant type
        self.plants.append(plant)
        