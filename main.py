import tkinter as tk

screen=tk.Tk()
screen.title("Multiplication table generator")
screen.geometry("500x800")
screen.configure(bg="grey")

def generatetable():
    number=int(e1.get())
    range1=int(r.get())
    for i in range(1,range1+1):
        result=str(number)+"*"+str(i)+"="+str(number*i)
        lb1.insert(tk.END,result)

l1=tk.Label(text="Multiplication table generator",width=25,height=2,bg="black",fg="white",font=("Arial",15))
l1.place(x=100,y=50)

l2=tk.Label(text="enter a number",width=15,height=1,bg="white",fg="black",font=("Arial",10))
l2.place(x=30,y=150)

e1=tk.Entry(width=15,bg="white",fg="black")
e1.place(x=250,y=150)

b1=tk.Button(text="Generate table",width=15,height=2,fg="black",bg="teal",command=generatetable)
b1.place(x=100,y=350)

l3=tk.Label(text="Select your range",width=20,height=2,bg="teal",fg="white",font=("Arial",10))
l3.place(x=50,y=250)

r=tk.IntVar()
r1=tk.Radiobutton(text=10,value=10,variable=r)
r1.place(x=250,y=250)

r2=tk.Radiobutton(text=20,value=20,variable=r)
r2.place(x=300,y=250)

r3=tk.Radiobutton(text=30,value=30,variable=r)
r3.place(x=350,y=250)

lb1=tk.Listbox(width=30,height=10,bg="black",fg="white")
lb1.place(x=100,y=450)


screen.mainloop()