class IContainsPlants:
    def __init__(self, maximum_plants=0):
        self.__plants = dict()
        self.__maximum_plants = maximum_plants
        self.__current_plants = 0

    @property
    def plants(self):
        return self.__plants

    @property
    def maximum_plants(self):
        return self.__maximum_plants

    def is_plants_full(self):
        return len(self.plants) >= self.__maximum_plants

    @property
    def current_plants(self):
        return self.__current_plants

    def add_plant_to_list(self, plant):
        if plant.species not in self.plants.keys():
            self.plants.update({f"{plant.species}": [plant]})
        else:
            self.plants[f"{plant.species}"].append(plant)
        self.__current_plants += 1
