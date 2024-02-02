from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        self.shapesize(4, 1, 5)
        self.speed("fastest")
        self.goto(position)
        self.paddle_speed = 30

    def up(self):
        new_y = self.ycor() + self.paddle_speed
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - self.paddle_speed
        self.goto(self.xcor(), new_y)

    def speed_up(self):
        self.paddle_speed += 1
