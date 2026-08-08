from turtle import Turtle, Screen
from paddles import Paddle
import time

STARTING_CORDS = [(-290,20), (280,20)]
running = True
screen = Screen()
screen.tracer(0)

screen.setup(600,600)
screen.bgcolor("black")


left_paddle = Paddle(coords=STARTING_CORDS[0])
right_paddle = Paddle(coords=STARTING_CORDS[1])

screen.listen()
screen.onkeypress(right_paddle.move_paddle_up,"Up")
screen.onkeypress(right_paddle.move_paddle_down,"Down")
screen.onkeypress(left_paddle.move_paddle_up,"w")
screen.onkeypress(left_paddle.move_paddle_down,"s")

while running:
    screen.update()
    time.sleep(0.1)


screen.exitonclick()