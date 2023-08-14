import tkinter as tk
from tkinter import ttk

pencere = tk.Tk()
pencere.geometry("1350x700")
pencere.title("Öğrenci Bilgi İşlem Arayüzü")
pencere.resizable(False,False)

baslikLabel = tk.Label(pencere,text="Öğrenci Bilgi İşlem Arayüzü",font=("arial",30,"bold"),border=12,bg="light gray",fg="black",relief=tk.FLAT)
baslikLabel.pack(side=tk.TOP,fill=tk.X)

labelFrame = tk.LabelFrame(pencere,text="",font=("Arial",20),bg="light gray",fg="black",relief=tk.FLAT)
labelFrame.place(x=10,y=80,width=420,height=610)

dataFrame = tk.Frame(pencere,bd=12,bg="light gray",relief=tk.FLAT)
dataFrame.place(x=440,y=80,width=900,height=610)

baslik_label = tk.Label(labelFrame,text="Bilgi Girişi",font=("arial",17),bg="light gray")
baslik_label.place(x=150,y=10)

tcKimlikNo_label = tk.Label(labelFrame,text="TC Kimlik No",font=("arial",12),bg="light gray")
tcKimlikNo_label.place(x=20,y=60)

tcKimlikNo_entry = tk.Entry(labelFrame,bd=7,font=("arial",12),bg="white",relief=tk.FLAT)
tcKimlikNo_entry.place(x=150,y=60)

isim_label = tk.Label(labelFrame,text="İsim",font=("arial",12),bg="light gray")
isim_label.place(x=20,y=110)

isim_entry = tk.Entry(labelFrame,bd=7,font=("arial",12),bg="white",relief=tk.FLAT)
isim_entry.place(x=150,y=110)

soyisim_label = tk.Label(labelFrame,text="Soyisim",font=("arial",12),bg="light gray")
soyisim_label.place(x=20,y=160)

soyisim_entry = tk.Entry(labelFrame,bd=7,font=("arial",12),bg="white",relief=tk.FLAT)
soyisim_entry.place(x=150,y=160)

sinif_label = tk.Label(labelFrame,text="Sınıf",font=("arial",12),bg="light gray")
sinif_label.place(x=20,y=210)

sinif_entry = tk.Entry(labelFrame,bd=7,font=("arial",12),bg="white",relief=tk.FLAT)
sinif_entry.place(x=150,y=210)

bölüm_label = tk.Label(labelFrame,text="Bölüm",font=("arial",12),bg="light gray")
bölüm_label.place(x=20,y=260)

bölüm_entry = tk.Entry(labelFrame,bd=7,font=("arial",12),bg="white",relief=tk.FLAT)
bölüm_entry.place(x=150,y=260)

iletisim_label = tk.Label(labelFrame,text="İletişim",font=("arial",12),bg="light gray")
iletisim_label.place(x=20,y=310)

iletisim_entry = tk.Entry(labelFrame,bd=7,font=("arial",12),bg="white",relief=tk.FLAT)
iletisim_entry.place(x=150,y=310)

veliİletisim_label = tk.Label(labelFrame,text="Veli İletişim",font=("arial",12),bg="light gray")
veliİletisim_label.place(x=20,y=360)

veliİletisim_entry = tk.Entry(labelFrame,bd=7,font=("arial",12),bg="white",relief=tk.FLAT)
veliİletisim_entry.place(x=150,y=360)

cinsiyet_label = tk.Label(labelFrame,text="Cinsiyet",font=("arial",12),bg="light gray")
cinsiyet_label.place(x=20,y=410)

cinsiyet_entry = ttk.Combobox(labelFrame,font=("arial",12))
cinsiyet_entry["values"] = ("Erkek","Kadın")
cinsiyet_entry.place(x=150,y=410)

adres_label = tk.Label(labelFrame,text="Adres",font=("arial",12),bg="light gray")
adres_label.place(x=20,y=460)

adres_entry = tk.Text(labelFrame,bd=7,width=20,height=4,font=("arial",12),bg="white",relief=tk.FLAT)
adres_entry.place(x=150,y=460)

ekleButon = tk.Button(labelFrame,bg="white",fg="black",text="Ekle",font=("arial",12),width=5,relief=tk.FLAT)
ekleButon.place(x=100,y=560)

güncellemeButon = tk.Button(labelFrame,bg="white",fg="black",text="Güncelleme",font=("arial",12),width=10,relief=tk.FLAT)
güncellemeButon.place(x=165,y=560)

silButon = tk.Button(labelFrame,bg="white",fg="black",text="Sil",font=("arial",12),width=5,relief=tk.FLAT)
silButon.place(x=280,y=560)

arama_frame = tk.Frame(dataFrame,bg="white",bd=10,relief=tk.SUNKEN)
arama_frame.pack(side=tk.TOP,fill=tk.X)

arama_label = tk.Label(arama_frame,text="Arama Motoru",bg="white",font=("arial",12))
arama_label.grid(row=0,column=0)

arama_cm = ttk.Combobox(arama_frame,font=("arial",12),state="readonly")
arama_cm["values"] = ("TC Kimlik No","İsim","Soyisim","Sınıf","Bölüm","İletişim","Veli İletişim","Cinsiyet","Adres")
arama_cm.grid(row=0,column=1,padx=12,pady=2)

arama_buton = tk.Button(arama_frame,text="Ara",font=("arial",12),width=9)
arama_buton.grid(row=0,column=2,padx=12,pady=2)

arama_buton = tk.Button(arama_frame,text="Tümünü Göster",font=("arial",12),width=15)
arama_buton.grid(row=0,column=3,padx=12,pady=2)

main_frame = tk.Frame(dataFrame,bg="white",bd=11,relief=tk.SUNKEN)
main_frame.pack(fill=tk.BOTH,expand=True)

x_scroll = tk.Scrollbar(main_frame,orient=tk.VERTICAL)
y_scroll = tk.Scrollbar(main_frame,orient=tk.HORIZONTAL)

ogrenciBilgileriTrw = ttk.Treeview(main_frame,columns=("TC Kimlik No","İsim","Soyisim","Sınıf","Bölüm","İletişim","Veli İletişim","Cinsiyet","Adres"),yscrollcommand=y_scroll.set,xscrollcommand=x_scroll.set)

y_scroll.config(command=ogrenciBilgileriTrw.yview)
x_scroll.config(command=ogrenciBilgileriTrw.xview)

y_scroll.pack(side=tk.RIGHT,fill=tk.Y)
x_scroll.pack(side=tk.BOTTOM,fill=tk.X)

ogrenciBilgileriTrw.heading("TC Kimlik No",text="TC Kimlik No")
ogrenciBilgileriTrw.heading("İsim",text="İsim")
ogrenciBilgileriTrw.heading("Soyisim",text="Soyisim")
ogrenciBilgileriTrw.heading("Sınıf",text="Sınıf")
ogrenciBilgileriTrw.heading("Bölüm",text="Bölüm")
ogrenciBilgileriTrw.heading("İletişim",text="İletişim")
ogrenciBilgileriTrw.heading("Veli İletişim",text="Veli İletişim")
ogrenciBilgileriTrw.heading("Cinsiyet",text="Cinsiyet")
ogrenciBilgileriTrw.heading("Adres",text="Adres")

ogrenciBilgileriTrw.column("TC Kimlik No",width=100)
ogrenciBilgileriTrw.column("İsim",width=70)
ogrenciBilgileriTrw.column("Soyisim",width=80)
ogrenciBilgileriTrw.column("Sınıf",width=70)
ogrenciBilgileriTrw.column("Bölüm",width=70)
ogrenciBilgileriTrw.column("İletişim",width=100)
ogrenciBilgileriTrw.column("Veli İletişim",width=100)
ogrenciBilgileriTrw.column("Cinsiyet",width=100)
ogrenciBilgileriTrw.column("Adres",width=80)

ogrenciBilgileriTrw["show"] = "headings"

ogrenciBilgileriTrw.pack(fill=tk.BOTH,expand=True)

pencere.mainloop()