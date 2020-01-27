# from interfaces import IAquatic
from interfaces import Identifiable
from interfaces import IContainsAnimals
from interfaces import IContainsPlants
from .biome import Biome

# from animals import RiverDolphin


class River(IContainsAnimals, IContainsPlants, Identifiable, Biome):
    def __init__(self, name):
        IContainsAnimals.__init__(self, 12)
        IContainsPlants.__init__(self, 6)
        Identifiable.__init__(self)
        Biome.__init__(self, name)

    def add_animal(self, animal):
        if self.is_animals_not_full():
            try:
                if animal.aquatic and animal.cell_type == "hypertonic":
                    self.animals.append(animal)
            except AttributeError:
                raise AttributeError(
                    "Cannot add non-aquatic, or saltwater animals to a river"
                )
        else:
            print("Biome is full, choose another biome")

    def add_plant(self, plant):
        try:
            if plant.freshwater and plant.requires_current:
                self.plants.append(plant)
        except AttributeError:
            raise AttributeError(
                "Cannot add plants that require brackish water or stagnant water to a river biome"
            )
