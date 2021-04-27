from turtle import Screen
from paddle import Paddle
from ball import Ball
from midline import Midline
from scoreboard import Scoreboard

# Create the screen
screen = Screen()
screen.setup(height=600, width=800)
screen.title("Pong")
screen.bgcolor("black")
screen.tracer(0)

# Create Midline
midline = Midline()
for x in range(20):
    midline.draw_line()

# Create and move right paddle
right_paddle = Paddle((350, 0))
screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")

# Create and move left paddle
left_paddle = Paddle((-350, 0))
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")

# Create ball
ball = Ball()

# Create Scoreboard
score = Scoreboard()

game_is_on = True
while game_is_on:
    screen.update()
    ball.move()

    # Detect collision with wall and bounce
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.wall_bounce()

    # Detect collision with paddle and bounce
    if ball.xcor() > 330 or ball.xcor() < -330:
        if ball.distance(right_paddle) < 50 or ball.distance(left_paddle) < 50:
            ball.paddle_bounce()

    # Detect when R paddle misses
    if ball.xcor() > 405:
        score.increase_left()
        ball.reset_position_right()

    # Detect when L paddle misses
    if ball.xcor() < -405:
        score.increase_right()
        ball.reset_position_left()

screen.exitonclick()
