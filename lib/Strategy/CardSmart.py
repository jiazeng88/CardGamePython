#From a list of player's cards and picks a card to play
#
from ..Cards import CustomErrorCard
	
class CardSmart():
	def __init__(self, player):
		self.cards = player.cards
		self.player = player

	def smart_leadcard(self):
		smart_suits = set([])
		smart_cards = []

		for pname in self.player.game.player_runout_suit.keys():
			if  pname == self.player.name:
				continue
			elif self.player.game.player_runout_suit[pname]:
				smart_suits = smart_suits|set(self.player.game.player_runout_suit[pname])
			else:
				pass

		if smart_suits:
			for card in self.cards:
				if card.suit in smart_suits:
					smart_cards.append(card)

		if len(smart_cards)==0:
			smart_cards = self.cards

		smart_cards.sort(key=lambda x : x.rank_power)
		return smart_cards[-1]
	
	def smart_follow_card(self, leadcard, leadplayer):
		play_queue = self.player.game.get_queue(leadplayer)

		bigger_cards = self.player.get_beatable_cards(leadcard)
		
		if len(bigger_cards) == 0:
			cards = self.player.get_playable_cards(leadcard)
			card_tbd = cards[0]
			for card in cards:
				if card_tbd.rank_power > card.rank_power:
					card_tbd = card
			return card_tbd
		elif len(bigger_cards) == 1:
			return bigger_cards[0]
		
		if self.player == play_queue[-1]:
			return min(bigger_cards)
		else:
			player_index = play_queue.index(self.player)
			return self.smart_middle_card(leadcard, bigger_cards, play_queue[player_index+1:])
	
	def smart_middle_card(self, leadcard, beatable_cards, players):
		beatable_cards.sort()
		suit = leadcard.suit
		safe = 0
		player_names = [x.name for x in players]
		
		for pname in self.player.game.player_runout_suit.keys():
			if  pname not in player_names:
				continue
			elif self.player.game.player_runout_suit[pname] and suit in self.player.game.player_runout_suit[pname]:
				safe += 1
			else:
				pass
		
		if safe == len(players):
			return beatable_cards[0]
		elif 0<safe<len(players):
			return beatable_cards[1]
		else:
			return beatable_cards[-1]
	

if __name__ == "__main__":
	print "Decide what to do"