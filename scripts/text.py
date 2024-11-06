import pygame
from scripts.utils import HEIGHT, WIDTH

class Text:
    def __init__(self, person1First, person1Name, person2Name, L):
        self.person1Turn = person1First
        self.person1Name = person1Name
        self.person2Name = person2Name
        self.text_list = L
        self.surface = pygame.Surface((WIDTH, HEIGHT/3))
        self.name_font = pygame.font.SysFont('Arial', 54)
        self.font = pygame.font.SysFont('Arial', 32)
        self.text_idx = 0
        self.idx = 0
        self.currentText = L[self.text_idx][0]
        self.frames = 0
        
    def updateText(self):
        # self.surface.fill((0,0,0))
        if self.person1Turn:
            name = self.name_font.render(self.person1Name, 0, (1, 0, 0))
            self.surface.blit(name, (0,0))
        else:
            name = self.name_font.render(self.person2Name, 0, (1, 0, 0))
            self.surface.blit(name, (WIDTH-name.get_width(), 0))
        if self.frames == 3 and self.text_idx < len(self.text_list[self.text_idx]):
            self.currentText = self.text_list[self.text_idx][:self.idx+1]
            words = self.font.render(self.currentText, 0, (1, 0, 0))
            if self.person1Turn: self.surface.blit(words, (0, 100))
            else:
                self.surface.fill((0,0,0)) 
                self.surface.blit(words, (WIDTH-words.get_width(), 100))
            if self.idx+1 < len(self.text_list[self.text_idx]):
                self.idx += 1
        self.frames = (self.frames + 1) % 4
        
    def next_text(self):
        if self.text_done():
            self.person1Turn = not self.person1Turn
            self.surface.fill((0,0,0))
            self.idx = 0
            if self.text_idx + 1 < len(self.text_list):
                self.text_idx += 1
            
    def text_done(self):
        return self.idx == len(self.text_list[self.text_idx]) - 1
            
        
    def getSurface(self):
        return self.surface
        
    