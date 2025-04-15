import pygame 
from constants import * 
from player import *
from circleshape import *


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock() 
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        dt = clock.get_time() / 1000
        screen.fill("black")
        player.draw(screen)
        player.update(dt)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
