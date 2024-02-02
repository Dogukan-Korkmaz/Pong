from turtle import Screen
from paddle import Paddle

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

player = Paddle((373, 0))
bot = Paddle((-380, 0))

screen.listen()
screen.onkey(player.up, "Up")
screen.onkey(player.down, "Down")
screen.onkey(bot.up, "w")
screen.onkey(bot.down, "s")

game_is_on = True

while game_is_on:
    screen.update()

screen.exitonclick()
