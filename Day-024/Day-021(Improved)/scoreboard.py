from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open(r"C:\Users\Chaitanya Mahale\OneDrive\Desktop\Udemy Python Course\100-Days-of-Python\Day-024\Day-021(Improved)\data.txt") as data:
            self.high_score=int(data.read())
        self.color("white")
        self.speed("fastest")
        self.penup()
        self.goto(0,265)
        self.update_scoorboard()
        self.hideturtle()

    def update_scoorboard(self):
        self.clear()
        self.write(f"Score : {self.score}\tHigh Score : {self.high_score}",align="center",font=("Arial",24,"bold"))

    def increase_score(self):
        self.score += 1
        self.update_scoorboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score=self.score
            with open(r"C:\Users\Chaitanya Mahale\OneDrive\Desktop\Udemy Python Course\100-Days-of-Python\Day-024\Day-021(Improved)\data.txt",mode="w") as data:
                data.write(str(self.high_score))

        self.score=0
        self.update_scoorboard()
