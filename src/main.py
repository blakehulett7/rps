import pygame
from logic import Game_Master


def main():
    pygame.init()
    screen_x = 900
    screen_y = 600
    screen = pygame.display.set_mode(size=(screen_x, screen_y))
    clock = pygame.time.Clock()
    running = True

    gm = Game_Master(screen, 3)
    gm.initialize_balls(30, 25, 1)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill("black")
        gm.move_balls()
        gm.wall_collisions()
        gm.ball_collisions()
        gm.draw_balls()
        pygame.display.flip()


main()
