import tkinter as tk

pencere = tk.Tk()
pencere.geometry("380x450")
pencere.title("Hesap Makinesi")
pencere.config(background="gray")

fonksiyon = tk.StringVar()
operator = ""

def tiklabuton(numara):
    global operator
    operator = operator + str(numara)
    fonksiyon.set(operator)

def islembuton():
    global operator
    islem = str(eval(operator))
    fonksiyon.set(islem)
    operator = ""

def silmebuton():
    fonksiyon.set("")

entry = tk.Entry(pencere,font=("Arial",15,"bold"),textvariable=fonksiyon,width=30,borderwidth=5,background="white",justify="right")
entry.pack()

buton1=tk.Button(pencere,padx=14,pady=14,bd=4,bg='white',command=lambda:tiklabuton(1),text="1",font=("Arial",12,'bold'))
buton1.place(x=10,y=100)

buton2=tk.Button(pencere,padx=14,pady=14,bd=4,bg='white',command=lambda:tiklabuton(2),text="2",font=("Arial",12,'bold'))
buton2.place(x=10,y=170)

buton3=tk.Button(pencere,padx=14,pady=14,bd=4,bg='white',command=lambda:tiklabuton(3),text="3",font=("Arial",12,'bold'))
buton3.place(x=10,y=240)

buton4=tk.Button(pencere,padx=14,pady=14,bd=4,bg='white',command=lambda:tiklabuton(4),text="4",font=("Arial",12,'bold'))
buton4.place(x=75,y=100)

buton5=tk.Button(pencere,padx=14,pady=14,bd=4,bg='white',command=lambda:tiklabuton(5),text="5",font=("Arial",12,'bold'))
buton5.place(x=75,y=170)

buton6=tk.Button(pencere,padx=14,pady=14,bd=4,bg='white',command=lambda:tiklabuton(6),text="6",font=("Arial",12,'bold'))
buton6.place(x=75,y=240)

buton7=tk.Button(pencere,padx=14,pady=14,bd=4,bg='white',command=lambda:tiklabuton(7),text="7",font=("Arial",12,'bold'))
buton7.place(x=140,y=100)

buton8=tk.Button(pencere,padx=14,pady=14,bd=4,bg='white',command=lambda:tiklabuton(8),text="8",font=("Arial",12,'bold'))
buton8.place(x=140,y=170)

buton9=tk.Button(pencere,padx=14,pady=14,bd=4,bg='white',command=lambda:tiklabuton(9),text="9",font=("Arial",12,'bold'))
buton9.place(x=140,y=240)

buton0=tk.Button(pencere,padx=14,pady=14,bd=4,bg='white',command=lambda:tiklabuton(0),text="0",font=("Arial",12,'bold'))
buton0.place(x=10,y=310)

butonnokta=tk.Button(pencere,padx=47,pady=14,bd=4,bg='white',command=lambda:tiklabuton("."),text=".",font=("Arial",12,'bold'))
butonnokta.place(x=75,y=310)

butontoplama=tk.Button(pencere,padx=14,pady=14,bd=4,bg='white',text="+",command=lambda:tiklabuton("+"),font=("Arial",12,'bold'))
butontoplama.place(x=205,y=100)

butoncikarma=tk.Button(pencere,padx=14,pady=14,bd=4,bg='white',text="-",command=lambda:tiklabuton("-"),font=("Arial",12,'bold'))
butoncikarma.place(x=205,y=170)

butoncarpma=tk.Button(pencere,padx=14,pady=14,bd=4,bg='white',text="*",command=lambda:tiklabuton("*"),font=("Arial",12,'bold'))
butoncarpma.place(x=205,y=240)

butonbolme=tk.Button(pencere,padx=14,pady=14,bd=4,bg='white',text="/",command=lambda:tiklabuton("/"),font=("Arial",12,'bold'))
butonbolme.place(x=205,y=310)

butonsil=tk.Button(pencere,padx=14,pady=119,bd=4,bg='white',text="CE",command=silmebuton,font=("Arial",12,'bold'))
butonsil.place(x=270,y=100)

butonislem=tk.Button(pencere,padx=151,pady=14,bd=4,bg='white',command=islembuton,text="=",font=("Arial",12,'bold'))
butonislem.place(x=10,y=380)

pencere.mainloop()
