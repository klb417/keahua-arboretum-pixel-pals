from interfaces import Identifiable
from interfaces import IContainsAnimals
from interfaces import IContainsPlants
from interfaces import IWalking
from .biome import Biome

class Mountain(IContainsAnimals, IContainsPlants, Identifiable, Biome):

    def __init__(self, name):
        IContainsAnimals.__init__(self, 6)
        IContainsPlants.__init__(self, 4)
        Identifiable.__init__(self)
        Biome.__init__(self, name)

    def add_animal(self, animal):
        if self.is_animals_not_full():
            try:
                if isinstance(animal, IWalking):
                    self.animals.append(animal)
            except AttributeError:
                raise AttributeError(
                    "Cannot add aquatic animals to a mountain"
                )
        else:
            print("Choose another biome")

    def add_plant(self, plant):
        # Add in checks for plant type
        self.plants.append(plant)