import pygame
from utility import image_cutter
from settings import *

class Monster(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = 50
        self.y = 450
        self.speed = 5
        self.idle = pygame.image.load("Sprite-0001.png").convert_alpha()
        self.idle = pygame.transform.scale(self.idle, (self.idle.get_width()*6, self.idle.get_height()*6))
        self.run1 = pygame.image.load("monster-run1.png").convert_alpha()
        self.run1 = pygame.transform.scale(self.run1, (self.run1.get_width()*6, self.run1.get_height()*6))
        self.run2 = pygame.image.load("monster-run1.png").convert_alpha()
        self.run2 = pygame.transform.scale(self.run2, (self.run2.get_width()*6, self.run2.get_height()*6))
        self.images = [self.idle, self.run1, self.run2]
        self.index = 0
        self.surf = self.images[self.index]
        self.rect = self.surf.get_rect(midbottom=(self.x, self.y))

    def animation(self):
        self.index += 0.1
        if self.index > len(self.images):
            self.index = 0
        self.surf = self.images[int(self.index)]
    
    def update(self):
        self.rect.right += self.speed
        self.animation()
        if self.rect.right > SCREEN_WIDTH:
            self.speed = -self.speed
        elif self.rect.left < 0:
            self.speed = -self.speed

    def draw(self, screen):
        screen.blit(self.surf, self.rect)