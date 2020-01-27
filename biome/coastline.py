from interfaces import Identifiable
from interfaces import IContainsAnimals
from interfaces import IContainsPlants
from .biome import Biome


class Coastline(IContainsAnimals, IContainsPlants, Identifiable, Biome):
    def __init__(self, name):
        IContainsAnimals.__init__(self, 15)
        IContainsPlants.__init__(self, 3)
        Identifiable.__init__(self)
        Biome.__init__(self, name)

    def add_animal(self, animal):
        if self.is_animals_not_full():
            try:
                if animal.aquatic and animal.cell_type == "hypotonic":
                    self.animals.append(animal)
            except AttributeError:
                raise AttributeError(
                    "Cannot add non-aquatic, or freshwater animals to a coastline"
                )
        else:
            print("Choose another biome")

    def add_plant(self, plant):
        # Add in checks for plant type
        self.plants.append(plant)
