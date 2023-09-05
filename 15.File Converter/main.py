import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from docx2pdf import convert
from pdf2docx import Converter

def wordToPdf():
    filePath = filedialog.askopenfilename(filetypes=[("Word Dosyası", "*.docx")])
    if filePath:
        try:
            convert(filePath)
            messagebox.showinfo("Başarılı", "Word dosyası PDF'ye dönüştürüldü.")
        except Exception as e:
            messagebox.showerror("Hata", f"Hata oluştu: {str(e)}")

def pdfToWord():
    filePath = filedialog.askopenfilename(filetypes=[("PDF Dosyası", "*.pdf")])
    if filePath:
        try:
            cv = Converter(filePath)
            outputPath = filedialog.asksaveasfilename(defaultextension=".docx", filetypes=[("Word Dosyası", "*.docx")])
            cv.convert(outputPath, start=0, end=None)
            cv.close()
            messagebox.showinfo("Başarılı", "PDF dosyası Word'e dönüştürüldü.")
        except Exception as e:
            messagebox.showerror("Hata", f"Hata oluştu: {str(e)}")

# Tkinter penceresini oluştur
window = tk.Tk()
window.geometry("300x100")
window.title("Dosya Dönüştürücü")

# "Word dosyasını PDF yap" butonu
word_to_pdf_button = tk.Button(window, text="Word dosyasını PDF yap", command=wordToPdf)
word_to_pdf_button.pack(pady=10)

# "PDF dosyasını Word yap" butonu
pdf_to_word_button = tk.Button(window, text="PDF dosyasını Word yap", command=pdfToWord)
pdf_to_word_button.pack(pady=10)

# Pencereyi çalıştır
window.mainloop()
