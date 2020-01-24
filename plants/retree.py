from plants import Plant


class RainbowEucalyptusTree(Plant):
    def __init__(self):
        Plant.__init__(self, "Rainbow Eucalyptus Tree", "full", 8, "low")
        self.add_location("forest")


