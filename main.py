from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

player_right = Paddle((373, 0))
player_left = Paddle((-380, 0))
ball = Ball()

screen.listen()
screen.onkey(player_right.up, "Up")
screen.onkey(player_right.down, "Down")
screen.onkey(player_left.up, "w")
screen.onkey(player_left.down, "s")

game_is_on = True
point_player_left = 0
point_player_right = 0

while game_is_on:
    time.sleep(0.04)

    # Detect collision with wall
    if ball.ycor() > 285 or ball.ycor() < -285:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.xcor() > 340 and ball.distance(player_right) < 50 or ball.xcor() < -340 and ball.distance(player_left) < 50:
        ball.bounce_x()

    if ball.xcor() > 380:
        point_player_left += 1
        print("ball go brrr")

    if ball.xcor() < -380:
        point_player_right += 1
        print("ball go dog")

    ball.move()
    screen.update()

screen.exitonclick()
