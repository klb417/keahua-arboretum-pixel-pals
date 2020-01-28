# PLANT.PY
#
# This module is responsible for creating the Plant parent class. Plant inherits
# from the Indetifiable interface.
#
# Author(s): Ryan Crowley

from interfaces import Identifiable


class Plant(Identifiable):

    def __init__(self, species, sunlight, seeds_produced, insecticide_resistance):
        self.__species = species
        self.__sunlight = sunlight
        self.__seeds_produced = seeds_produced
        self.__insecticide_resistance = insecticide_resistance
        self.__required_locations = []
        Identifiable.__init__(self)

    @property
    def name(self):
        return f'{self.__species} ({str(self.id)[:8]})'

    @property
    def species(self):
        return self.__species


    @property
    def sunlight(self):
        return self.__sunlight

    @property
    def seeds_produced(self):
        return self.__seeds_produced

    @property
    def insecticide_resistance(self):
        return self.__insecticide_resistance

    @property
    def required_locations(self):
        return self.__required_locations

    @species.setter
    def species(self, species_name):
        if type(species_name) is str:
            self.__species = species_name
        else:
            raise TypeError("Species must be a string.")


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

    def add_location(self, location):
        if type(location) is str:
            self.__required_locations.append(location)
        else:
            raise TypeError("location must be a string.")

    def __str__(self):
        return self.name