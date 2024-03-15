import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from docx2pdf import convert
from pdf2docx import Converter

def wordToPdf():
    filePath = filedialog.askopenfilename(filetypes=[("Word File", "*.docx")])
    if filePath:
        try:
            convert(filePath)
            messagebox.showinfo("Successful", "The Word file has been converted to PDF.")
        except Exception as e:
            messagebox.showerror("Error", f"An error has occurred: {str(e)}")

def pdfToWord():
    filePath = filedialog.askopenfilename(filetypes=[("PDF File", "*.pdf")])
    if filePath:
        try:
            cv = Converter(filePath)
            outputPath = filedialog.asksaveasfilename(defaultextension=".docx", filetypes=[("Word File", "*.docx")])
            cv.convert(outputPath, start=0, end=None)
            cv.close()
            messagebox.showinfo("Successful", "The PDF file has been converted to Word.")
        except Exception as e:
            messagebox.showerror("Error", f"An error has occurred: {str(e)}")

# Tkinter penceresini oluştur
window = tk.Tk()
window.geometry("300x100")
window.title("File Converter")

# "Word dosyasını PDF yap" butonu
word_to_pdf_button = tk.Button(window, text="Make a word file a PDF", command=wordToPdf)
word_to_pdf_button.pack(pady=10)

# "PDF dosyasını Word yap" butonu
pdf_to_word_button = tk.Button(window, text="Make a PDF file a Word", command=pdfToWord)
pdf_to_word_button.pack(pady=10)

# Pencereyi çalıştır
window.mainloop()
