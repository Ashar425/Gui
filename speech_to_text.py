import tkinter as tk
import speech_recognition as sr
from tkinter import messagebox

screen=tk.Tk()
screen.title("Speech to Text Converter")
screen.configure(bg="black")
screen.geometry("800x500")

recognizer=sr.Recognizer()

def speechtotext():
    try:
        with sr.Microphone() as source:
            messagebox.showinfo("Speak","Start speaking after clicking OK")
            recognizer.adjust_for_ambient_noise(source,duration=1)
            recognizer.pause_threshold=2
            audio=recognizer.listen(source,timeout=5,phrase_time_limit=20)

        text=recognizer.recognize_google(audio)
        t1.delete("1.0","end")
        t1.insert("1.0",text)

    except sr.WaitTimeoutError:
        messagebox.showerror("Error","You did not start speaking in time")

    except sr.UnknownValueError:
        messagebox.showerror("Error","Speech could not be understood")

    except sr.RequestError:
        messagebox.showerror("Error","Internet connection is required")

    except OSError:
        messagebox.showerror("Error","Microphone is not available")

def cleartext():
    t1.delete("1.0","end-1c")

def savetext():
    speechdata=t1.get("1.0","end-1c")
    file=open("speech.txt","a")
    file.write(speechdata)
    file.write("\n")
    file.close()
    messagebox.showinfo("Text saved","your text got saved succesfully")

l1=tk.Label(text="Speech to Text Converter",width=30,height=1,bg="grey",fg="white",font=("Arial",20))
l1.place(x=100,y=70)

l2=tk.Label(text="Click the button and start speaking",width=30,height=1,bg="teal",fg="black",font=("Comic Sans MS",12))
l2.place(x=200,y=130)

t1=tk.Text(width=30,height=5,bg="turquoise",fg="black",font=("Arial",20))
t1.place(x=150,y=180)

b1=tk.Button(text="Start Recording",width=15,height=1,bg="grey",fg="black",font=("Comic Sans MS",15),command=speechtotext)
b1.place(x=300,y=400)

b2=tk.Button(text="Save Text",width=15,height=1,bg="green",fg="black",font=("Comic Sans MS",15),command=savetext)
b2.place(x=100,y=400)

b3=tk.Button(text="Clear Text",width=15,height=1,bg="red",fg="black",font=("comic Sans MS",15),command=cleartext)
b3.place(x=500,y=400)

screen.mainloop()