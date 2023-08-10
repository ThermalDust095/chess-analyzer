import chess.pgn
import multiprocessing
from stockfish import Stockfish

cores = multiprocessing.cpu_count()

stockfish = Stockfish(path="stockfish", depth=18, parameters={"Threads": cores})


class PGN_analyzer:
    def __init__(self, path):
        self.res = None
        self.moves_list = self.pgn_to_moves(path)
        self.adv = []

    def pgn_to_moves(self, pgn_file_path):
        moves_list = []

        with open(pgn_file_path) as pgn_file:
            while True:
                game = chess.pgn.read_game(pgn_file)
                if game is None:
                    break
                moves = [move.uci() for move in game.mainline_moves()]
                moves_list.append(moves)
            self.moves_list = moves_list[0]

        return self.moves_list

    def analyze_move(self, move: str):
        index = self.moves_list.index(move)
        moves = self.moves_list[:index + 1]
        stockfish.set_position(moves)
        pos = Move()
        pos.best_move = stockfish.get_best_move()
        pos.board_visual = stockfish.get_board_visual()
        pos.top_moves = stockfish.get_top_moves(5)
        pos.wdl = stockfish.get_wdl_stats()
        return pos

    def analyze_all_moves(self):
        moves = []
        res = {}
        stockfish.set_position(moves)
        x = 0

        print("Starting Analysis...")

        for idx, move in enumerate(self.moves_list):
            a = {"top_moves": stockfish.get_top_moves(2)}
            moves.append(move)
            stockfish.set_position(moves)
            a["eval"] = stockfish.get_evaluation()
            x += a["eval"]["value"]
            self.adv.append(x)
            res[move] = a

            if idx % 2 == 0:
                print(f"Move {idx // 2 + 1}(White) Analyzed")

            if idx % 2 == 1:
                print(f"Move {idx // 2 + 1}(Black) Analyzed")

        self.res = res
        return res


class Move:
    def __init__(self):
        self.best_move = 0
        self.board_visual = 0
        self.wdl = 0
        self.top_moves = 0


if __name__ == "__main__":
    a = PGN_analyzer("game.pgn")
    a.analyze_all_moves()
    print(a.res)
    print(a.adv)
