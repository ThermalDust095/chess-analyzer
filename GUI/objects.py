import pygame
from pygame.locals import *

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

