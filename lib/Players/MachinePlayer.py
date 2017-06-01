import random
from ..Cards import CustomErrorCard
from Player import Player

class MachinePlayer(Player):
    def __init__(self, name):
        Player.__init__(self,name)
        self.machine = True

    def lead_card(self):
        Player.lead_card(self)
        card = random.choice(self.cards)
        return self.playcard(card)        
        
    def follow_card(self, leadcard,leadplayer):
        Player.follow_card(self,leadcard,leadplayer)
        cards = self.get_beatable_cards(leadcard)
        if len(cards):
            card = min(cards)
            return self.playcard(card, leadcard)
        else:
            cards = self.get_playable_cards(leadcard)
            card_tbd = random.choice(cards)
            for card in cards:
            	try:
            		if card_tbd > card:
            		    card_tbd = card
            	except CustomErrorCard:
            		continue
            		
            return self.playcard(card_tbd, leadcard)
        
if __name__ == "__main__":
    print "Decide what to do"