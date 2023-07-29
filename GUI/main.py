import pygame
import sys
from pygame.locals import *
from game import *
from const import *

sys.path.insert(0,r"C:\Users\akhil\OneDrive - dsatm.edu.in\Documents\Akhil\Python\chess-python-project\chess-python-project\Analysis")

from analyser import *
from Decoder import decode

PGN = PGN_analyzer("games.pgn")
moves_list = PGN.moves_list

class Main:
    def __init__(self) -> None:
        pygame.init()
        self.moves = decode(moves_list)
        self.move = -1
        self.screen=pygame.display.set_mode((1000,700))
        pygame.display.set_caption('Chess')
        # Create a new 'Game' object to represent the chess game.
        self.game=Game()
        # Main game loop to handle events and update the screen.
    def mainloop(self):
        # Alias the 'Game' and 'screen' objects for convenience.
        game=self.game
        screen=self.screen
        while True:# Enter the game loop.
            # Show the background of the chessboard.
            game.show_bg(screen)
            # Show the pieces on the chessboard.
            game.show_pieces(screen) 
            # Event handling loop to process user inputs.   
            for event in pygame.event.get():
                # Check if the user closed the game window.
                if event.type == pygame.QUIT:
                    # Exit the game loop and close the program.
                    sys.exit()
                
                if event.type == KEYDOWN:
                    if event.key == K_RIGHT:
                        if self.move != len(self.moves)-1 :
                            self.move += 1
                            self.game.board.move_piece(self.moves[self.move])

            # Update the display to show any changes.
            pygame.display.update()
# Create an instance of the 'Main' class and start the game loop.
main=Main()
main.mainloop()
