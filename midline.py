from turtle import Turtle


class Midline(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.setheading(90)
        self.hideturtle()
        self.pensize(3)
        self.penup()
        self.goto(0, -292)

    def draw_line(self):
        self.pendown()
        self.forward(15)

        self.penup()
        self.forward(15)
