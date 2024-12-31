# this allows us to use code from
# the open-source pygame library
# throughout this file
import sys

import pygame

from asteroid import Asteroid
from asteroidfield import AsteroidField
from bullet import Shot
from constants import *
from player import Player


def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0

    # Create a screen to be shown for pygame
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Creating a score board to show how many asteroids destroyed
    score = 0

    updatable_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()
    asteroid_group = pygame.sprite.Group()
    bullet_group = pygame.sprite.Group()

    Player.containers = (updatable_group, drawable_group)
    Asteroid.containers = (asteroid_group, updatable_group, drawable_group)
    AsteroidField.containers = updatable_group
    Shot.containers = (bullet_group, updatable_group, drawable_group)

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)

    asteroid_field = AsteroidField()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Set the fill of the screen to Black (0, 0, 0)
        pygame.Surface.fill(screen, "black")

        for drawable in drawable_group:
            drawable.draw(screen)

        for updatable in updatable_group:
            updatable.update(dt)

        for asteroid in asteroid_group:
            if asteroid.collision(player):
                print("Game Over!")
                sys.exit(0)
            for bullet in bullet_group:
                if asteroid.collision(bullet):
                    asteroid.split()
                    bullet.kill()
                    score += 1

        created_text = create_text(f"Score: {score}")
        text = created_text[0]
        textRect = created_text[1]
        screen.blit(text, textRect)

        pygame.display.flip()

        dt = clock.tick(60) / 1000


def create_text(text):
    font = pygame.font.SysFont("arial", 30)
    text = font.render(text, True, (255, 255, 255))

    # Create a rectangle to store the text and position it somewhere
    textRect = text.get_rect()
    textRect.topleft = (0, 0)

    return text, textRect


if __name__ == "__main__":
    main()
