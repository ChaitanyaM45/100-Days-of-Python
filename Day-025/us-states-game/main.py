import turtle
import pandas as pd

df=pd.read_csv("./Day-025/us-states-game/50_states.csv")

screen=turtle.Screen()
screen.title("U.S. States Game")

image="./Day-025/us-states-game/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


guessed_state=0
guessed_states=[]
all_state=df.state.to_list()
game_is_on=True
while game_is_on:
    answer_state=screen.textinput(title=f"{guessed_state}/50 State Correct",prompt="Enter the State").title()
    if (answer_state in all_state) and (answer_state not in guessed_states):
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        state=df[df['state']==answer_state]
        X=state.x.iloc[0]
        Y=state.y.iloc[0]
        t.goto(X,Y)
        t.write(state.state.iloc[0],align="left",font=("Arial",10,"bold"))
        guessed_state+=1
        guessed_states.append(answer_state)

    if guessed_state==50:
        game_is_on=False
        

    if (guessed_state!=0) and (guessed_state%5)==0:
        choice=screen.textinput("Do you want to Continue??",prompt="Type Y/N:")
        if choice=="N":
            game_is_on=False
        else:
            game_is_on=True

screen.exitonclick()