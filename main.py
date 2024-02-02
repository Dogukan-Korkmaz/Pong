from turtle import Screen
from paddle import Paddle
import time

screen = Screen()

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

p = Paddle()
p.create_paddle()

screen.listen()

screen.onkey(p.up, "Up")
screen.onkey(p.down, "Down")

game_is_on = True
while game_is_on:
    screen.update()

    screen.exitonclick()
