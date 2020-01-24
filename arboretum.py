class Arboretum:
    def __init__(self, name, address):
        self.__name = name
        self.__address = address
        self.__biomes = {
            "rivers": [],
            "coastlines": [],
            "forests": [],
            "grasslands": [],
            "mountains": [],
            "swamps": [],
        }

    @property
    def name(self):
        return self.__name

    @property
    def address(self):
        return self.__address

    @property
    def rivers(self):
        return self.__biomes["rivers"]

    @property
    def coastlines(self):
        return self.__biomes["coastlines"]

    @property
    def forests(self):
        return self.__biomes["forests"]

    @property
    def grasslands(self):
        return self.__biomes["grasslands"]

    @property
    def mountains(self):
        return self.__biomes["mountains"]

    @property
    def swamps(self):
        return self.__biomes["swamps"]

    @property
    def biomes(self):
        return self.__biomes
