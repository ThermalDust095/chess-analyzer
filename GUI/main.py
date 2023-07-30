import pygame
import sys
from pygame.locals import *
from game import *
from const import *
from objects import *

sys.path.insert(0,r"C:\Users\akhil\OneDrive - dsatm.edu.in\Documents\Akhil\Python\chess-python-project\chess-python-project\Analysis")

from analyser import *
from Decoder import decode

class Main:
    def __init__(self,username:str,Rating,moves_list) -> None:
        pygame.init()
        self.moves_list = moves_list
        self.moves = decode(moves_list)
        self.move = -1
        self.screen=pygame.display.set_mode((1360,768))
        pygame.display.set_caption('Chess Analysis')

        #Trivial
        self.username = username
        self.Rating = Rating
        
        self.game=Game(100,50)

        #Trivial Settings
        mediumText = pygame.font.Font(None, 32)
        littleText = pygame.font.Font(None, 16)
        bigText = pygame.font.Font(None, 48)
        green = (234,235,200)
        white = (0,0,0)


        self.username = Label(f"{username}   ||   Best Rating: {self.Rating}",bigText,(40,35),(0,0,0))
        self.instru1 = Label("'Right Arrow Key' for Next Move & 'R' key for Refresh",mediumText, (70,720) ,(0,0,0))
        self.your_move = Button((750,100),(500,200),mediumText,green,white)
        self.graph = Graph()

    #trivial functions
    def check_move(self,moves_list,move,result):
        if move == -1:
            self.original_move = "Start"
            self.best_move_one,self.best_move_two,self.best_move_three,self.advantage,self.move_name = "","","","",""
            
        if move != -1:
            self.original_move =  f"Original Move:   {moves_list[move]}"
            self.advantage = f"Advantage: {result[moves_list[move]]['eval']['value']}"

            try:
                self.best_move_one = f"Best Move: {result[moves_list[move]]['top_moves'][0]['Move']}     ||     Advantage: {result[moves_list[move]]['top_moves'][0]['Centipawn']}"
                self.best_move_two = f"Best Move: {result[moves_list[move]]['top_moves'][1]['Move']}      ||     Advantage: {result[moves_list[move]]['top_moves'][1]['Centipawn']}"

            except:
                self.best_move_one,self.best_move_two,self.best_move_three,self.advantage,self.move_name = "","","","",""

            if move%2 == 0:
                self.move_name = f"Move{move//2 + 1} (White)"
            
            if move%2 == 1:
                self.move_name = f"Move{move//2 + 1} (Black)"


    def mainloop(self,result,adv):
        self.check_move(self.moves_list,self.move,result)
        game=self.game
        screen=self.screen

        plot_surface = self.graph.draw_graph(adv[:0])
        while True:
            # Show the background of the chessboard.
            screen.fill((255,255,255))
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
                            self.check_move(self.moves_list,self.move,result)
                            plot_surface = self.graph.draw_graph(adv[:self.move+1])
                            

                    if event.key == K_r:
                        self.move = -1
                        self.game.board.set_original_state()
                        self.check_move(self.moves_list,self.move,result)
                        plot_surface = self.graph.draw_graph(adv[:0])

            move_name = Label(self.move_name,pygame.font.Font(None, 48),(760,50),(0,0,0))
            advantage = Label(self.advantage,pygame.font.Font(None, 32),(1000,110),(0,0,0))
            best_moves = Label(f"Best Moves ",pygame.font.Font(None, 32),(900,160),(0,0,0))
            best_move_one = Label(self.best_move_one,pygame.font.Font(None, 32),(760,200),(0,0,0))
            best_move_two = Label(self.best_move_two,pygame.font.Font(None, 32),(760,230),(0,0,0))

            #Rendering Objects
            move_name.draw_render(screen)
            self.your_move.draw_render(screen,self.original_move)
            self.username.draw_render(screen)
            self.instru1.draw_render(screen)
            best_moves.draw_render(screen)
            best_move_one.draw_render(screen)
            advantage.draw_render(screen)
            best_move_two.draw_render(screen)


            screen.blit(plot_surface, (670, 260))

            # Update the display to show any changes.
            pygame.display.update()





# Main
PGN = PGN_analyzer("games.pgn")
moves_list = PGN.moves_list
result = PGN.analyze_all_moves()
adv = PGN.adv

main=Main("ThermalDust095",974,moves_list)
main.mainloop(result,adv)