from interfaces import Identifiable


class Biome:
    def __init__(self, name):
        self.name = name
        Identifiable.__init__(self)

    def __str__(self):
        return f"{self.name} [{str(self.id)[:8]}]"
