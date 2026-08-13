import turtle
from turtle import Turtle

FONT = "Courier", 24, "normal"
class UI(Turtle):

    def __init__(self):
        super().__init__()
        self.segments = []
        self.create_middle()

    def create_middle(self):

        coord = (0,300)

        for i in range(0,11):
            segment = Turtle("square")
            segment.goto(coord)
            segment.shapesize(1.4, 0.5, 0.60)
            segment.color("white")
            coord = (0, segment.ycor()-60)
            self.segments.append(segment)


class RightSideScore(Turtle):

    def __init__(self):
        super().__init__()
        self.goto(150,240)
        self.color("white")
        self.right_score = 0
        self.create_right_score()
        self.hideturtle()

    def update_right_score(self):
        self.right_score += 1
        self.clear()
        self.create_right_score()

    def create_right_score(self):
        self.write(f"{self.right_score}", align="center", font=FONT)


class LeftSideScore(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(-150, 240)
        self.color("white")
        self.left_score = 0
        self.create_left_score()
        self.hideturtle()

    def create_left_score(self):
        self.write(f"{self.left_score}",align="center",font=FONT)

    def update_left_score(self):
        self.left_score += 1
        self.clear()
        self.create_left_score()



