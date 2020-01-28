# RETREE.PY
#
# This module is responsible for creating the RainbowEucalyptusTree class.
# RainbowEucalyptusTree inherits from the Plant class.
#
# Author(s): Ryan Crowley

from plants import Plant


class RainbowEucalyptusTree(Plant):
    def __init__(self):
        Plant.__init__(self, "Rainbow Eucalyptus Tree", "full", 8, "low")
        self.add_location("forests")


