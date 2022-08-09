import random
from tkinter import *

def fonk():
    x = random.randint(1, 90)
    q = random.randint(1, 90)
    w = random.randint(1, 90)
    e = random.randint(1, 90)
    r = random.randint(1, 90)
    t = random.randint(1, 90)
    numara1.set(x)
    numara2.set(q)
    numara3.set(w)
    numara4.set(e)
    numara5.set(r)
    numara6.set(t)
    return

pencere = Tk()
pencere.geometry("800x210")
frame = Frame(pencere)
frame.pack()
pencere.title("Sayısal Loto Sayı Üretme Robotu")

numara1 = StringVar()
numara2 = StringVar()
numara3 = StringVar()
numara4 = StringVar()
numara5 = StringVar()
numara6 = StringVar()

frame1 = Frame(pencere)
frame1.pack(side=TOP)

label1 = Label(frame1, text="Sayısal Loto Sayı Üretme Robotu",font=("Calibri,46"),fg="blue")
label1.pack(side=TOP)

frame2 = Frame(pencere)
frame2.pack(side=TOP)

entry = Entry(frame1,textvariable=numara1,bd=20,insertwidth=1,font=("Arial", 30), justify='center', width=4)
entry.pack(side=LEFT)
entry.config(state="readonly")
entry1 = Entry(frame1,textvariable=numara2,bd=20,insertwidth=1,font=("Arial", 30), justify='center', width=4)
entry1.pack(side=LEFT)
entry1.config(state="readonly")
entry2 = Entry(frame1,textvariable=numara3,bd=20,insertwidth=1,font=("Arial", 30), justify='center', width=4)
entry2.pack(side=LEFT)
entry2.config(state="readonly")
entry3 = Entry(frame1,textvariable=numara4,bd=20,insertwidth=1,font=("Arial", 30), justify='center', width=4)
entry3.pack(side=LEFT)
entry3.config(state="readonly")
entry4 = Entry(frame1,textvariable=numara5,bd=20,insertwidth=1,font=("Arial", 30), justify='center', width=4)
entry4.pack(side=LEFT)
entry4.config(state="readonly")
entry5 = Entry(frame1,textvariable=numara6,bd=20,insertwidth=1,font=("Arial", 30), justify='center', width=4)
entry5.pack(side=LEFT)
entry5.config(state="readonly")
