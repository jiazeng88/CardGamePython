# -*- coding: iso-8859-15 -*-

import random
from ..Cards import CustomErrorCard
from Player import Player

class PersonPlayer(Player):
    def __init__(self, name):
        Player.__init__(self, name)
        self.machine = False
 
    def list_these_cards(self,cardlist):
		for card in cardlist:
		    print str(cardlist.index( card )) + ":" + str(card)
	    
    def pick_card_from_list(self, cardlist):
        maximum = len(cardlist)-1
        card_num = maximum + 1
        
        if maximum ==0:
            return cardlist[0]
            
        self.list_these_cards(cardlist)          
	    
        while 1:
            card_num = int(raw_input("\t picking a number from 0 to %s: " %maximum))
            if card_num < 0 or card_num > maximum:
                print ("Chosen number %s is out of range. Choose again, range is 0 to %s " %(card_num, maximum))
                continue
            else:
                break
        return cardlist[card_num]	    

    def lead_card(self):
        Player.lead_card(self)
        card = self.pick_card_from_list(self.cards)
        return self.playcard(card)        

    def follow_card(self, leadcard,leadplayer):
        Player.follow_card(self,leadcard,leadplayer)
        cards = self.get_playable_cards(leadcard)
        card = self.pick_card_from_list(cards)
        return self.playcard(card,leadcard)
        
if __name__ == "__main__":
    print "Decide what to do"