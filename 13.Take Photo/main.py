import tkinter as tk
import cv2
import uuid # Fotoya rastgele isim için gerekli kütüphane

def takePhoto():
    ret, frame = video_capture.read()
    if ret:
        fileName = str(uuid.uuid4()) + ".png"  # Rastgele isim oluştur
        cv2.imwrite(fileName, frame)
        print(f"Fotoğraf kaydedildi: {fileName}")

def exitApp():
    video_capture.release()
    window.quit()

window = tk.Tk()
window.title("FotoÇek")
window.geometry("400x300")
window.resizable(False, False)

video_source = 0
video_capture = cv2.VideoCapture(video_source)

frame = tk.Frame(window)
frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

btn_takePhoto = tk.Button(frame, text="Fotoğraf Çek", width=20, command=takePhoto)
btn_takePhoto.pack(padx=20, pady=10)

btn_exit = tk.Button(frame, text="Çıkış", width=20, command=exitApp)
btn_exit.pack(padx=20, pady=10)

window.mainloop()
