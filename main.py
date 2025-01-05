import pygame
from constants import *

def main():
    BLACK = (0, 0, 0)
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill(BLACK)
        pygame.display.flip()

if __name__ == "__main__":
    main()