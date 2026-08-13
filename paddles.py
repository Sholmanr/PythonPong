from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, coords):
        super().__init__()
        self.create_paddle(coords)


    def create_paddle(self, coords):

        # for i in range(4):
        self.shape("square")
        self.goto(coords)
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()

    def move_paddle_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def move_paddle_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), self.ycor() - 20)



