import tkinter as tk
import datetime

def showtime():
   currenttime=datetime.datetime.now()
   x=currenttime.strftime("%H:%M:%S")
   l2.config(text=x)
   l2.after(1000,showtime)

mainscreen=tk.Tk()
mainscreen.title("Digital Clock")
mainscreen.configure(bg="grey")
mainscreen.geometry("500x500")

dg1=tk.Label(text="Digital Clock",width=20,height=2,bg="black",fg="white",font=("Arial",20))
dg1.place(x=100,y=50)

b1=tk.Button(text="Show Time",width=10,height=2,bg="teal",fg="white",font=("Arial",20),command=showtime)
b1.place(x=100,y=200)

l2=tk.Label(text="",width=20,height=2,bg="white",fg="black",font=("Arial",20))
l2.place(x=100,y=350)

mainscreen.mainloop()