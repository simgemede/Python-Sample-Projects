import random
import tkinter as tk
from tkinter import messagebox

def random_sifre():
    harf = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
               'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    harff = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    sembol = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "+", "=", "|", "{", "}",
               "[", "]", ":", ";", "''", ">", "<", ",", ".", "?", "/", "\\", "~", "`", ]

    password_entry.insert(random.randint(0, 10), random.randint(0,10))
    password_entry.insert(random.randint(0, 10), random.choice(harf))
    password_entry.insert(random.randint(0, 10), random.choice(harff))
    password_entry.insert(random.randint(0, 10), random.randint(0,10))
    password_entry.insert(random.randint(0, 10), random.choice(harf))
    password_entry.insert(random.randint(0, 10), random.choice(harff))
    password_entry.insert(random.randint(0, 10), random.randint(0,10))
    password_entry.insert(random.randint(0, 10), random.choice(harf))
    password_entry.insert(random.randint(0, 10), random.choice(sembol))

def giris():
    if len(password_entry.get()) == 0 or len(email_entry.get()) == 0 or len(web_entry.get()) == 0:
        messagebox.showinfo("UYARI!", "Boş bir alan bırakmayın!")

    else:
        data_list = []
        web = web_entry.get()
        email = email_entry.get()
        password = password_entry.get()
        data_list.append(web)
        data_list.append(email)
        data_list.append(password)

        with open("passworddata.txt", "a") as opn:
            opn.write(" | ".join(data_list))
            opn.write("\n")

        messagebox.showinfo("","Giriş başarılı.")
        web_entry.delete(0,"end")
        password_entry.delete(0,"end")

pencere = tk.Tk()
pencere.title("Creating a Password")
pencere.resizable(False,False)
pencere.geometry("300x450")

img = tk.PhotoImage(file="Apps-preferences-desktop-user-password-icon.png")
label_image = tk.Label(pencere,image=img)
label_image.place(x=30,y=3,width=250,height=250)
website_label = tk.Label(text="Website:")
website_label.place(x=20,y=220)
email_label = tk.Label(text="Username: ")
email_label.place(x=20,y=250)
password_label = tk.Label(text="Password: ", padx=0, pady=0)
password_label.place(x=20,y=280)

web_entry = tk.Entry(width=28)
web_entry.place(x=90,y=220)
web_entry.focus()
email_entry = tk.Entry(width=28)
email_entry.place(x=90,y=250)
email_entry.insert(0,"simgemede2510@gmail.com")
password_entry = tk.Entry(width=28)
password_entry.place(x=90,y=280)

button_pass = tk.Button(text="Rastgele şifre",command=random_sifre)
button_pass.place(x=150,y=320)
button_pass = tk.Button(text="Giriş",command=giris)
button_pass.place(x=90,y=320)

pencere.mainloop()