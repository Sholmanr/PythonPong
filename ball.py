from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.goto(0,0)
        self.shape("circle")
        self.color("white")
