import os
import requests
from datetime import date

#fetches 3 pgn of the latest 3 games played
def fetchpgn(user, i,where=""):
    print("Downloading %s's last 3 games to %s:" % (user, where))
    archives = get('https://api.chess.com/pub/player/%s/games/archives' % user)['archives']
    latest_archives = archives[-1:]  # Retrieve the last archive

    for idx, archive in enumerate(latest_archives, 1):
        games = get(archive)['games']
        latest_game = games[-i]  # Retrieve the last game (latest)

        d = date.fromtimestamp(latest_game['end_time'])
        y = d.year
        m = d.month
        filename = os.path.join(where, "games.pgn")
        print('Starting work on %s...' % filename)

        with open(filename, 'w', encoding='utf-8') as output:
            print(latest_game['pgn'], file=output)

def get(url):
    return requests.get(url).json()

if __name__ == '__main__':
    # import argparse
    # parser = argparse.ArgumentParser(description="Download a user's games from chess.com")
    # parser.add_argument('user', metavar='USER', help='The user whose games we want')
    # parser.add_argument('where', metavar='PATH', help='Where to create the PGN files',
    #                     default=".", nargs='?')
    # args = parser.parse_args()
    fetchpgn("ThermalDust095")
