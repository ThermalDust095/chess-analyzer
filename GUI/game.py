# Import necessary libraries and modules.
import pygame
from const import *
from board import Board
# Define the 'Game' class to represent the chess game.
class Game:
    def __init__(self,top,left) -> None:
        # Create a new 'Board' object to represent the chessboard.
        self.board=Board()
        self.top = top
        self.left = left
        # Method to display the background of the chessboard on the given surface.
    def show_bg(self,surface):
        for row in range(rows):
            for col in range(cols):
                if(row+col)%2==0:
                    #light green
                    color=(234,235,200)
                else:
                    #dark green
                    color=(119,154,88)
                # Calculate the rectangle position and size for the current square. 
                rect=(col*sqsize+self.left,row*sqsize+self.top,sqsize,sqsize)

                # Draw the square on the surface with the specified color.
                pygame.draw.rect(surface,color,rect)
    
    def show_pieces(self,surface):
        for row in range(rows):
            for col in range(cols):
                #check piece on a specific block
                 if self.board.squares[row][col].has_piece():
                  #if the piece is present in the block save in into a variable
                  piece=self.board.squares[row][col].piece
                  #taking an image
                  img=pygame.image.load(piece.texture)
                  # Calculate the center position of the square.
                  img_center=col * sqsize + sqsize // 2 + self.left, row * sqsize+ sqsize // 2 + self.top
                  # Get the rectangle that will center the image on the square.
                  piece.texture_rect=img.get_rect(center=img_center)
                  # Blit the image onto the surface at the specified 'texture_rect' position.
                  #In the provided code, the term "blit" stands for "Block Transfer." 
                  # It is a term commonly used in the context of graphics and graphical operations.
                  # Specifically, in the Pygame library, the blit function is used to copy the contents of 
                  # one surface (e.g., an image) onto another surface (e.g., the game window's surface).
                  surface.blit(img,piece.texture_rect)
    