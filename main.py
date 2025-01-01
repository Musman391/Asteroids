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

particle_group = pygame.sprite.Group()


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
    particle_g = pygame.sprite.Group()

    Player.containers = (updatable_group, drawable_group)
    Asteroid.containers = (asteroid_group, updatable_group, drawable_group)
    AsteroidField.containers = updatable_group
    Shot.containers = (bullet_group, updatable_group, drawable_group)
    Particle.containers = (particle_g, updatable_group, drawable_group)

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
                    spawn_particles(100, asteroid.position, screen)
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
        particle_group.update(dt)

        pygame.display.flip()

        dt = clock.tick(60) / 1000


def spawn_particles(n: int, pos: pygame.Vector2, screen):
    for _ in range(n):
        color = choice(("red", "green", "blue"))
        direction = pygame.math.Vector2(uniform(-1, 1), uniform(-1, 1))
        direciton = direction.normalize()
        speed = randint(50, 400)
        Particle(particle_group, pos, color, direciton, speed, screen)


def create_text(text, color):
    font = pygame.font.SysFont("arial", 30)
    text = font.render(text, True, color)

    # Create a rectangle to store the text and position it somewhere
    textRect = text.get_rect()

    return text, textRect


if __name__ == "__main__":
    main()
