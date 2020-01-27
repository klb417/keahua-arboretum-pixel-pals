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
        if not self.is_animals_full():
            self.add_animal_to_list(animal)

        else:
            print("Biome is full, choose another biome")
            input("Press ENTER to continue")

    def add_plant(self, plant):
        if not self.is_plants_full():
            self.add_plant_to_list(plant)

        else:
            print("Biome is full, choose another biome")
            input("Press ENTER to continue")
