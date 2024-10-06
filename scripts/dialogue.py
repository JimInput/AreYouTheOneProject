import pygame
from scripts.portrait import Emotion, Portrait

from scripts.utils import HEIGHT, WIDTH

class Dialogue:
    def __init__(self, string: str, font: str, font_size: int, portrait1: Portrait, portrait2: Portrait):
        self.string = string
        self.font_size = font_size
        self.portrait1 = portrait1
        self.portrait2 = portrait2
        self.font = pygame.font.SysFont(font, font_size)
        self.surface = pygame.Surface((WIDTH, HEIGHT - 250))
    
    def getSurface(self):
        self.surface.blit(self.portrait1.getPortraitWithFrame(Emotion.NEUTRAL), (0,0))
        self.surface.blit(pygame.transform.flip(self.portrait2.getPortraitWithFrame(Emotion.DIZZY), 1, 0), (WIDTH-240, 0))
        self.surface.blit(self.font.render(self.string, False, (255,255,255)), (0, 250))
        return self.surface
        
    
    def getPortraits(self):
        return self.portrait1, self.portrait2