import pygame
import sys
from const import *
from pygame.locals import *
from game import Game
from Decoder import decode

moves_list = ['d2d4', 'b8c6', 'f2f4', 'g8f6', 'e2e3', 'd7d5', 'g2g3', 'c8g4', 'f1e2', 'g4e2', 'd1e2', 'f6e4', 'e2f3', 'c6b4', 'c2c3', 'b4c2', 'e1e2', 'c2a1', 'e2f1', 'e7e6', 'f3d1', 'f8d6', 'g1h3', 'e8g8', 'f1g2', 'h7h6', 'd1f1', 'b7b6', 'f1e2', 'c7c5', 'b2b3', 'c5d4', 'e3d4', 'e4f6', 'c1b2', 'a1b3', 'a2b3', 'a7a5', 'h3f2', 'a5a4', 'b3b4', 'a4a3', 'b1a3', 'f6e4', 'f2e4', 'd5e4', 'e2e4', 'd8g5', 'f4g5', 'h6g5']

class Main:
    def __init__(self) -> None:
        pygame.init()
        self.moves = decode(moves_list)
        self.move = 0
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
                    if self.move != len(self.moves)-1 :
                        print(event.type)
                        self.game.board.move_piece(self.moves[self.move])
                        self.move += 1

            # Update the display to show any changes.
            pygame.display.update()
# Create an instance of the 'Main' class and start the game loop.
main=Main()
main.mainloop()
