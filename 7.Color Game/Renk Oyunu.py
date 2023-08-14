import tkinter
import random

renkler = ["Red","Blue","Green","Black","White",
           "Yellow","Pink","Brown","Purple","Gray","Orange"]

skor = 0

kalan_sure = 90

def oyun_basla(event):
    if kalan_sure == 90:
        geri_sayım()
    renk_gir()

def renk_gir():
    global skor
    global kalan_sure
    if kalan_sure > 0:
        entry.focus_set()
        if entry.get().lower() == renkler[1].lower():
            skor += 1
        entry.delete(0,tkinter.END)
        random.shuffle(renkler)
        label.config(fg=str(renkler[1]),text=str(renkler[0]))
        skor_label.config(text="Skor:"+str(skor))


def geri_sayım():
    global kalan_sure
    if kalan_sure > 0:
        kalan_sure -= 1
        zaman_label.config(text="Kalan zaman:"+str(kalan_sure))
        zaman_label.after(1000,geri_sayım)

pencere = tkinter.Tk()
pencere.title("RENK OYUNU")
pencere.geometry("300x200")
pencere.resizable(False,False)

talimat = tkinter.Label(pencere,text="Renk girin.",
                        font=("Arial",12,"bold"))
talimat.pack()

skor_label = tkinter.Label(pencere,text="Başlamak için enter tuşuna basın")
skor_label.pack()

zaman_label = tkinter.Label(pencere,text="Kalan zaman:"+str(kalan_sure),font=("Arial",12))
zaman_label.pack()

label = tkinter.Label(pencere,font=("Arial",60))
label.pack()

entry = tkinter.Entry(pencere)
pencere.bind("<Return>",oyun_basla)
entry.pack()
entry.focus_set()

pencere.mainloop()