# SILVERSWORD.PY
#
# This module is responsible for creating the Silversword class. Silversword
# inherits from the Plant class.
#
# Author(s): Ryan Crowley

from plants import Plant


class Sliversword(Plant):
    def __init__(self):
        Plant.__init__(self, "Silversword", "shade", 22, "high")
        self.add_location("grasslands")


