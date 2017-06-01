import random
from ..Cards import Card,CardDeck,CustomErrorCard

class Game():
    def __init__(self, player_list, card_for_each, lead=None):
        self.players = player_list
        random.shuffle(self.players)
    	self.player_cnt = len(self.players)
    	self.trumps=None
    	self.tricks = card_for_each
    	self.tricks_done = 0
        self.trick_history = {}
    	self.player_runout_suit = {}
    	self.player_bigcard_suit = {}
    	if lead!=None:
            self.lead=lead
        else:
            self.lead=random.choice(self.players)

        deck = CardDeck()
        deck.dealcard(self.players,self.tricks)
        for player in self.players:
            i = self.players.index(player)
            if i<self.player_cnt-1:
                player.nextplayer = self.players[i+1]
            else:
                player.nextplayer = self.players[0]
            player.start_new_game(self)

    def get_queue(self,leadplayer):
        queue = [leadplayer]
        while len(queue) < self.player_cnt:
            queue.append(queue[-1].nextplayer)
        return queue

    def play_trick(self, leadplayer):
        play_queue = self.get_queue(leadplayer)
        current_trick = self.tricks_done + 1
        self.trick_history[current_trick] = {}
        self.trick_history[current_trick]['lead'] = leadplayer.name
        self.trick_history[current_trick]['cards'] = []
        self.trick_history[current_trick]['winner'] = None
        print "=================Trick #"+str(current_trick)+"=================="
        winning_card = leadplayer.lead_card()
        self.trick_history[current_trick]['cards'].append(leadplayer.name+":"+str(winning_card))
        
        for player in play_queue[1:]:
            card = player.follow_card(winning_card,leadplayer)
            self.trick_history[self.tricks_done + 1]['cards'].append(player.name+":"+str(card))
            winning_card = winning_card.get_winning_card([card])
        winner = winning_card.player
        winner.tricks += 1
        self.trick_history[current_trick]['winner'] = winner.name
        print "========= Trick #"+str(current_trick)+" winner: " + str(winner)+" ========="
        self.tricks_done += 1
        return winner

    def print_history(self):
        print "=================================Summary================================"
        print "Trick#"+"\t"+"Lead"+"\t"+"Cards Played"
        for trick_num in range(1,self.tricks+1):
            print str(trick_num) + "\t" + self.trick_history[trick_num]['lead'] + "\t" + '; '.join(self.trick_history[trick_num]['cards'])+ "\t" + self.trick_history[trick_num]['winner']

    def get_game_winner(self):
        #return the player who wins the game
        self.print_history()
        win_tricks = [player.tricks for player in self.players]
        wins = max(win_tricks)
        winners = [player for player in self.players if player.tricks == wins]
        if len(winners) > 1:
            print "We got a tie in this game"
        for winner in winners:
            print "Winner of the game : "+winner.name+" got " + str(wins)+" tricks."
            
        for player in self.players:
            if player not in winners:
                print "Player "+player.name+" got " + str(player.tricks)+" tricks."

        return winners

    def play_game(self, leadplayer):
        while True:
            self.play_round(leadplayer)
            leadplayer = self.lead
            self.reset()
        
    def reset(self):
    	self.tricks_done = 0
        self.trick_history = {}
    	self.player_runout_suit = {}
    	self.player_bigcard_suit = {}

        deck = CardDeck()
        deck.dealcard(self.players,self.tricks)
        for player in self.players:
            player.start_new_game(self)

    def play_round(self, leadplayer):
        next_lead = leadplayer
        while self.tricks_done!=self.tricks:
            next_lead = self.play_trick(next_lead)
        winners = self.get_game_winner()
        random.shuffle(winners)
        self.lead = winners[0]
            
    #update if a player has runout of this suit
    def update_player_runout_suit(self, player_name, suit):
        if self.player_runout_suit[player_name]:
            if suit not in self.player_runout_suit[player_name]:
                self.player_runout_suit[player_name].append(suit)
        else:
            self.player_runout_suit[player_name] = [suit]
            
if __name__ == "__main__":
    print "Decide what to do"            