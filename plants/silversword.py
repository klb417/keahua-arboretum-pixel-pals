from plants import Plant


class Sliversword(Plant):
    def __init__(self):
        Plant.__init__(self, "Silversword", "shade", 22, "high")
        self.add_location("grassland")


