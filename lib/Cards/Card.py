# -*- coding: iso-8859-15 -*-

import random
#Suits = ['Spade', 'Heart', 'Diamond', 'Club']
Ranks = ['A', 'K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2']
Rank_Power = {r:13-Ranks.index(r) for r in Ranks}
Suits = ['♠', '♥', '♦', '♣']

class CustomErrorCard(Exception):
	pass

class Card():
	def __init__(self, suit, rank):
		self.suit = suit
		self.rank = rank
		self.rank_power = Rank_Power[rank]
		self.player = None
		self.forsake_power = 13*(3-Suits.index(suit))+self.rank_power
	
	def __str__(self):
		return self.suit+self.rank	
	
	def dealt_to(self, player):
		self.player = player
		player.cards.append(self)
		
	def get_winning_card(self, cardlist):
		if len(cardlist)==0:
			return self		
		winning_card = self
		for card in cardlist:
			try:
				winning_card = max(winning_card, card)
			except CustomErrorCard:
				pass
		return winning_card		

	def __cmp__(self, card):
		if self.suit != card.suit:
			raise CustomErrorCard("Two cards in different suits: "+str(self)+","+str(card))
		else:
			return cmp(self.rank_power, card.rank_power)
			
	def __eq__(self,card):
		if self.suit==card.suit and self.rank == card.rank:
			return True
		else:
			return False
		
class CardDeck():
	def __init__(self):
		self.all_cards = []
		for suit in Suits:
			for rank in Ranks:
				self.all_cards.append(Card(suit,rank))
			
	def dealcard(self, players, card_for_each=0):
		all_cards = list(self.all_cards)
		player_cnt = len(players)
		index = 0
		remain = 0
		if card_for_each!= 0:
			remain = len(all_cards) - player_cnt*card_for_each
		while (len(all_cards)!=remain):
			index = index % player_cnt
			card = random.choice(all_cards)
			player = players[index]
			card.dealt_to(player)
			all_cards.remove(card)
			index = index + 1
	

if __name__ == "__main__":
	deck1 = CardDeck()
	spades = []
	clubs = []
	for card in deck1.all_cards:
		if card.suit == "Spade":
			spades.append(card)
		elif card.suit == "Club":
			clubs.append(card)

	minimum_s = min(spades)
	maximum_s = max(spades)
	print minimum_s
	print maximum_s
	
	minimum_c = min(clubs)
	print "minimum_s "+ str(minimum_s.forsake_power)
	print "maximum_s "+ str(maximum_s.forsake_power)	
	print "minimum_c "+ str(minimum_c.forsake_power)
	minimum_c = min(clubs)
	print min(minimum_c, minimum_s)