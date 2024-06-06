import pygame
from logic import Game_Master


def main():
    gm = Game_Master(900, 600)
    print(gm.balls)
    gm.generate_balls(5, "white")
    print(gm.balls)


main()
