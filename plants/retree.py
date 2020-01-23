# from plants import Plant
from plant import Plant

class RiverEucalyptusTree(Plant):
    def __init__(self):
        Plant.__init__(self, "Rainbow Eucalyptus Tree", "full", 8, "low")
        self.add_location("forrest")


test = RiverEucalyptusTree()

print(test.required_locations)
