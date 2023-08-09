# Import necessary classes and constants from other modules.
import os


# Define a base class 'Piece' to represent chess pieces.
class Piece:
    def __init__(self, name, color, value, texture=None, texture_rect=None) -> None:
        self.name = name
        self.color = color
        value_sign = 1 if color == 'white' else -1
        # Assign a positive value for white pieces and negative value for black pieces.
        self.value = value * value_sign
        # List to store possible moves for the piece.
        self.moves = []
        # A flag to track if the piece has been moved during the game.
        self.texture = texture
        self.moved = False
        self.texture = texture
        # Set the texture path for the piece image based on its color and name.
        self.set_texture()
        self.texture_rect = texture_rect

    def set_texture(self, size=80):
        # Function to set the texture path based on the piece's color and name.
        self.texture = os.path.join(
            f'assets/images/imgs-{size}px/{self.color}_{self.name}.png')
        # Function to add possible moves to the piece's move list.

    def add_moves(self, moves):
        self.moves.append(moves)


# Create specific chess piece classes, inheriting from the 'Piece' class.
# inheritence-child_class(parent_class):

# Pawn: 1 point (or pawn)
class Pawn(Piece):
    def __init__(self, color, ) -> None:
        self.dir = -1 if color == 'white' else 1

        super().__init__('pawn', color, 1.0)


# Knight: 3 points.
class Knight(Piece):
    def __init__(self, color) -> None:
        super().__init__('knight', color, 3.0)


# Bishop: 3 points.
# both bishop and Knight have same value but bishop is slightly more important than knight
class Bishop(Piece):
    def __init__(self, color) -> None:
        super().__init__('bishop', color, 3.001)


# Rook: 5 points.
class Rook(Piece):
    def __init__(self, color) -> None:
        super().__init__('rook', color, 5.0)


# Queen: 9 points.
class Queen(Piece):
    def __init__(self, color) -> None:
        super().__init__('queen', color, 9.0)


# King has high value in chess so, more points
class King(Piece):
    def __init__(self, color) -> None:
        super().__init__('king', color, 10000.0)
