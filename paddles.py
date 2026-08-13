from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, coords):
        super().__init__()
        self.segments = []
        self.create_paddle(coords)
        self.up = False
        self.down = False
        self.w = False
        self.s = False

    def create_paddle(self, coords):

        for i in range(4):
            segment = Turtle("square")
            segment.goto(coords)
            segment.color("white")
            segment.penup()
            coords = (segment.xcor(), segment.ycor() - 20)
            self.segments.append(segment)

    def move_paddle_up(self):
        for segment in range(len(self.segments) - 1, 0, -1):
            xcor = self.segments[segment - 1].xcor()
            ycor = self.segments[segment - 1].ycor()
            self.segments[segment].goto(xcor, ycor)

        self.segments[0].goto(self.segments[0].xcor(), self.segments[0].ycor() + 20)

    def move_paddle_down(self):
        for segment in range(0, len(self.segments) - 1, 1):
            xcor = self.segments[segment + 1].xcor()
            ycor = self.segments[segment + 1].ycor()
            self.segments[segment].goto(xcor, ycor)

        self.segments[len(self.segments) - 1].goto(self.segments[len(self.segments) - 1].xcor(), self.segments[len(self.segments) - 1].ycor() - 20)

    def press_up(self):
        self.up = True
        while self.up:
            self.move_paddle_up()

    def press_s(self):
        self.s = True
        while self.s:
            self.move_paddle_down()

    def release_up(self):
        self.up = False

    def release_s(self):
        self.s = False

