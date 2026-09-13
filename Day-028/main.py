from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
timer_countdown=None

# ---------------------------- TIMER RESET ------------------------------- # 

def timer_reset():
    global timer_countdown
    global reps
    window.after_cancel(timer_countdown)
    reps = 0
    canvas.itemconfig(timer, text="00:00")
    timer_txt.config(text="Timer", fg=GREEN)
    tickmark.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps+=1
    if reps%8==0:
        count_down(LONG_BREAK_MIN*60)
        timer_txt.config(text="LONG BRAKE",fg=RED)
    elif reps%2==0:
        count_down(SHORT_BREAK_MIN*60)
        timer_txt.config(text="SHORT BRAKE",fg=PINK)
    else:
        count_down(WORK_MIN*60)
        timer_txt.config(text="WORK",fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    global timer_countdown
    canvas.itemconfig(timer,text=f"{count//60:02d}:{count%60:02d}")
    if count>0:
        timer_countdown=window.after(1000,count_down,count-1)
    else:
        start_timer()
        mark="✔"
        for i in range(math.floor(reps/2)):
            mark+="✔"
        tickmark.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)

timer_txt=Label(text="Timer",fg=GREEN,font=(FONT_NAME,50,"bold"),bg=YELLOW)
timer_txt.grid(column=1,row=0)

canvas=Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
tomato_img=PhotoImage(file="./Day-028/tomato.png")
canvas.create_image(100,112,image=tomato_img)
timer=canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,30,"bold"))
canvas.grid(column=1,row=1)

start=Button(text="START",highlightthickness=0,command=start_timer)
start.grid(column=0,row=2)

reset=Button(text="RESET",highlightthickness=0,command=timer_reset)
reset.grid(column=2,row=2)

tickmark=Label(fg=GREEN,bg=YELLOW,font=(70))
tickmark.grid(column=1,row=3)

window.mainloop()