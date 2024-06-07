import pygame
from logic import Game_Master


def main():
    screen_x = 900
    screen_y = 600
    screen = pygame.display.set_mode(size=(screen_x, screen_y))

    gm = Game_Master(screen)
    print(gm.initialize_balls(5, 50, "white"))


main()
