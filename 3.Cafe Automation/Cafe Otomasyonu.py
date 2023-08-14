import tkinter as tk

pencere = tk.Tk()
pencere.geometry("1000x500")
pencere.title("Cafe Otomasyonu")
pencere.resizable(False,False)

toplamgor = tk.StringVar()

def Temizle():
    entryTK.delete(0, tk.END)
    entrySK.delete(0, tk.END)
    entryFK.delete(0, tk.END)
    entryLimonata.delete(0, tk.END)
    entryKola.delete(0, tk.END)
    entryGazoz.delete(0, tk.END)
    entrySu.delete(0, tk.END)

def Toplam():

    try: i1 = int(turkKahvesi.get())
    except: i1 = 0

    try: i2 = int(sutluKahve.get())
    except: i2 = 0

    try: i3 = int(filtreKahve.get())
    except: i3 = 0

    try: i4 = int(limonata.get())
    except: i4 = 0

    try: i5 = int(kola.get())
    except: i5 = 0

    try: i6 = int(gazoz.get())
    except: i6 = 0

    try: i7 = int(su.get())
    except: i7 = 0

    icecek1 = 15 * i1
    icecek2 = 17 * i2
    icecek3 = 15 * i3
    icecek4 = 17 * i4
    icecek5 = 15 * i5
    icecek6 = 10 * i6
    icecek7 = 3.5 * i7

    toplamPara = icecek1 + icecek2 + icecek3 + icecek4 + icecek5 + icecek6 + icecek7
    toplamgor.set(toplamPara)

label = tk.Label(pencere,text="Cafe Otomasyonu",bg="gray",fg="white",font=("arial",30),width="300",height="2")
label.pack()

frame1 = tk.Frame(pencere,bg="light gray",width=300,height=350)
frame1.place(x=10,y=120)

label1 = tk.Label(frame1,text="Menü",font=("Gabriola",30,"bold"),bg="light gray")
label1.place(x=100,y=0)

labelicecek1 = tk.Label(frame1,text="Türk Kahvesi..... 15 TL",fg="black",bg="light gray",font=("Lucida Calligraphy",13,"bold"))
labelicecek1.place(x=25,y=80)
labelicecek2 = tk.Label(frame1,text="Sütlü Kahve...... 17 TL",fg="black",bg="light gray",font=("Lucida Calligraphy",13,"bold"))
labelicecek2.place(x=25,y=110)
labelicecek3 = tk.Label(frame1,text="Filtre Kahve..... 15 TL",fg="black",bg="light gray",font=("Lucida Calligraphy",13,"bold"))
labelicecek3.place(x=25,y=140)
labelnokta = tk.Label(frame1,text="......................................",fg="black",bg="light gray",font=("Lucida Calligraphy",13,"bold"))
labelnokta.place(x=25,y=170)
labelicecek4 = tk.Label(frame1,text="Limonata.......... 17 TL",fg="black",bg="light gray",font=("Lucida Calligraphy",13,"bold"))
labelicecek4.place(x=25,y=200)
labelicecek5 = tk.Label(frame1,text="Kola.................. 15 TL",fg="black",bg="light gray",font=("Lucida Calligraphy",13,"bold"))
labelicecek5.place(x=25,y=230)
labelicecek6 = tk.Label(frame1,text="Gazoz................ 10 TL",fg="black",bg="light gray",font=("Lucida Calligraphy",13,"bold"))
labelicecek6.place(x=25,y=260)
labelicecek7 = tk.Label(frame1,text="Su...................... 3,5 TL",fg="black",bg="light gray",font=("Lucida Calligraphy",13,"bold"))
labelicecek7.place(x=25,y=290)

frame2 = tk.Frame(pencere,height=370,width=300)
frame2.pack()

turkKahvesi = tk.StringVar()
sutluKahve = tk.StringVar()
filtreKahve = tk.StringVar()
limonata = tk.StringVar()
kola = tk.StringVar()
gazoz = tk.StringVar()
su = tk.StringVar()
total = tk.StringVar()

labelTurkKahvesi = tk.Label(frame2,font=("arial",15,"bold"),text="Türk Kahvesi",fg="black",bg="light gray")
labelTurkKahvesi.place(x=20,y=50)
labelSutluKahve = tk.Label(frame2,font=("arial",15,"bold"),text="Sütlü Kahve",fg="black",bg="light gray")
labelSutluKahve.place(x=20,y=90)
labelFiltreKahve = tk.Label(frame2,font=("arial",15,"bold"),text="Filtre Kahve",fg="black",bg="light gray")
labelFiltreKahve.place(x=20,y=130)
labelLimonata = tk.Label(frame2,font=("arial",15,"bold"),text="Limonata",fg="black",bg="light gray")
labelLimonata.place(x=20,y=170)
labelKola = tk.Label(frame2,font=("arial",15,"bold"),text="Kola",fg="black",bg="light gray")
labelKola.place(x=20,y=210)
labelGazoz = tk.Label(frame2,font=("arial",15,"bold"),text="Gazoz",fg="black",bg="light gray")
labelGazoz.place(x=20,y=250)
labelSu = tk.Label(frame2,font=("arial",15,"bold"),text="Su",fg="black",bg="light gray")
labelSu.place(x=20,y=290)

entryTK = tk.Entry(frame2,font=("arial",15,"bold"),textvariable=turkKahvesi,width=5)
entryTK.place(x=160,y=50)
entrySK = tk.Entry(frame2,font=("arial",15,"bold"),textvariable=sutluKahve,width=5)
entrySK.place(x=160,y=90)
entryFK = tk.Entry(frame2,font=("arial",15,"bold"),textvariable=filtreKahve,width=5)
entryFK.place(x=160,y=130)
entryLimonata = tk.Entry(frame2,font=("arial",15,"bold"),textvariable=limonata,width=5)
entryLimonata.place(x=160,y=170)
entryKola = tk.Entry(frame2,font=("arial",15,"bold"),textvariable=kola,width=5)
entryKola.place(x=160,y=210)
entryGazoz = tk.Entry(frame2,font=("arial",15,"bold"),textvariable=gazoz,width=5)
entryGazoz.place(x=160,y=250)
entrySu = tk.Entry(frame2,font=("arial",15,"bold"),textvariable=su,width=5)
entrySu.place(x=160,y=290)

butonReset = tk.Button(frame2,fg="black",bg="light gray",font=("arial",15,"bold"),width=6,text="Temizle",command=Temizle)
butonReset.place(x=30,y=330)

butonToplam = tk.Button(frame2,fg="black",bg="light gray",font=("arial",15,"bold"),width=6,text="Toplam",command=Toplam)
butonToplam.place(x=125,y=330)

frame3 = tk.Frame(pencere,width=300,height=400)
frame3.place(x=700, y=120)

sonuc = tk.Label(frame3,text="Toplam",font=("calibri",20),bg="light gray")
sonuc.place(x=70, y=10)

entryToplam = tk.Entry(frame3,font=("arial",15,"bold"),textvariable=toplamgor,width=15,bg="light gray")
entryToplam.place(x=30, y=70)

pencere.mainloop()