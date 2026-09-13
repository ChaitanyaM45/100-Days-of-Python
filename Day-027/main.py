from tkinter import *

window=Tk()
window.title("Miles to KM Converter")
window.minsize(width=400,height=400)
window.config(padx=20,pady=20)

miles=Entry(width=7)
miles.grid(column=1,row=0)

txt=Label(text="Miles")
txt.grid(column=2,row=0)

txt1=Label(text="is equal to")
txt1.grid(column=0,row=1)

txt2=Label(text="0")
txt2.grid(column=1,row=1)

txt3=Label(text="Km")
txt3.grid(column=2,row=1)

def calculate():
    txt2.config(text=f"{float(miles.get())*1.6}")

button=Button(text="Calculate",command=calculate)
button.grid(column=1,row=2)

window.mainloop()

# from tkinter import *

# window=Tk()
# window.title("My First GUI")
# window.minsize(width=800,height=600)

# my_label=Label(text="I am Label",font=("Arial",24,"bold"))
# my_label.grid(column=0,row=0)

# def button_clicked():
#     my_label.config(text=f"{entry.get()}")

# button=Button(text="Click Me",command=button_clicked)
# button.grid(column=1,row=1)

# new_button=Button(text="Again Click Me",command=button_clicked)
# new_button.grid(column=3,row=0)

# entry=Entry(width=10)
# entry.grid(column=4,row=3)



# window.mainloop()