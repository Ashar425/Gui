import tkinter as tk

screen = tk.Tk()
screen.title("Theme Changer")
screen.geometry("500x300")
screen.configure(bg="red")

def change_color():
    color = bg_color.get()
    screen.configure(bg=color.lower())

l1 = tk.Label(text="Choose Background Color:", bg="white", fg="black", font=("Arial", 14))
l1.place(x=130, y=30)

bg_color = tk.StringVar()
bg_color.set("Red")

r1 = tk.Radiobutton(text="Red", value="Red", variable=bg_color, command=change_color, bg="white", font=("Arial", 12))
r1.place(x=210, y=80)

r2 = tk.Radiobutton(text="Green", value="Green", variable=bg_color, command=change_color, bg="white", font=("Arial", 12))
r2.place(x=210, y=120)

r3 = tk.Radiobutton(text="Blue", value="Blue", variable=bg_color, command=change_color, bg="white", font=("Arial", 12))
r3.place(x=210, y=160)

r4 = tk.Radiobutton(text="Yellow", value="Yellow", variable=bg_color, command=change_color, bg="white", font=("Arial", 12))
r4.place(x=210, y=200)

r5 = tk.Radiobutton(text="Purple", value="Purple", variable=bg_color, command=change_color, bg="white", font=("Arial", 12))
r5.place(x=210, y=240)

screen.mainloop()