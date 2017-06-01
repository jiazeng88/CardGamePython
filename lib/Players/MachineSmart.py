import random
from ..Cards import CustomErrorCard
from MachinePlayer import *
from ..Strategy import CardSmart

class MachineSmart(MachinePlayer):
    def __init__(self, name):
        MachinePlayer.__init__(self,name)
        self.smart = CardSmart(self)

    def lead_card(self):
        Player.lead_card(self)
        card = self.smart.smart_leadcard()
        return self.playcard(card)        
    
    def follow_card(self, leadcard,leadplayer):
        Player.follow_card(self,leadcard,leadplayer)
        card = self.smart.smart_follow_card(leadcard,leadplayer)
        return self.playcard(card, leadcard)          

if __name__ == "__main__":
    print "Decide what to do"