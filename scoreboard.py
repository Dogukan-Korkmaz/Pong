from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.scoreboard_right()
        self.scoreboard_left()

    def scoreboard_right(self):
        self.clear()
        self.goto(200, 200)
        self.write(self.r_score, align="center", font=("Courier", 70, "normal"))

    def scoreboard_left(self):
        self.clear()
        self.goto(-200, 200)
        self.write(self.l_score, align="center", font=("Courier", 70, "normal"))

    def add_score_left(self):
        self.l_score += 1
        self.scoreboard_left()

    def add_score_right(self):
        self.r_score += 1
        self.scoreboard_right()
