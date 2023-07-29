# Import necessary classes and constants from other modules.
from square import Square
from const import *
from piece import *
# Define the 'Board' class to represent the chessboard and initialize it.
class Board:
    def __init__(self) -> None:
         #adding a list of 8 zeros to each column
         self.squares=[[0,0,0,0,0,0,0,0]for col in range(cols)] 
         # Call the '_create()' method to populate the grid with 'Square' objects.
         self._create()
          # Add chess pieces to the board for both 'white' and 'black' players.
         self._add_pieces('white')
         self._add_pieces('black')

    #_before method represent that the method is private
    def _create(self):
        #traversal
        for row in range(rows):
            for col in range(cols):
                 self.squares[row][col]=Square(row,col)
    #method to add pieces
    def _add_pieces(self,color):
        # Determine the starting row for pawns and other pieces based on the color.
       row_pawn,row_other=(6,7)if color=='white'else(1,0)

      #pawns
       for col in range(cols):
           self.squares[row_pawn][col]=Square(row_pawn,col,Pawn(color))
    
      #knights
       self.squares[row_other][1]=Square(row_other,1,Knight(color))
       self.squares[row_other][6]=Square(row_other,6,Knight(color))
    
      #Bishops
       self.squares[row_other][2]=Square(row_other,2,Bishop(color))
       self.squares[row_other][5]=Square(row_other,5,Bishop(color))
      #Rooks
       self.squares[row_other][0]=Square(row_other,0,Rook(color))
       self.squares[row_other][7]=Square(row_other,7,Rook(color))
       #Queen
       self.squares[row_other][3]=Square(row_other,3,Queen(color))
       
       #King
       self.squares[row_other][4]=Square(row_other,4,King(color))

    def move_piece(self,move_list):
        sq1c,sq1r,sq2c,sq2r = move_list[0],move_list[1],move_list[2],move_list[3]
        self.squares[sq2r][sq2c].piece , self.squares[sq1r][sq1c].piece = self.squares[sq1r][sq1c].piece , None




    

    


