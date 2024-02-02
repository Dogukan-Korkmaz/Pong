from turtle import Turtle

UP = 90
DOWN = 270


class Paddle(Turtle):

    def __init__(self):
        super().__init__()

    def create_paddle(self):
        self.penup()
        self.shape("square")
        self.color("white")
        self.shapesize(4, 1, 5)
        self.speed("fastest")
        self.setpos(379, 0)

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
