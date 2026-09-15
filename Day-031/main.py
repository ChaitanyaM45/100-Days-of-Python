from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"

try:
    df=pd.read_csv(r"./Day-031/data/words_to_learn.csv")
except FileNotFoundError:
    df=pd.read_csv(r"./Day-031/data/german_words.csv")
new_dict=df.to_dict(orient="records")
current_card={}

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card=random.choice(new_dict)
    canvas.itemconfig(card_title,text="German",fill="black")
    canvas.itemconfig(card_word,text=current_card["German"],fill="black")
    canvas.itemconfig(card_bg,image=card_front_img)
    flip_timer=window.after(3000,func=flip_card)

def flip_card():
    global current_card
    canvas.itemconfig(card_title,text="English",fill="white")
    canvas.itemconfig(card_word,text=current_card["English"],fill="white")
    canvas.itemconfig(card_bg,image=card_back_img)

def is_known():
    new_dict.remove(current_card)
    data=pd.DataFrame(new_dict)
    data.to_csv("./Day-031/data/words_to_learn.csv",index=False)
    next_card()


window=Tk()
window.title("Flashy")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

flip_timer=window.after(3000,func=flip_card)

canvas=Canvas(width=800,height=526,bg=BACKGROUND_COLOR,highlightthickness=0)
card_front_img=PhotoImage(file="./Day-031/images/card_front.png")
card_back_img=PhotoImage(file="./Day-031/images/card_back.png")
card_bg=canvas.create_image(400,263,image=card_front_img)
card_title=canvas.create_text(400,150,text="",font=("Ariel",40,"italic"))
card_word=canvas.create_text(400,263,text="",font=("Ariel",60,"bold"))
canvas.grid(column=0,row=0,columnspan=2)

wrong_img=PhotoImage(file="./Day-031/images/wrong.png")
wrong_button=Button(image=wrong_img,bg=BACKGROUND_COLOR,highlightthickness=0,command=next_card)
wrong_button.grid(column=0,row=1)
right_img=PhotoImage(file="./Day-031/images/right.png")
right_button=Button(image=right_img,bg=BACKGROUND_COLOR,highlightthickness=0,command=is_known)
right_button.grid(column=1,row=1)

next_card()

window.mainloop()