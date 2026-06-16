import tkinter as tk
import random
from tkinter import messagebox

screen=tk.Tk()
screen.title("Guess The Number")
screen.configure(bg="black")
screen.geometry("800x600")

attempts=0
actualnumber=random.randint(1,20)


def checkresult():
    global attempts,actualnumber
    guessnumber=int(e1.get())
    if guessnumber>actualnumber:
        result="Guess Lower"
    elif guessnumber<actualnumber:
        result="Guess Higher"
    else:
        result="Correct Answer"
    attempts=attempts+1
    l3.config(text="attempts: "+str(attempts))

    messagebox.showinfo("Result",result)

l1=tk.Label(text="Welcome to guess the number game",width=30,height=2,bg="skyblue",fg="white",font=("Comic Sans MS",20))
l1.place(x=200,y=50)

l2=tk.Label(text="Take a guess from 1 to 20",width=25,height=1,bg="turquoise",fg="white",font=("Comic Sans MS",13))
l2.place(x=50,y=150)

e1=tk.Entry(width=20,bg="teal",fg="white")
e1.place(x=400,y=150)

b1=tk.Button(text="Check",width=15,height=1,bg="grey",fg="white",command=checkresult)
b1.place(x=200,y=250)

l3=tk.Label(text="Attempts:0",width=25,height=1,bg="green",fg="white",font="Arial")
l3.place(x=200,y=350)

screen.mainloop()