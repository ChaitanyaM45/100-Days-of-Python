from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet=screen.textinput(title="Make your bet",prompt="Which Turtle will win the race? Enter Color")
color=["red","green","yellow","blue","purple","orange"]
y_pos=[-125,-75,-25,25,75,125]
all_turtle=[]

for turtle_index in range(0,6):
    new_turtle=Turtle(shape="turtle")
    new_turtle.color(color[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-220, y=y_pos[turtle_index])
    all_turtle.append(new_turtle)

if user_bet:
    is_race_on=True

while is_race_on:
    for turtle in all_turtle:
        rand_dist=random.randint(0,10)
        turtle.forward(rand_dist)
        if turtle.xcor()>230:
            is_race_on=False
            winning_color=turtle.pencolor()
            if winning_color==user_bet:
                print(f"You Won! {winning_color} turtle won the race!")
            else:
                print(f"You Lose! {winning_color} turtle won the race!")

screen.exitonclick()