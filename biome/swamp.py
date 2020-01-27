from interfaces import Identifiable
from interfaces import IContainsAnimals
from interfaces import IContainsPlants
from .biome import Biome

# Swamp inherits from IContainsAnimals, IContainsPlants, Identifiable and Biome. IContainsAnimals and IContainsPlants are set with the maximum number of occupants they can accept. Identifiable gives each instance a unique uuid.
class Swamp(IContainsAnimals, IContainsPlants, Identifiable, Biome):
    def __init__(self, name):
        IContainsAnimals.__init__(self, 8)
        IContainsPlants.__init__(self, 12)
        Identifiable.__init__(self)
        Biome.__init__(self, name)

# Method to check if the biome is full. If it isn't full, the animal is added to the biome with .append. Otherwise an error message is displayed with a prompt to press the enter key to continue.
    def add_animal(self, animal):
        if not self.is_animals_full():
            self.animals.append(animal)
            
        else:
            print("Biome is full, choose another biome")
            input("Press ENTER to continue")

# Method to check if the biome is full. If it isn't full, the plant is added to the biome with .append. Otherwise an error message is displayed with a prompt to press the enter key to continue.
    def add_plant(self, plant):
        if not self.is_plants_full():
            self.plants.append(plant)
            
        else:
            print("Biome is full, choose another biome")
            input("Press ENTER to continue")