class IContainsPlants:
    def __init__(self, maximum_plants=0):
        self.__plants = []
        self.__maximum_plants = maximum_plants

    @property
    def plants(self):
        return self.__plants

    @property
    def maximum_plants(self):
        return self.__maximum_plants

    def is_plants_full(self):
        return len(self.plants) >= self.__maximum_plants
