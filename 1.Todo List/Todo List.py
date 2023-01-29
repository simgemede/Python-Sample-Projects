import tkinter
import tkinter.messagebox

def ekle():
    entryisi = entry.get()
    if entryisi != "":
        listbox.insert(tkinter.END,entryisi)
        entry.delete(0,tkinter.END)
    else:
        tkinter.messagebox.showinfo(title="", message="Bir şey yazmadın!")

def sil():
    try:
        listboxx = listbox.curselection()[0]
        listbox.delete(listboxx)
    except IndexError as Error:
        tkinter.messagebox.showinfo(title="", message="Bir şey seçmelisin!")


pencere = tkinter.Tk()
pencere.title("Yapılacaklar Listesi")
pencere.geometry("350x320")

frame = tkinter.Frame(pencere)
frame.pack()

listbox = tkinter.Listbox(frame,height=15,width=40,bg="black",fg="white")
listbox.pack(side=tkinter.LEFT)

entry = tkinter.Entry(pencere,width=50,bg="white",fg="black")
entry.pack()

buton = tkinter.Button(pencere,text="Ekle",width=20,bg="black",fg="white",command=ekle)
buton.pack(anchor=tkinter.CENTER)
buton1 = tkinter.Button(pencere,text="Sil",width=20,bg="black",fg="white",command=sil)
buton1.pack(anchor=tkinter.CENTER)

pencere.mainloop()