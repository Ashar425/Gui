import tkinter as tk
import gtts
from tkinter import messagebox

screen=tk.Tk()
screen.title("Text to speech converter")
screen.configure(bg="black")
screen.geometry("800x500")

def texttospeech():
    text1=t1.get("1.0","end-1c")
    audiofile=gtts.gTTS(text=text1,slow=False,lang="en")
    audiofile.save("output.mp3")
    messagebox.showinfo("Succes","the text is converted into speech")


l1=tk.Label(text="text to speech converter",width=30,height=1,bg="grey",fg="white",font=("Arial",20))
l1.place(x=100,y=100)

l2=tk.Label(text="Enter your text below",width=20,height=1,bg="teal",fg="black",font=("Comic Sans MS",12))
l2.place(x=200,y=150)

t1=tk.Text(width=20,height=5,bg="turquoise",fg="black",font=("Arial",20))
t1.place(x=200,y=200)

b1=tk.Button(text="convert",width=15,height=1,bg="grey",fg="black",font=("Comic Sans MS",15),command=texttospeech)
b1.place(x=200,y=400)


screen.mainloop()