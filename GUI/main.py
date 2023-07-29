# Import necessary libraries and modules.
import pygame
import sys
from const import *
from game import Game
# Define the 'Main' class to manage the chess game.
class Main:
    def __init__(self) -> None:
        # Initialize the pygame library.
        pygame.init()
         # Create the game window with the specified width and height.
        self.screen=pygame.display.set_mode((width,height))
        # Set the title of the game window.
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

            # Update the display to show any changes.
            pygame.display.update()
# Create an instance of the 'Main' class and start the game loop.
main=Main()
main.mainloop()
