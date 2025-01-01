import random

import pygame

from circleshape import CircleShape
from constants import *


class Particle(pygame.sprite.Sprite):
    def __init__(self, groups, pos, color, direction, speed, lifetime):
        super().__init__(groups)
        self.pos = pos
        self.color = color
        self.direction = direction
        self.speed = speed
        self.lifetime = lifetime
        self.alpha = 255
        self.fade_rate = 255 / lifetime
        self.radius = random.randint(2, 4)

    def draw(self, screen):
        print("Drawing the particle")
        pygame.draw.circle(
            surface=screen,
            color=(*self.color, self.alpha),
            center=(self.radius, self.radius),
            radius=self.radius,
        )

    def move(self, dt):
        self.pos += self.direction * self.speed * dt
        # self.rect.center = self.pos

    def update(self, dt):
        self.move(dt)

        self.alpha -= self.fade_rate * dt
        if self.alpha <= 0:
            self.kill()
