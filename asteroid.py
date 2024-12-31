import random

import pygame

from circleshape import *
from constants import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        new_angle = random.uniform(20, 50)
        vector1 = self.velocity.rotate(new_angle)
        vector2 = self.velocity.rotate(-new_angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        child1 = Asteroid(self.position[0], self.position[1], new_radius)
        child1.velocity = vector1 * 1.2

        child2 = Asteroid(self.position[0], self.position[1], new_radius)
        child2.velocity = vector2 * 1.2
