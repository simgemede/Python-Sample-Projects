import tkinter as tk
from tkinter import ttk
from tkinter import font

pencere = tk.Tk()
pencere.title("Yazı Tipi Oluşturma")

frame = tk.Frame(pencere)

def guncelleme(self):
    ornekFont.configure(family=yaziTipiSec_combobox.get())
    ornekFont.configure(size=yaziBoyutuSec_combobox.get())
    ornekFont.configure(weight=isBold())
    ornekFont.configure(slant=isItalic())
    ornekFont.configure(underline=isUnderline())
    ornekFont.configure(overstrike=isOverstrike())
    pencere.update()

def sonuc():
    ornekFont.configure(weight=isBold())
    ornekFont.configure(slant=isItalic())
    ornekFont.configure(underline=isUnderline())
    ornekFont.configure(overstrike=isOverstrike())

def isBold():
    if(Bold.get()):
        return "bold"
    else:
        return "normal"
def isItalic():
    if(Italic.get()):
        return 'italic'
    else:
        return 'roman'
def isUnderline():
    if(Underline.get()):
        return True
    else:
        return False
def isOverstrike():
    if(Overstrike.get()):
        return True
    else:
        return False

baslaFrame = tk.Frame(frame)
baslaFrame.grid(column=0,row=0)

secLabel = ttk.Label(baslaFrame, text="Bir yazı tipi stili seçin:")
secLabel.grid(column=0,row=0)
yaziTipiSec = tk.StringVar()
yaziTipiSec_combobox = ttk.Combobox(baslaFrame,width=30,textvariable=yaziTipiSec,state="readonly")
yaziTipiSec_combobox["values"] = font.families()
yaziTipiSec_combobox.grid(column=0,row=1)
yaziTipiSec_combobox.current(0)

boyutLabel = ttk.Label(baslaFrame, text="Bir yazı boyutu seçin:")
boyutLabel.grid(column=1,row=0)
yaziBoyutuSec = tk.StringVar()
yaziBoyutuSec_combobox = ttk.Combobox(baslaFrame, width=10, textvariable=yaziBoyutuSec,state="readonly")
yaziBoyutuSec_combobox["values"] = list(range(2,50))
yaziBoyutuSec_combobox.grid(column=1,row=1)
yaziBoyutuSec_combobox.current(0)

TextLabel = ttk.Label(frame, text="Görüntülenecek metin")
TextLabel.grid(column=0,row=2)

frame2 = tk.Frame(frame)
frame2.grid(column=0,row=1)

ornekText = tk.StringVar()
ornekText.set("Örnek Metin")
ornekText_entry = ttk.Entry(frame,width=30,textvariable=ornekText)
ornekText_entry.grid(column=0,row=3)

Bold = tk.IntVar()
Italic = tk.IntVar()
Underline = tk.IntVar()
Overstrike = tk.IntVar()
text = ["Bold", "Italic", "Underline", "Overstrike"]

checkbutton1 = tk.Checkbutton(frame2, text=text[0], variable=Bold, command=sonuc)
checkbutton1.grid(column=0,row=0, sticky=tk.W)
checkbutton2 = tk.Checkbutton(frame2, text=text[1], variable=Italic, command=sonuc)
checkbutton2.grid(column=1,row=0, sticky=tk.W)
checkbutton3 = tk.Checkbutton(frame2, text=text[2], variable=Underline, command=sonuc)
checkbutton3.grid(column=2,row=0, sticky=tk.W)
checkbutton4 = tk.Checkbutton(frame2, text=text[3], variable=Overstrike, command=sonuc)
checkbutton4.grid(column=3,row=0, sticky=tk.W)

LabelFrame = ttk.LabelFrame(frame, text='Örnek metin')
LabelFrame.grid(column=0, row=4)

ornekFont = font.Font(family=yaziTipiSec_combobox.get(),size=yaziBoyutuSec_combobox.get())

ornekLabel = ttk.Label(LabelFrame)
ornekLabel["textvariable"] = ornekText
ornekLabel["font"] = ornekFont
ornekLabel.grid(column=0,row=0)

yaziTipiSec_combobox.bind("<<ComboboxSelected>>", guncelleme)
yaziBoyutuSec_combobox.bind("<<ComboboxSelected>>", guncelleme)

frame.pack()
pencere.mainloop()