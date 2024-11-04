from enum import Enum
import pygame


class Emotion(Enum):
    NEUTRAL = 0
    HAPPY = 1
    EXCITED = 2
    ECSTATIC = 3
    ANGRY = 4
    PISSED = 5
    SAD = 6
    HURT = 7
    TEARS = 8
    WAILING = 9
    WORRIED = 10
    DIZZY = 11
    SHOCKED = 12
    
class Gender(Enum):
    MALE = 0
    FEMALE = 1
    
class Portrait():
    def __init__(self, game, name, frame=None):
        self.game = game
        self.name = name
        self.frame = frame
        self.images = game.assets[name]
        self.frame = game.assets['frame'][frame]
        
    def getPortrait(self, emo: Emotion):
        return self.images[emo.value]
    
    def getPortraitWithFrame(self, emo: Emotion):
        surface = pygame.Surface((240, 240), pygame.SRCALPHA, 32)
        surface.blit(self.getPortrait(emo), (20,20))
        if self.frame is not None:
            surface.blit(self.frame, (0,0))
        surface.convert_alpha()
        return surface
        
            