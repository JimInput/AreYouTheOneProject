from scripts.dialogue import Dialogue
import pygame

from scripts.utils import HEIGHT


class Scene:
    def __init__(self, game, dialogue: Dialogue, background=None, next=None, prev=None):
        self.game = game
        self.dialogue = dialogue
        self.background = self.game.assets[background]
        self.next = next
        self.prev = prev
        self.surface = pygame.Surface((1280,720))
        self.update_renderables()
        
        
    def update_renderables(self):
        self.surface.blit(self.background, (0,0))
        self.surface.blit(self.dialogue.getSurface(), (0, int(2*HEIGHT/3)))
        
    def get_surface(self):
        return self.surface