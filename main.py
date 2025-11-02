import pygame
from constants import *

def main():
    print( "Starting Asteroids!")

def print_screen_size():
    # print("Screen width: ", SCREEN_WIDTH)
    # print("Screen height: ", SCREEN_HEIGHT)
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

def draw_screen():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(FILL_COLOR_BLACK)
        
        pygame.display.flip()



if __name__ == "__main__":

    main()
    print_screen_size()
    draw_screen()
    # pygame.display.flip()
