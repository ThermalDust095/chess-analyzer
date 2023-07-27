from stockfish import Stockfish
import chess.pgn
import sys

stockfish = Stockfish(path="stockfish",depth=18)

class PGN_analyzer:
    def __init__(self,path="games.pgn"):
        self.moves_list = self.pgn_to_moves(path)

    def pgn_to_moves(self,pgn_file_path):
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
    
    def analyze_move(self,move:str):
        index = self.moves_list.index(move)
        moves = self.moves_list[:index+1]
        stockfish.set_position(moves)
        pos = Move()
        pos.best_move = stockfish.get_best_move()
        pos.board_visual = stockfish.get_board_visual()
        pos.top_moves = stockfish.get_top_moves(5)
        pos.wdl = stockfish.get_wdl_stats()
        return pos
    
    def analyze_all_moves(self):
        moves = []
        stockfish.set_position(moves)
        for move in self.moves_list:
            stockfish.make_moves_from_current_position(moves.append(move))
            print(stockfish.get_best_move())
            print(stockfish.get_board_visual())
            print(stockfish.get_top_moves(5))
            print(stockfish.get_wdl_stats())


class Move:
    def __init__(self):
        self.best_move = 0
        self.board_visual = 0
        self.wdl= 0
        self.top_moves = 0

a = 'hi'

if __name__ == "__main__":
    path = sys.argv[1]
    a = PGN_analyzer(path=path)
    a.analyze_all_moves()
