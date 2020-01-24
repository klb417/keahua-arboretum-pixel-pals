from plants import Plant


class BlueJadeVine(Plant):
    def __init__(self):
        Plant.__init__(self, "Blue Jade Vine", "partial", 0, "medium")
        self.add_location("grasslands")
        self.add_location("swamplands")


