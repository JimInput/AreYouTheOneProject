import pygame
from scripts.portrait import Emotion, Portrait

from scripts.utils import HEIGHT, WIDTH

class Dialogue:
    def __init__(self, portrait1: Portrait, portrait2: Portrait):
        self.portrait1 = portrait1
        self.portrait2 = portrait2
        self.surface = pygame.Surface((WIDTH, HEIGHT/3))
        self.updateSurface()
    
    def updateSurface(self):
        self.surface.fill((0,0,0))
        self.surface.set_alpha(167)
        self.surface.blit(self.portrait1.getPortraitWithFrame(Emotion.DIZZY), (0,0))
        
    def getSurface(self):
        return self.surface