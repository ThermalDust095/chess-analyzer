# Define the 'Square' class to represent a cell on the chessboard.
class Square:
    def __init__(self,row,col,piece=None) -> None:
         # Initialize the square with its row, column, and an optional 'piece' object.
        self.row=row
        self.col=col
        self.piece=piece
    def has_piece(self):
        # Check if the square has a piece. If it does, return True; otherwise, return False.   
        return self.piece!=None 