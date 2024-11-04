import math
import sys
import random
import os

import pygame
from scripts.dialogue import Dialogue
from scripts.portrait import Emotion, Portrait
from scripts.scene import Scene
from scripts.scene_manager import SceneManager

from scripts.utils import HEIGHT, WIDTH, load_image, load_images
# from scripts.entities import PhysicsEntity, Player, Enemy
# from scripts.sparks import Spark
# from scripts.tilemap import Tilemap
# from scripts.clouds import Clouds
# from scripts.particle import Particle
# from scripts.text import Text


class Game:
    def __init__(self):
        pygame.init()
        pygame.font.init()

        pygame.display.set_caption('Are you the one?')
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)

        self.clock = pygame.time.Clock()

        self.assets = {
            'mudkip': load_images('portraits/mudkip', (67,67)),
            'frame': load_images('frames', (80,80)),
            'field': load_image('backgrounds/field_background.png', (1280,720)),
            # 'grass': load_images('tiles/grass'),
        }

        # import sfx
        self.sfx = {
            # 'jump': pygame.mixer.Sound('data/sfx/jump.wav'),
        }
        # self.sfx['ambience'].set_volume(0.2)
        
        self.test_scene = Scene(self, Dialogue(portrait1=Portrait(self, 'mudkip', 0), portrait2=Portrait(self, 'mudkip', 0)), 'field')
        
        self.test_scene_manager = SceneManager(self.test_scene)


    def run(self):
        # load music
        # pygame.mixer.music.load('data/music.wav')
        # pygame.mixer.music.set_volume(0.5)
        # pygame.mixer.music.play(-1)

        # self.sfx['ambience'].play(-1)

        while True:
            self.screen.fill((255,255,0))
            
            L = []
            for emo in Emotion:
                L.append(emo)
                

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    if event.key == pygame.K_a:
                        self.test_scene_manager.next_scene()
                if event.type == pygame.KEYUP:
                    pass
                
            self.screen.blit(self.test_scene_manager.get_surface(), (0,0))
            
            # self.screen.blit(portrait2.getPortraitWithFrame(L[other_portrait]), (250,250))

            pygame.display.update()
            self.clock.tick(60)


Game().run()
