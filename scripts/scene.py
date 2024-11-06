from scripts.dialogue import Dialogue
import pygame

from scripts.utils import HEIGHT, WIDTH


class Scene:
    def __init__(self, game, dialogue: Dialogue, background=None, next=None, prev=None):
        self.game = game
        self.dialogue = dialogue
        self.background = background
        if self.background is not None:
            self.background = self.game.assets[background]
        self.next = next
        self.prev = prev
        self.text = True
        self.surface = pygame.Surface((1280,720))
        self.update_renderables()
        
    def next_text(self):
        self.dialogue.next_text()
        
        
        
    def update_renderables(self):
        if self.background is not None:
            self.surface.blit(self.background, (0,0))
        self.surface.blit(self.dialogue.getSurface(), (0, int(2*HEIGHT/3)-240))
        if self.text:
            text_surface = pygame.Surface((WIDTH, HEIGHT/3))
            text_surface.fill((255,255,255))
            self.dialogue.updateSurface()
            text_surface.set_alpha(100)
            self.surface.blit(text_surface, (0,2*HEIGHT/3))
            
    def text_segment_done(self):
        return self.dialogue.text_done()
    
    def get_surface(self):
        return self.surface