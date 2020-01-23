class Plant:

    def __init__(self):
        self.__species = ''
        self.__required_locations = []
        self.__sunlight = ''
        self.__seeds_produced = 0
        self.__insecticide_resistance = ''

    @property
    def species(self):
        return self.__species

    @property
    def required_locations(self):
        return self.__required_locations

    @property
    def sunlight(self):
        return self.__sunlight

    @property
    def seeds_produced(self):
        return self.__seeds_produced

    @property
    def insecticide_resistance(self):
        return self.__insecticide_resistance

    @species.setter
    def species(self, species_name):
        if type(species_name) is str:
            self.__species = species_name
        else:
            raise TypeError("Species must be a string.")

    def add_location(self, location):
        if type(location) is str:
            self.__required_locations.append(location)
        else:
            raise TypeError("location must be a string.")

    @seeds_produced.setter
    def seeds_produced(self, num_seeds):
        if type(num_seeds) is int:
            self.__seeds_produced = num_seeds
        else:
            raise TypeError("the number of seeds must be an integer")

    @insecticide_resistance.setter
    def insecticide_resistance(self, resistance):
        if type(resistance) is str:
            self.__insecticide_resistance = resistance
        else:
            raise TypeError("Insecticide resistance must be a string.")

