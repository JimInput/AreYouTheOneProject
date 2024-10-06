import math
import sys
import random
import os

import pygame
from scripts.portrait import Emotion, Portrait

from scripts.utils import load_image, load_images, Animation
from scripts.utils import PORTRAIT_SCALE
# from scripts.entities import PhysicsEntity, Player, Enemy
# from scripts.sparks import Spark
# from scripts.tilemap import Tilemap
# from scripts.clouds import Clouds
# from scripts.particle import Particle
# from scripts.text import Text


class Game:
    def __init__(self):
        pygame.init()

        pygame.display.set_caption('ninja game')
        self.screen = pygame.display.set_mode((1000, 750), pygame.RESIZABLE)

        self.clock = pygame.time.Clock()

        self.assets = {
            'mudkip': load_images('portraits/mudkip', PORTRAIT_SCALE),
            'frames': load_images('frames', (240,240))
            # 'grass': load_images('tiles/grass'),
            # 'large_decor': load_images('tiles/large_decor'),
            # 'stone': load_images('tiles/stone'),
            # 'player': load_image('entities/player.png'),
            # 'background': load_image('background.png'),
            # 'clouds': load_images('clouds'),
            # 'enemy/idle': Animation(load_images('entities/enemy/idle'), img_dur=6),
            # 'enemy/run': Animation(load_images('entities/enemy/run'), img_dur=4),
            # 'player/idle': Animation(load_images('entities/player/idle'), img_dur=6),
            # 'player/run': Animation(load_images('entities/player/run'), img_dur=4),
            # 'player/jump': Animation(load_images('entities/player/jump')),
            # 'player/slide': Animation(load_images('entities/player/slide')),
            # 'player/wall_slide': Animation(load_images('entities/player/wall_slide')),
            # 'particle/leaf': Animation(load_images('particles/leaf'), img_dur=20, loop=False),
            # 'particle/particle': Animation(load_images('particles/particle'), img_dur=6, loop=False),
            # 'gun': load_image('gun.png'),
            # 'projectile': load_image('projectile.png')
        }

        # import sfx
        self.sfx = {
            # 'jump': pygame.mixer.Sound('data/sfx/jump.wav'),
            # 'dash': pygame.mixer.Sound('data/sfx/dash.wav'),
            # 'hit': pygame.mixer.Sound('data/sfx/hit.wav'),
            # 'shoot': pygame.mixer.Sound('data/sfx/shoot.wav'),
            # 'ambience': pygame.mixer.Sound('data/sfx/ambience.wav'),
        }

        # set sfx volume
        
        # self.sfx['ambience'].set_volume(0.2)
        # self.sfx['shoot'].set_volume(0.4)
        # self.sfx['hit'].set_volume(0.8)
        # self.sfx['dash'].set_volume(0.3)
        # self.sfx['jump'].set_volume(0.7)


    def run(self):
        # load music
        # pygame.mixer.music.load('data/music.wav')
        # pygame.mixer.music.set_volume(0.5)
        # pygame.mixer.music.play(-1)

        # self.sfx['ambience'].play(-1)
        current_portrait = 0
        other_portrait = 5

        while True:
            self.screen.fill((255,255,0))
            
            portrait = Portrait(self.assets["mudkip"], self.assets["frames"][0])
            portrait2 = Portrait(self.assets["mudkip"], self.assets["frames"][1])
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
                        current_portrait = (current_portrait + 1) % 13
                        other_portrait = (other_portrait + 1) % 13
                if event.type == pygame.KEYUP:
                    pass
            for i in range(0, 3):
                self.screen.blit(portrait.getPortraitWithFrame(L[current_portrait]), (0,250*i))
            
            # self.screen.blit(portrait2.getPortraitWithFrame(L[other_portrait]), (250,250))

            pygame.display.update()
            self.clock.tick(60)


Game().run()
