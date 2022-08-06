from time import strftime
from tkinter import Label, Tk

pencere = Tk()
pencere.title("")
pencere.geometry("200x80")
pencere.resizable(False, False)

saat_label = Label(
    pencere, bg="black", fg="white", font=("Arial", 30, "bold"), relief="flat"
)
saat_label.place(x=20, y=20)


def etiketi_güncelle():

    zaman = strftime("%H: %M: %S\n %d-%m-%Y ")
    saat_label.configure(text=zaman)
    saat_label.after(80, etiketi_güncelle)
    saat_label.pack(anchor="center")


etiketi_güncelle()
pencere.mainloop()
