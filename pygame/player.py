import pygame
from utility import image_cutter

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = 100
        self.y = 100
        self.spritesheet = pygame.image.load("64X128_Walking_Free.png").convert_alpha()
        self.image = image_cutter(self.spritesheet, 0, 0, 64, 128, 1)
        self.rect = self.image.get_rect(midbottom=(self.x, self.y))
        self.index = 0
        self.speed = 5
        self.lives = 3
        self.invul = False

    def animation(self, direction):
        frame_count = 3

        self.index += 0.1

        if self.index >= frame_count:
            self.index = 0

        self.image = image_cutter(self.spritesheet, int(self.index), direction, 64, 128, 1)

    def update(self):
        key = pygame.key.get_pressed()

        if key[pygame.K_w]:
            self.animation(3)
            self.rect.move_ip(0, -self.speed)
        if key[pygame.K_s]:
            self.animation(0)
            self.rect.move_ip(0, +self.speed)
        if key[pygame.K_a]:
            self.animation(1)
            self.rect.move_ip(-self.speed, 0)
        if key[pygame.K_d]:
            self.animation(2)
            self.rect.move_ip(+self.speed, 0)

    def draw(self, screen):
        screen.blit(self.image, self.rect)