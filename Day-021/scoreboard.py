from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.speed("fastest")
        self.penup()
        self.goto(0,265)
        self.write(f"Score : {self.score}",align="center",font=("Arial",24,"bold"))
        self.hideturtle()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score : {self.score}", align="center", font=("Arial", 24, "bold"))

    def game_over(self):
        self.goto(0,0)
        self.clear()
        self.write("Game Over",align="center",font=("Arial",30,"bold"))