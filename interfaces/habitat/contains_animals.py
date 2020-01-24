class IContainsAnimals:
    def __init__(self, maximum_animals=0):
        self.__animals = []
        self.__maximum_animals = maximum_animals

    @property
    def animals(self):
        return self.__animals

    def is_animals_not_full(self):
        return len(self.__animals) < self.__maximum_animals
