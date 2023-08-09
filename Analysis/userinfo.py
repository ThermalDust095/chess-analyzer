from chessdotcom import get_leaderboards, get_player_stats, get_player_game_archives
import pprint
import requests
from tabulate import tabulate

printer = pprint.PrettyPrinter()


def print_leaderboards():
    data = get_leaderboards().json
    print(data)
    categories = data.keys()

    for category in categories:
        print('Category:', category)
        for idx, entry in enumerate(data[category]):
            print(f'Rank: {idx + 1} | Username: {entry["username"]} | Rating: {entry["score"]}')


def get_player_rating(user):
    data = get_player_stats(user).json
    categories = ['chess_blitz', 'chess_rapid', 'chess_bullet']

    best = []
    current = []

    for category in categories:
        # print('Category:', category)
        best.append(data["stats"][category]["best"]["rating"])
        current.append(data["stats"][category]["last"]["rating"])

        # print(f'Current: {data["stats"][category]["last"]["rating"]}')
        # print(f'Best: {data["stats"][category]["best"]["rating"]}')
        # print(f'Best: {data["stats"][category]["record"]}')

    head = ["Category", "Best", "Current"]
    cat = ["Blitz", "Rapid", "Bullet"]
    mydata = []
    new = []

    for i in range(3):
        new.append(cat[i])
        new.append(best[i])
        new.append(current[i])
        mydata.append(new)
        new = []

    print(tabulate(mydata, headers=head, tablefmt='grid'))
    return best


def get_most_recent_game(user, i):
    data = get_player_game_archives(user).json
    print("raw data:", data, "\n\n\n\n\n")
    url = data['archives'][-i]
    games = requests.get(url).json()
    game = games['games'][-i]
    printer.pprint(game)


if __name__ == "__main__":
    username = input("Enter username:")
    get_player_rating(username)
    get_most_recent_game(username, 0)
