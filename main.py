import pygame
from constants import *
from player import Player

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

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)

    # Create a Clock object
    clock_obj = pygame.time.Clock()

    # Delta time
    """In math, the Greek letter delta (Δ) is often used to represent a change in a value. 
    In game development, we use "delta time" to represent the amount of time that has passed since the last frame was drawn. 
    This value is useful to decouple the game's speed from the speed it's being drawn to the screen.

    If your computer speeds up, the asteroids shouldn't also speed up. 
    Conversely, if your computer slows down, the asteroids shouldn't also slow down: they would just move less smoothly."""
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(FILL_COLOR_BLACK)
        
        player.draw(screen)

        player.update(dt)

        pygame.display.flip()
        dt = clock_obj.tick()/1000



if __name__ == "__main__":

    main()
    print_screen_size()
    draw_screen()
    # pygame.display.flip()

   