import tkinter as tk

screen=tk.Tk()
screen.title("Color Paint")
screen.geometry("1000x1000")
screen.configure(bg="black")

pen=tk.Button(text="Pen",width=10,height=1,bg="blue",fg="black",font=("Arial",16))
pen.place(x=100,y=50)

brush=tk.Button(text="Brush",width=10,height=1,bg="grey",fg="black",font=("Arial",16))
brush.place(x=250,y=50)

eraser=tk.Button(text="Eraser",width=10,height=1,bg="white",fg="black",font=("Arial",16))
eraser.place(x=400,y=50)

penwidth=tk.Label(text="Penwidth",width=10,height=1,bg="green",fg="black")
penwidth.place(x=550,y=50)

s1=tk.Scale(from_=1,to=100,orient="horizontal",length=200)
s1.place(x=700,y=50)

c1=tk.Canvas(width=800,height=700)
c1.place(x=100,y=300)

l1=tk.Label(text="Select your color",width=20,height=2,bg="grey",fg="white")
l1.place(x=250,y=150)

screen.mainloop()