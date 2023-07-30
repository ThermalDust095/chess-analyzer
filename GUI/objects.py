import pygame
import matplotlib.pyplot as plt
from pygame.locals import *
import numpy as np
import io

class InputBox:
    def __init__(self,size,pos):
        self.input = pygame.Rect(size,pos)
        self.active = False
        self.text = 'Hi'
    
    def key_listener(self,event,func):
        if event.type == KEYDOWN:
            if self.active == True:
                if event.key == K_RETURN:
                    func()
                    
                elif event.key == K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                
        
    def mouse_listener(self,event):
        if self.input.collidepoint(event.pos):
                self.active = True
    
    def draw_render(self,screen,color,font):
        pygame.draw.rect(screen, (0,0,0,0), self.input,border_radius=15)
        text_surface = font.render(self.text, True, color)
        screen.blit(text_surface, (self.input.x+20, self.input.y+5))


class Button:
    def __init__(self,size,pos,font,color,textcolor):
        self.button = pygame.Rect(size,pos)
        self.active = False
        self.font = font
        self.color = color
        self.textcolor = textcolor

    def mouse_listener(self,event,func):
        if self.button.collidepoint(event.pos):
                submit_active = True
                active = False
                func()
    
    def draw_render(self,screen,text):
        pygame.draw.rect(screen,self.color,self.button)
        submit_surface = self.font.render(text,True, self.textcolor)
        screen.blit(submit_surface, (self.button.x+9,self.button.y+10))


class Image:
    def __init__(self,file,pos):
        self.image = pygame.image.load(file)
        self.pos = pos

    def draw_render(self,screen):
        screen.blit(self.image, self.pos)
    

class Label:
    def __init__(self,text,font,pos,color):
        self.pos = pos
        self.font = font
        self.color = color
        self.text = text

    def draw_render(self,screen):
        self.text_surface = self.font.render(self.text, True, self.color)
        screen.blit(self.text_surface, self.pos)


class Graph:
    def get_alternating_color(self,index):
        if index % 2 == 0:
            return 'w'
        else:
            return 'b'
    
    def draw_graph(self,data_points):
        self.data_point = data_points
        plt.clf()
        background_color = (234/255, 235/255, 200/255, 1)
        scale_factor = 30
        # Set the positions of the bars
        positions = np.arange(len(data_points))
        # Set the colors for positive and negative bars
        colors = ['white' if value >= 0 else 'black' for value in data_points]
        # Create the figure and axis for the graph
        fig, ax = plt.subplots(figsize=(6.67, 5))
        # Draw the bars
        ax.bar(positions, data_points, color=colors)

        # Set the x-axis labels
        x_labels = ['M{}({})'.format(i // 2 + 1, self.get_alternating_color(i)) for i in range(len(data_points))]
        ax.set_xticks(positions)
        ax.set_xticklabels(x_labels, rotation=45 ,ha='right')
        # Set the y-axis label
        ax.set_ylabel('Centipawn')
        # Set the title
        ax.set_title('Advantage')
        # Set the background color of the plot area to match the window background
        ax.set_facecolor(background_color)
        # Save the plot to an in-memory buffer
        buffer = io.BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        # Convert the buffer to a Pygame surface
        plot_surface = pygame.image.load(buffer)

        # Close the Matplotlib plot to free up resources
        plt.close()

        return plot_surface

        



