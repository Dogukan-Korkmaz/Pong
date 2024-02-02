from turtle import Screen

import paddle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

player_right = Paddle((373, 0))
player_left = Paddle((-380, 0))
ball = Ball()
scoreboard = Scoreboard()
scoreboard.scoreboard_left()
scoreboard.scoreboard_right()

screen.listen()
screen.onkey(player_right.up, "Up")
screen.onkey(player_right.down, "Down")
screen.onkey(player_left.up, "w")
screen.onkey(player_left.down, "s")

game_is_on = True
while game_is_on:
    time.sleep(0.04)

    # Detect collision with wall
    if ball.ycor() > 285 or ball.ycor() < -285:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.xcor() > 340 and ball.distance(player_right) < 50 or ball.xcor() < -340 and ball.distance(player_left) < 50:
        ball.x_move += 5
        ball.y_move += 5
        ball.bounce_x()

    # Detect player_right misses
    if ball.xcor() > 380:
        scoreboard.add_score_left()
        scoreboard.scoreboard_left()
        ball.reset_position()

    # Detect player_left misses
    if ball.xcor() < -380:
        scoreboard.add_score_right()
        scoreboard.scoreboard_right()
        ball.reset_position()

    ball.move()
    screen.update()

screen.exitonclick()
