from turtle import Turtle

INCREASED_SPEED = 0.02
DEFAULT_SPEED = 0.2


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.x_move_distance = DEFAULT_SPEED
        self.y_move_distance = DEFAULT_SPEED

    def move(self):
        new_x = self.xcor() + self.x_move_distance
        new_y = self.ycor() + self.y_move_distance
        self.goto(new_x, new_y)

    def wall_bounce(self):
        self.y_move_distance *= -1

    def paddle_bounce(self):
        self.x_move_distance *= -1
        self.increase_speed()

    def reset_position_left(self):
        self.goto(0, 0)
        self.reset_speed()

    def reset_position_right(self):
        self.goto(0, 0)
        self.reset_speed()
        self.x_move_distance *= -1

    def increase_speed(self):
        if self.x_move_distance > 0:
            self.x_move_distance += INCREASED_SPEED
        else:
            self.x_move_distance -= INCREASED_SPEED

        if self.y_move_distance > 0:
            self.y_move_distance += INCREASED_SPEED
        else:
            self.y_move_distance -= INCREASED_SPEED

    def reset_speed(self):
        if self.x_move_distance > 0:
            self.x_move_distance = DEFAULT_SPEED
        else:
            self.x_move_distance = DEFAULT_SPEED

        if self.y_move_distance > 0:
            self.y_move_distance = DEFAULT_SPEED
        else:
            self.y_move_distance = DEFAULT_SPEED




