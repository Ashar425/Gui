import tkinter as tk

screen = tk.Tk()
screen.config(bg="light grey")
screen.title("Currency Converter")
screen.geometry("500x350")

l1 = tk.Label(text="Enter USD ($):", width=15, height=1, bg="light grey", fg="black", font=("Arial", 12))
l1.place(x=50, y=80)

e1 = tk.Entry(width=25, bg="white", fg="black")
e1.place(x=230, y=85)

def convert():
    usd = float(e1.get())
    inr = usd * 94
    e2.delete(0, tk.END)
    e2.insert(0, str(inr) + " Rupees")

b1 = tk.Button(text="Convert to INR", width=15, height=1, bg="light green", fg="black", font=("Arial", 12), command=convert)
b1.place(x=170, y=150)

l2 = tk.Label(text="Result in INR:", width=15, height=1, bg="light grey", fg="black", font=("Arial", 12))
l2.place(x=50, y=230)

e2 = tk.Entry(width=25, bg="white", fg="black")
e2.place(x=230, y=235)

screen.mainloop()