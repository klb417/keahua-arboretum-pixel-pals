from plants import Plant


class MountainAppleTree(Plant):
    def __init__(self):
        Plant.__init__(self, "Mountain Apple Tree", "partial", 17, "high")
        self.add_location("mountains")


