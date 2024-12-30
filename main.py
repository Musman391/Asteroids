# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

from constants import *


def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Create a screen to be shown for pygame
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Set the fill of the screen to Black (0, 0, 0)
        pygame.Surface.fill(screen, (0, 0, 0))
        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
