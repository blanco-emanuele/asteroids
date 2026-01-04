from logger import log_state
import pygame
from constants import *
from player import *

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while(True):
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        
        x = SCREEN_WIDTH / 2
        y = SCREEN_HEIGHT / 2
        player = Player(x, y)
        player.draw(screen)

        pygame.display.flip()
        elapsed_milliseconds = clock.tick(60)
        dt = elapsed_milliseconds / 1000

if __name__ == "__main__":
    main()
