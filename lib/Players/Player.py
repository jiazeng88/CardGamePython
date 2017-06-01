import random
from ..Cards import CustomErrorCard

class Player():
    def __init__(self, name):
		self.name = name
		self.cards = []
		self.tricks = 0
		self.nextplayer = None
		self.suitinfo = {}
		self.game = None
    
    def __str__(self):
        return self.name
		
    def start_new_game(self, game):
        self.tricks = 0
        self.cards.sort(key=lambda x : x.forsake_power)
        self.game = game
        self.game.player_runout_suit[self.name] = []
        self.game.player_bigcard_suit[self.name] = []
        
    def get_playable_cards(self, leadcard=None):
		if leadcard:
			legal_cards = []
			for card in self.cards:
				if card.suit == leadcard.suit:
					legal_cards.append(card)
					
			if legal_cards:
				return legal_cards
				
		return self.cards


    def get_beatable_cards(self,leadcard,trumps=None):
		playable = self.get_playable_cards(leadcard)
		beatable = []
		for card in playable:
			if card.suit == leadcard.suit:
				if card.rank_power > leadcard.rank_power:
					beatable.append(card)
			elif card.suit == trumps:
				beatable.append(card)
			else:
				pass
				
		return beatable

    def playcard(self, card, leadcard=None):
        print str(self) + " played " + str(card)
        self.cards.remove(card)
        if leadcard and leadcard.suit != card.suit:
            self.game.update_player_runout_suit(self.name, leadcard.suit)
            
        return card
        
    def lead_card(self):
        print str(self) + " is leading this trick"
        
    def follow_card(self, card, leadplayer):
    	if self.machine != True:
        	print str(self) + " follows " + str(card) + " by"
        
if __name__ == "__main__":
    print "Decide what to do"