from animals import Animal
from interfaces import IFlying
from interfaces import Identifiable
from interfaces import IWalking
from interfaces import ITerrestrial
class nenegoose(Animal, IFlying, IWalking, ITerrestrial, Identifiable):

    def __init__(self):
        Animal.__init__(self, "Nene Goose")
        IFlying.__init__(self)
        IWalking.__init__(self)
        ITerrestrial.__init__(self)
        Identifiable.__init__(self)
        self.__prey = { "Grass", "Weedy Plants", "Berries" }

    @property
    def prey(self):
        return self.__prey

    def feed(self, prey):
        os.system('cls' if os.name == 'nt' else 'clear')
        print( ''' +-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-+
 |  K  e  a  h  u  a    A  r  b  o  r  e  t  u  m  |
 +-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-+\n''')
        if prey in self.__prey:
            print(f"The Nene Goose ate {prey} for a meal")
            input("Press any button to continue...")
        else:
            print(f"The Nene Goose rejects the {prey}")


    def __str__(self):
        return f"Nene Goose {self.id}. Can we buy some more Weedy plants, please! I'm sick of eating grass!!!!"