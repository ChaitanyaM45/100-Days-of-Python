from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self,quiz_brain: QuizBrain):
        self.quiz=quiz_brain
        self.window=Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)

        self.score_text=Label(text="Score:0",bg=THEME_COLOR,fg="white")
        self.score_text.grid(column=1,row=0)

        self.canvas=Canvas(width=300,height=250,highlightthickness=0,bg="white")
        self.question_text=self.canvas.create_text(150,125,text="Question",width=280,font=("Arial",20,"italic"),fill=THEME_COLOR)
        self.canvas.grid(column=0,row=1,columnspan=2,pady=50)

        correct=PhotoImage(file="./Day-034/images/true.png")
        self.correct_button=Button(image=correct,highlightthickness=0,command=self.true_pressed)
        self.correct_button.grid(column=0,row=2)

        wrong=PhotoImage(file="./Day-034/images/false.png")
        self.wrong_button=Button(image=wrong,highlightthickness=0,command=self.false_pressed)
        self.wrong_button.grid(column=1,row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            self.score_text.config(text=f"Score:{self.quiz.score}")
            q_text=self.quiz.next_question()
            self.canvas.itemconfig(self.question_text,text=q_text)
        else:
            self.canvas.itemconfig(self.question_text,text="You have reached question limit.")

    def true_pressed(self):
        is_right=self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right=self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000,self.get_next_question)