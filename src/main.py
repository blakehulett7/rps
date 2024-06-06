from objects import Window
from logic import Game_Master


def main():
    screen_x = 900
    screen_y = 600
    win = Window(screen_x, screen_y)

    gm = Game_Master(screen_x=screen_x, screen_y=screen_y, canvas=win.canvas)
    gm.generate_balls(5, "red")
    gm.draw_balls()

    win.wait_for_close()


main()
