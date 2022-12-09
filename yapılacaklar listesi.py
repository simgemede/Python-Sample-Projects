import tkinter
from tkinter import END,ANCHOR

pencere = tkinter.Tk()
pencere.title("Yapılacaklar Listesi")
pencere.geometry("400x365")
pencere.resizable(False,False)
pencere.config(bg="#1faee9")

def Ekle():
    if entry.get() == "":
        pass
    else:
        listbox.insert(END,entry.get())
        entry.delete(0,END)

def Kaldir():
    listbox.delete(0,END)

def Temizle():
    entry.delete(0,END)

def Paylas():
    with open("yapılacaklarListesi.txt","w") as f:
        listbox1 = listbox.get(0,END)
        for item in listbox1:
            if item.endswith("\n"):
                f.write(item)
            else:
                f.write(item + "\n")

girisFrame = tkinter.Frame(pencere,bg="#1faee9")
girisFrame.pack()
cikisFrame = tkinter.Frame(pencere,bg="#1faee9")
cikisFrame.pack()
butonFrame = tkinter.Frame(pencere,bg="#1faee9")
butonFrame.pack()

entry = tkinter.Entry(girisFrame,width=40,borderwidth=3)
entry.grid(row=0,column=0,padx=5,pady=5)
buton = tkinter.Button(girisFrame,text="Ekle",borderwidth=3,bg="#f7fafc",command=Ekle)
buton.grid(row=0,column=1,padx=5,pady=5)

scrollbar = tkinter.Scrollbar(cikisFrame)
listbox = tkinter.Listbox(cikisFrame,height=17,width=45,borderwidth=3)
scrollbar.config(command=listbox.yview)
listbox.grid(row=0,column=0)
scrollbar.grid(row=0,column=1,sticky="NS")

kaldirButon = tkinter.Button(butonFrame,text="Kaldır",borderwidth=3,command=Kaldir)
kaldirButon.grid(row=0,column=0,padx=2,pady=10)
temizleButon = tkinter.Button(butonFrame,text="Temizle",borderwidth=3,command=Temizle)
temizleButon.grid(row=0,column=1,padx=2,pady=10)
paylasButon = tkinter.Button(butonFrame,text="Paylaş",borderwidth=3,command=Paylas)
paylasButon.grid(row=0,column=2,padx=2,pady=10)
CikisButon = tkinter.Button(butonFrame,text="Çıkış",borderwidth=3,command=pencere.destroy)
CikisButon.grid(row=0,column=3,padx=2,pady=10)

pencere.mainloop()
