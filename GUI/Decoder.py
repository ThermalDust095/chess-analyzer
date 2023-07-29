def decode(moves_list):
    chess_notation = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7}
    moves = []
    for move in moves_list:
        a = []

        for i in move:
            if i in chess_notation:
                a.append(chess_notation[i])
            else:
                a.append(8 - int(i))

        
        moves.append(a)
    
    return moves


if __name__ == "__main__":
    decode(["e1c1"])

