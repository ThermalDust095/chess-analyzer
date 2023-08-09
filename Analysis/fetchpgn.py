import os
import requests
from datetime import date


# fetches 3 pgn of the latest 3 games played
def fetchpgn(user, i, where=""):
    print("Downloading %s's last %d games to %s:" % (user, i, where))
    archives = get('https://api.chess.com/pub/player/%s/games/archives' % user)['archives']
    latest_archives = archives[-1:]  # Retrieve the last archive

    for archive in latest_archives:
        games = get(archive)['games']
        for idx in range(i):
            print("Game {number}:".format(number=idx + 1))
            print("Time Control: {tc}".format(tc=games[-(idx + 1)]['time_class']))
            print("White: {player} ({result}) [{rating}]".format(player=games[-(idx + 1)]['white']['username'],
                                                                 result=games[-(idx + 1)]['white']['result'],
                                                                 rating=games[-(idx + 1)]['white']['rating']))
            print("Black: {player} ({result}) [{rating}]\n".format(player=games[-(idx + 1)]['black']['username'],
                                                                   result=games[-(idx + 1)]['black']['result'],
                                                                   rating=games[-(idx + 1)]['black']['rating']))

    choice = int(input("Choose game to analyse [Enter game number as displayed]: "))

    for archive in latest_archives:
        games = get(archive)['games']
        latest_game = games[-choice]  # Retrieve the last game (latest)

        d = date.fromtimestamp(latest_game['end_time'])
        y = d.year
        m = d.month

        filename = os.path.join(where, "games.pgn")
        print('Starting work on %s...' % filename)

        with open(filename, 'w', encoding='utf-8') as output:
            print(latest_game['pgn'], file=output)
            output.close()

        print("PGN Downloaded!\n")
        tc = games[-choice]['time_class']
    return tc


def get(url):
    return requests.get(url).json()


if __name__ == '__main__':
    # import argparse
    # parser = argparse.ArgumentParser(description="Download a user's games from chess.com")
    # parser.add_argument('user', metavar='USER', help='The user whose games we want')
    # parser.add_argument('where', metavar='PATH', help='Where to create the PGN files',
    #                     default=".", nargs='?')
    # args = parser.parse_args()
    fetchpgn("HarshMawandia", 2)
