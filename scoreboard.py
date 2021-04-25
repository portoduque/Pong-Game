from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 60, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.right_score = 0
        self.left_score = 0
        self.update()

    def update(self):
        self.clear()
        self.goto(100, 200)
        self.write(arg=self.right_score, align=ALIGNMENT, font=FONT)
        self.goto(-100, 200)
        self.write(arg=self.left_score, align=ALIGNMENT, font=FONT)

    def increase_right(self):
        self.right_score += 1
        self.update()

    def increase_left(self):
        self.left_score += 1
        self.update()




