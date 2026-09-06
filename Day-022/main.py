from turtle import Screen

from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen=Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))
ball=Ball()
scoreboard=Scoreboard()

screen.listen()
screen.onkey(l_paddle.go_up,"Up")
screen.onkey(l_paddle.go_down,"Down")
screen.onkey(r_paddle.go_up,"8")
screen.onkey(r_paddle.go_down,"2")

is_game_on=True
while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #detect collision with wall
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()

    #detect collision with paddles
    if (r_paddle.distance(ball)<50 and ball.xcor()>320) or (l_paddle.distance(ball)<50 and ball.xcor()<-320):
        ball.bounce_x()
        ball.move_speed*=0.9

    #detect r_paddle misses
    if ball.xcor()>380:
        ball.resetpos()
        scoreboard.l_point()

    #detect l_paddle misses
    if ball.xcor()<-380:
        ball.resetpos()
        scoreboard.r_point()

screen.exitonclick()