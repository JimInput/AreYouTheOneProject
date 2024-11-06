import pygame
from scripts.portrait import Emotion, Portrait
from scripts.text import Text

from scripts.utils import HEIGHT, WIDTH

class Dialogue:
    def __init__(self, portrait1: Portrait, portrait2: Portrait, text: Text):
        self.portrait1 = portrait1
        self.portrait2 = portrait2
        self.text = text
        self.portrait_surface = pygame.Surface((WIDTH, HEIGHT/3))
        self.text_surface = pygame.Surface((WIDTH, HEIGHT/3))
        self.updateSurface()
        
    def next_text(self):
        self.text.next_text()
        
    def text_done(self):
        return self.text.text_done()
        
    
    def updateSurface(self):
        self.portrait_surface.blit(self.portrait1.getPortraitWithFrame(Emotion.ANGRY), (10,0))
        self.portrait_surface.blit(pygame.transform.flip(self.portrait2.getPortraitWithFrame(Emotion.ECSTATIC), 1, 0), (WIDTH-250, 0))
        self.text.updateText()
        self.text_surface.blit(self.text.getSurface(), (0, 0))
        #update text
        
    def getSurface(self):
        grouped_surface = pygame.Surface((WIDTH, 2*HEIGHT/3))
        grouped_surface.set_colorkey((0,0,0))
        grouped_surface.blit(self.portrait_surface, (0,0))
        grouped_surface.blit(self.text_surface, (0, HEIGHT/3))
        return grouped_surface