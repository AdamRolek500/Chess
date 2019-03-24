from tkinter import *


class Board:
    BOARD_LENGTH = 8

    def __init__(self):
        self.root = Tk()

        self.draw()

    def draw(self):
        color_switch = True
        for x in range(Board.BOARD_LENGTH):
            color_switch = not color_switch
            for y in range(Board.BOARD_LENGTH):
                if color_switch:
                    color = "black"
                else:
                    color = "white"
                color_switch = not color_switch
                space = Canvas(self.root, width=50, height=50, bg=color, highlightthickness=0)
                space.bind("<Button-1>", self.click)
                space.piece = None
                space.grid(row=y, column=x)

    def click(self, event):
        space = event.widget
        info = space.grid_info()
        print("row: {}|| col: {}".format(info["row"], info["column"]))

    def run(self):
        self.root.mainloop()


def main():
    Board().run()


if __name__ == "__main__":
    main()
