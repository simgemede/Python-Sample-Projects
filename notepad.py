from tkinter import *
from tkinter.filedialog import *

def ac():
    file = askopenfile(mode="r",filetypes=[("text files",".txt")])
    if file is not None:
        icerik = file.read()
    entry.insert(INSERT,icerik)

def kaydet():
    new_file = asksaveasfile(mode="w",filetypes=[("text files",".txt")])
    if new_file is None:
        return
    text = str(entry.get())
    new_file.write(text)
    new_file.close()

def yeni():
    entry.delete(1.0,END)

pencere = Tk()
pencere.geometry("400x500")
pencere.resizable(False,False)
pencere.title("Not Defteri")
pencere.config(bg="white")
frame_top = Frame(pencere)
frame_top.pack(padx=10,pady=5,anchor="nw")

ac_buton = Button(pencere,text="Aç",bg="white",command=ac)
ac_buton.place(x=5,y=10)

kaydet_buton = Button(pencere,text="Kaydet",bg="white",command=kaydet)
kaydet_buton.place(x=30,y=10)

yeni_buton = Button(pencere,text="Yeni",bg="white",command=yeni)
yeni_buton.place(x=77,y=10)

cikis_buton = Button(pencere,text="Çıkış",bg="white",command=exit)
cikis_buton.place(x=111,y=10)

entry = Text(pencere,wrap="word",bg="#efe5f6",font=("arial",15))
entry.pack(padx=5,pady=25,expand=True,fill="both")

pencere.mainloop()