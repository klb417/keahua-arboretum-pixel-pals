class IContainsAnimals:
    def __init__(self, maximum_animals=0):
        self.__animals = []
        self.__maximum_animals = maximum_animals

    @property
    def animals(self):
        return self.__animals

    @property
    def maximum_animals(self):
        return self.__maximum_animals

    def is_animals_full(self):
        return len(self.__animals) >= self.__maximum_animals
