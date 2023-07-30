from chessdotcom import get_leaderboards, get_player_stats, get_player_game_archives
import pprint
import requests

printer = pprint.PrettyPrinter()
def print_leaderboards():
	data = get_leaderboards().json
	print(data)
	categories = data.keys()

	for category in categories:
		print('Category:', category)
		for idx, entry in enumerate(data[category]):
			print(f'Rank: {idx + 1} | Username: {entry["username"]} | Rating: {entry["score"]}')


def get_player_rating(username):
	data = get_player_stats(username).json
	categories = ['chess_blitz', 'chess_rapid', 'chess_bullet']
	for category in categories:
		print('Category:', category)
		print(f'Current: {data["stats"][category]["last"]["rating"]}')
		print(f'Best: {data["stats"][category]["best"]["rating"]}')
		print(f'Best: {data["stats"][category]["record"]}')

def get_most_recent_game(username,i):
	data = get_player_game_archives(username).json
	url = data['archives'][-i]
	games = requests.get(url).json()
	game = games['games'][-i]
	printer.pprint(game)


if __name__ == "__main__":
	username = input("Enter username:")
	get_player_rating(username)
	get_most_recent_game(username)