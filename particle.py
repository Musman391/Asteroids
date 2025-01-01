import pygame

from circleshape import CircleShape
from constants import *


class Particle(pygame.sprite.Sprite):
    def __init__(self, groups, pos, color, direction, speed, screen):
        super().__init__(groups)
        self.pos = pos
        self.color = color
        self.direction = direction
        self.speed = speed

        self.create_surf(screen)

    def create_surf(self, screen):
        # self.image = pygame.Surface((4, 4)).convert_alpha()
        # self.image.set_colorkey("black")
        pygame.draw.circle(surface=screen, color=self.color, center=(2, 2), radius=2)
        # self.rect = self.image.get_rect(center=self.pos)

    def move(self, dt):
        self.pos += self.direction * self.speed * dt
        # self.rect.center = self.pos

    def update(self, dt):
        self.move(dt)
