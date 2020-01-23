from plants import Plant


class MountainAppleTree(Plant):
    def __init__(self):
        Plant.__init__(self, "Mountain Apple Stree", "partial", 17, "high")
        self.add_location("mountain")


