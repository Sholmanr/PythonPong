from turtle import Turtle, Screen
from paddles import Paddle
import UI as ui
import time
from ball import Ball

STARTING_CORDS = [(-250,20), (250,20)]
running = True
screen = Screen()
screen.tracer(0)

screen.setup(600,600)
screen.bgcolor("black")

direction = 0

left_paddle = Paddle(coords=STARTING_CORDS[0])
right_paddle = Paddle(coords=STARTING_CORDS[1])
interface = ui.UI()
left = ui.LeftSideScore()
right = ui.RightSideScore()
ball = Ball()
turtle = Turtle()


screen.listen()
screen.onkeypress(right_paddle.move_paddle_up,"Up")
screen.onkeypress(right_paddle.move_paddle_down,"Down")
screen.onkeypress(left_paddle.move_paddle_up,"w")
screen.onkeypress(left_paddle.move_paddle_down,"s")

while running:
    screen.update()
    time.sleep(0.1)

    # for segment in right_paddle.segments:
    if ball.distance(right_paddle) < 30 and ball.xcor() < 320 or ball.distance(left_paddle) < 30 and ball.xcor() > -320:
        ball.bounce_x()

    if direction == 0:
        ball.move()
    elif direction == 1:
        ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    if ball.xcor() == 300:
        left.update_left_score()
        ball.create_ball()
    if ball.xcor() == -300:
        right.update_right_score()
        ball.create_ball()

    if left.left_score == 5 or right.right_score == 5:
        running = False
        turtle.goto(0,0)
        turtle.color("white")
        turtle.write("Game Over", align="center",  font=("Calibre", 20, "normal"))
        turtle.hideturtle()




screen.exitonclick()