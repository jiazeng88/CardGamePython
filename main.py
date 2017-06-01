#!/usr/bin/python

import sys,getopt

from lib import Card,CardDeck,CustomErrorCard
from lib import Player,MachinePlayer,PersonPlayer,MachineSmart
from lib import Game
from lib import CardSmart

def main(argv):
    card_cnt = None
    machine_cnt = None
    smart_cnt = None
    people_cnt = None
    try:
        opts, args = getopt.getopt(argv,"hc:m:s:p:",["help", "card", "machine", "smart", "people"])
    except getopt.GetoptError:
        print __file__ + ' -card <num_card_per_player> -machine <num_regular_machin_player> -smart <num_smart_machine_player>'
        # python main.py -c 12 -m 2 -s 1 -p 1
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print __file__ + ' -card <num_card_per_player> -machine <num_regular_machin_player> -smart <num_smart_machine_player> -people <num_people_player>'
            sys.exit()
        elif opt in ("-c", "-card"):
            card_cnt = int(arg)
        elif opt in ("-m", "-machine"):
            machine_cnt = int(arg)  
        elif opt in ("-s", "-smart"):
            smart_cnt = int(arg)
        elif opt in ("-p", "-people"):
            people_cnt = int(arg)            
    
    player_list = []
    for i in range (0, machine_cnt):
        name = "ROBOT" + str(i+1)
        player_list.append(MachinePlayer(name))
    for i in range (0, smart_cnt):
        name = "SMART" + str(i+1)
        player_list.append(MachineSmart(name))
    for i in range (0, people_cnt):
        name = "ZENG"
        player_list.append(PersonPlayer(name))

    game1 = Game(player_list, card_cnt)
    game1.play_game(game1.lead)
    
if __name__ == "__main__":
    if len(sys.argv)<2:
        print __file__ + ' -card <num_card_per_player> -machine <num_regular_machin_player> -smart <num_smart_machine_player> -people <num_people_player>'
        sys.exit()        
    main(sys.argv[1:])