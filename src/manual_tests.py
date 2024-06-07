import pygame
from logic import Game_Master


def main():
    screen_x = 900
    screen_y = 600
    screen = pygame.display.set_mode(size=(screen_x, screen_y))

    gm = Game_Master(screen, 3)
    print(gm.initialize_balls(5, 50, "white"))
    for i in range(len(gm.balls)):
        current_ball = gm.balls[i]
        for j in range(len(gm.balls)):
            if i != j:
                target_ball = gm.balls[j]
                print(current_ball.collision_check(target_ball))


main()
