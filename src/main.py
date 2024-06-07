import pygame
from logic import Game_Master


def main():
    pygame.init()
    screen_x = 900
    screen_y = 600
    screen = pygame.display.set_mode(size=(screen_x, screen_y))
    clock = pygame.time.Clock()
    running = True

    gm = Game_Master(screen, 7)
    gm.initialize_balls(5, 25, "white", 1)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill("black")
        gm.move_balls()
        gm.draw_balls()
        pygame.display.flip()


main()
