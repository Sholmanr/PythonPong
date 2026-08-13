from turtle import Turtle, Screen
from paddles import Paddle
import UI as ui
import time

STARTING_CORDS = [(-290,20), (280,20)]
running = True
screen = Screen()
screen.tracer(0)

screen.setup(600,600)
screen.bgcolor("black")


left_paddle = Paddle(coords=STARTING_CORDS[0])
right_paddle = Paddle(coords=STARTING_CORDS[1])
interface = ui.UI()
left = ui.LeftSideScore()
right = ui.RightSideScore()



screen.listen()
screen.onkeypress(right_paddle.move_paddle_up,"Up")
screen.onkeypress(right_paddle.move_paddle_down,"Down")
screen.onkeypress(left_paddle.move_paddle_up,"w")
screen.onkeypress(left_paddle.move_paddle_down,"s")

while running:
    screen.update()
    left.update_left_score()
    right.update_right_score()
    time.sleep(0.1)

    #TODO create the ball
    #   implement ball movmement

screen.exitonclick()