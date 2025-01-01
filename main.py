# this allows us to use code from
# the open-source pygame library
# throughout this file
import sys
from random import choice, randint, uniform

import pygame

from asteroid import Asteroid
from asteroidfield import AsteroidField
from bullet import Shot
from constants import *
from particle import Particle
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
    particle_group = pygame.sprite.Group()

    Player.containers = (updatable_group, drawable_group)
    Asteroid.containers = (asteroid_group, updatable_group, drawable_group)
    AsteroidField.containers = updatable_group
    Shot.containers = (bullet_group, updatable_group, drawable_group)
    Particle.containers = (particle_group, updatable_group, drawable_group)

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
                player.lives -= 1
                player.respawn(screen)
                if player.lives <= 0:
                    print("Game Over!")
                    sys.exit(0)
                break
            for bullet in bullet_group:
                if asteroid.collision(bullet):
                    create_explosion(asteroid.position)
                    asteroid.split()
                    bullet.kill()
                    score += 1

        # Create the text and text_rectangle for the score board
        score_text = create_text(f"Score: {score}", (255, 255, 255))
        text = score_text[0]
        textRect = score_text[1]
        textRect.topleft = (0, 0)
        screen.blit(text, textRect)

        live_text = create_text(f"Remaining Lives: {player.lives}", (255, 255, 255))
        l_text = live_text[0]
        l_textRect = live_text[1]
        l_textRect.topleft = (0, textRect.height)
        screen.blit(l_text, l_textRect)

        # particle_group.draw(screen)
        # particle_group.update(dt)

        pygame.display.flip()

        dt = clock.tick(60) / 1000


def create_explosion(pos):
    print("Creating explosion at:", pos)
    particle_colors = [
        (255, 200, 50),
        (255, 100, 0),
        (255, 50, 0),
        (255, 255, 200),
        (255, 255, 255),
    ]

    num_particles = 50
    for _ in range(num_particles):
        angle = uniform(0, 360)
        direction = pygame.Vector2(1, 0).rotate(angle)

        speed = randint(100, 300)
        lifetime = uniform(0.5, 1.5)
        color = choice(particle_colors)

        Particle(Particle.containers, pos, color, direction, speed, lifetime)


def create_text(text, color):
    font = pygame.font.SysFont("arial", 30)
    text = font.render(text, True, color)

    # Create a rectangle to store the text and position it somewhere
    textRect = text.get_rect()

    return text, textRect


if __name__ == "__main__":
    main()
