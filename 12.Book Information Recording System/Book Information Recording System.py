import tkinter
from tkinter import filedialog
import datetime

pencere = tkinter.Tk()
pencere.geometry("800x550")
pencere.resizable(False,False)
pencere.title("Book Information Recording System")
pencere.iconbitmap("blue_book.ico")

bg = tkinter.PhotoImage("paper-753508_1920.jpg")
img_label = tkinter.Label(pencere, image=bg)
img_label.place(x=0, y=0)

simdi = datetime.datetime.now()
d1 = tkinter.IntVar()

def kaydet_fonk():
    metin_dosyası = filedialog.askopenfile(initialdir="c:/", title="Dosya Metnini Aç", filetypes=(("Metin Dosyaları", "*.txt"))) #bir bak
    metin_dosyası = open(metin_dosyası, "w")
    metin_dosyası.write(baslik_entry.get(1.0, "end") + yazar_entry.get(1.0, "end") + ozet_entry.get(1.0, "end"))
    kaydet_label = tkinter.Label(pencere, text=baslik_entry.get(1.0,"end") + kaydedildi)
    kaydet_label.place(x=20, y=160)
    pencere.after(2000, kaydet_label.destroy)

def temizle_fonk():
    baslik_entry.delete(1.0, "end")
    yazar_entry.delete(1.0, "end")
    ozet_entry.delete(1.0, "end")
    temizle_label = tkinter.Label(pencere, text="Yazılar temizlendi")
    temizle_label.place(x=20, y=160)
    pencere.after(2000, temizle_label)

def ac_fonk():
    metin_dosyası = filedialog.askopenfile(initialdir="c:/", title="Dosya Metnini Aç",filetypes=(("Metin Dosyaları", "*.txt")))
    metin_dosyası = open(metin_dosyası, "r")
    metin_dosyası = metin_dosyası.read()
    ozet_entry.insert("end", metin_dosyası)
    metin_dosyası.close()
    ac_label = tkinter.Label(pencere, text="Açıldı")
    ac_label.place(x=20, y=160)
    pencere.after(2000, ac_label.destroy)

def zaman_ekle():
    if(d1.get()==1):
        ozet_entry.insert(1.0, simdi)
    else:
        pass

baslik = tkinter.Label(pencere, text="Başlık", fg="black", font="bold")
baslik.place(x=20, y=10)

baslik_entry = tkinter.Text(pencere, bd=5, height=1, width=82, bg="black", fg="white")
baslik_entry.place(x=100, y=10)

yazar = tkinter.Label(pencere, text="Yazar", fg="black", font="bold")
yazar.place(x=20, y=50)

yazar_entry = tkinter.Text(pencere, bd=5, height=1, width=82, bg="black", fg="white")
yazar_entry.place(x=100, y=50)

ozet = tkinter.Label(pencere, text="Özet", fg="black", font="bold")
ozet.place(x=20, y=90)

ozet_entry = tkinter.Text(pencere,bd=5, width=82, bg="black", fg="white")
ozet_entry.place(x=100, y=90)

zaman = tkinter.Checkbutton(pencere, text= "Zamanı ekle", font="bold", variable=d1, command=zaman_ekle, onvalue=1, offvalue=0)
zaman.place(x=100, y=500)

kaydet_buton = tkinter.Button(text="Kaydet", command=kaydet_fonk)
kaydet_buton.place(x=300,y=500)

temizle_buton = tkinter.Button(text="Temizle", command=temizle_fonk)
temizle_buton.place(x=360, y=500)

ac_buton = tkinter.Button(text="Aç", command=ac_fonk)
ac_buton.place(x=420, y=500)

pencere.mainloop()