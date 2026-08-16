from turtle import Turtle, Screen

tim=Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)
def move_backward():
    tim.backward(10)
def turn_left():
    new_heading=tim.heading()+10
    tim.setheading(new_heading)
def turn_right():
    new_heading=tim.heading()-10
    tim.setheading(new_heading)
def clear():
    tim.home()
    tim.clear()

screen.listen()
screen.onkey(move_forward,"Up")
screen.onkey(move_backward,"Down")
screen.onkey(turn_left,"Left")
screen.onkey(turn_right,"Right")
screen.onkey(clear,"c")
screen.exitonclick()