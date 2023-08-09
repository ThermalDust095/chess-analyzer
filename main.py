import argparse

from Analysis.analyser import *
from Analysis.fetchpgn import *
from Analysis.userinfo import *
from GUI.gui_main import Main

parser = argparse.ArgumentParser()
parser.add_argument("-u", "--username", help="enter your Chess.com username", type=str, required=True)
# parser.add_argument("-g", "--game", help="enter the game to select", type=int, required=True)
args = parser.parse_args()

print("\n----------Rating Stats of {user}----------".format(user=args.username))
ratings = get_player_rating(args.username)

print("Enter number of games to display [MAX = 5]: ", end='')
games = int(input())
print('')

time_control = fetchpgn(args.username, games)

PGN = PGN_analyzer("games.pgn")
moves_list = PGN.moves_list

result = PGN.analyze_all_moves()
adv = PGN.adv

rating_dict = {
    "blitz": 0,
    "rapid": 1,
    "bullet": 2
}

main = Main(args.username, ratings[rating_dict[time_control]], moves_list)
main.mainloop(result, adv)
