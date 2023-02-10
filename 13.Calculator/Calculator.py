import tkinter as tk
from tkinter import *

pencere = tk.Tk()
pencere.geometry("230x240")
pencere.title("Calculator")
pencere.resizable(False, False)

ent = tk.Entry(pencere, width=20, borderwidth=3, relief=SUNKEN)
ent.grid(padx=10, pady=10, sticky="w", row=0, column=0)

def esittirFonk():

    try:

        if ent.get() == "":
            ent.insert("end","error")
        elif ent.get()[0] == "0":
            ent.delete(0,"end")
            ent.insert("end","error")
        else:
            fonk = ent.get()
            fonk = eval(fonk)
            ent.insert("end","=")
            ent.insert("end",fonk)
    except SyntaxError:
        ent.insert("end","invalid input")

temizle = tk.Button(pencere, text="C", width=6, command=lambda:ent.delete(0,"end"), bg="red", borderwidth=2, relief=RAISED)
temizle.grid(padx=160, pady=10, sticky="w", row=0)


dokuz = tk.Button(pencere, text="9", width=6, command=lambda:ent.insert("end","9"), borderwidth=2, relief=RAISED)
dokuz.grid(padx=15, pady=5, sticky="w", row=1)

sekiz = tk.Button(pencere, text="8", width=6, command=lambda:ent.insert("end","8"), borderwidth=2, relief=RAISED)
sekiz.grid(padx=65, pady=5, sticky="w", row=1)

yedi = tk.Button(pencere, text="7", width=6, command=lambda:ent.insert("end","7"), borderwidth=2, relief=RAISED)
yedi.grid(padx=115, pady=5, sticky="w", row=1)

arti = tk.Button(pencere, text="+", width=6, command=lambda:ent.insert("end","+"), borderwidth=2, relief=RAISED)
arti.grid(padx=165, pady=5, sticky="w", row=1)


alti= tk.Button(pencere, text="6", width=6, command=lambda:ent.insert("end","6"), borderwidth=2, relief=RAISED)
alti.grid(padx=15, pady=5, sticky="w", row=2)

bes = tk.Button(pencere, text="5", width=6, command=lambda:ent.insert("end","5"), borderwidth=2, relief=RAISED)
bes.grid(padx=65, pady=5, sticky="w", row=2)

dort = tk.Button(pencere, text="4", width=6, command=lambda:ent.insert("end","4"), borderwidth=2, relief=RAISED)
dort.grid(padx=115, pady=5, sticky="w", row=2)

eksi = tk.Button(pencere, text="-", width=6, command=lambda:ent.insert("end","-"), borderwidth=2, relief=RAISED)
eksi.grid(padx=165, pady=5, sticky="w", row=2)


uc= tk.Button(pencere, text="3", width=6, command=lambda:ent.insert("end","3"), borderwidth=2, relief=RAISED)
uc.grid(padx=15, pady=5, sticky="w", row=3)

iki = tk.Button(pencere, text="2", width=6, command=lambda:ent.insert("end","2"), borderwidth=2, relief=RAISED)
iki.grid(padx=65, pady=5, sticky="w", row=3)

bir = tk.Button(pencere, text="1", width=6, command=lambda:ent.insert("end","1"), borderwidth=2, relief=RAISED)
bir.grid(padx=115, pady=5, sticky="w", row=3)

carpma = tk.Button(pencere, text="*", width=6, command=lambda:ent.insert("end","*"), borderwidth=2, relief=RAISED)
carpma.grid(padx=165, pady=5, sticky="w", row=3)


sifir = tk.Button(pencere, text="0", width=6, command=lambda:ent.insert("end","6"), borderwidth=2, relief=RAISED)
sifir.grid(padx=15, pady=5, sticky="w", row=4)

ciftSifir = tk.Button(pencere, text="00", width=6, command=lambda:ent.insert("end","5"), borderwidth=2, relief=RAISED)
ciftSifir.grid(padx=65, pady=5, sticky="w", row=4)

virgul = tk.Button(pencere, text=",", width=6, command=lambda:ent.insert("end","4"), borderwidth=2, relief=RAISED)
virgul.grid(padx=115, pady=5, sticky="w", row=4)

bolme = tk.Button(pencere, text="/", width=6, command=lambda:ent.insert("end","-"), borderwidth=2, relief=RAISED)
bolme.grid(padx=165, pady=5, sticky="w", row=4)


esittir = tk.Button(pencere, text="=", width=18, command=esittirFonk, borderwidth=2, relief=RAISED)
esittir.grid(padx=15, pady=5, sticky="w", row=5)

yuzde = tk.Button(pencere, text="%", width=6, command=lambda:ent.insert("end","%"), borderwidth=2, relief=RAISED)
yuzde.grid(padx=165, pady=5, sticky="w", row=5)

pencere.mainloop()