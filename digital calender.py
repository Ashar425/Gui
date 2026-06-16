import tkinter as tk
import datetime

def showdate():
   currentdate = datetime.datetime.now()
   x = currentdate.strftime("%d/%m/%Y")
   l2.config(text=x)

mainscreen = tk.Tk()
mainscreen.title("Calendar GUI")
mainscreen.configure(bg="black")
mainscreen.geometry("500x500")

dg1 = tk.Label(text="Calendar", width=20, height=2, bg="#56dbdb", fg="#dcf6fc", font=("Arial",20))
dg1.place(x=100,y=50)

b1 = tk.Button(text="Show Date", width=10, height=2, bg="#280985", fg="#bfc2a9", font=("Arial",20), command=showdate)
b1.place(x=100,y=200)

l2 = tk.Label(text="", width=20, height=2, bg="#4a7682", fg="#aac2a9", font=("Arial",20))
l2.place(x=100,y=350)

mainscreen.mainloop()