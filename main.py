import pygame
from pygame.locals import *
import os
import sys
a = os.getcwd()
sys.path.insert(0,rf'{a}\Analysis')
from fetchpgn import *
from userinfo import *
sys.path.insert(0,rf'{a}\GUI')
from gui_main import *


username = input("Give Your chess.com username: ")

get_player_rating(username)



PGN = PGN_analyzer("games.pgn")
moves_list = PGN.moves_list
result = PGN.analyze_all_moves()
adv = PGN.adv

main=Main("ThermalDust095",974,moves_list)
main.mainloop(result,adv)