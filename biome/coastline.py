from interfaces import Identifiable
from interfaces import IContainsAnimals
from interfaces import IContainsPlants
from .biome import Biome

# Coastline inherits from IContainsAnimals, IContainsPlants, Identifiable and Biome. IContainsAnimals and IContainsPlants are set with the maximum number of occupants they can accept. Identifiable gives each instance a unique uuid.
class Coastline(IContainsAnimals, IContainsPlants, Identifiable, Biome):
    def __init__(self, name):
        IContainsAnimals.__init__(self, 15)
        IContainsPlants.__init__(self, 3)
        Identifiable.__init__(self)
        Biome.__init__(self, name)

# Method to check if the biome is full. If it isn't full, the animal is added to the biome with .append. Otherwise an error message is displayed with a prompt to press the enter key to continue.
    def add_animal(self, animal):
        if not self.is_animals_full():
            self.add_animal_to_list(animal)

        else:
            print("Biome is full, choose another biome")
            input("Press ENTER to continue")

# Method to check if the biome is full. If it isn't full, the plant is added to the biome with .append. Otherwise an error message is displayed with a prompt to press the enter key to continue.
    def add_plant(self, plant):
        if not self.is_plants_full():
            self.add_plant_to_list(plant)

        else:
            print("Biome is full, choose another biome")
            input("Press ENTER to continue")
