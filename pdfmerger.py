import pypdf as pd  
import tkinter as tk
from tkinter import Label, filedialog

class pdfmerger:
    def __init__(self, root):
        self.root=root
        self.root.title("PDF Merger")
        self.root.geometry("400x200")
        self.files = []
        self.window = tk.Label(self.root, text="Select PDF files to merge", font = "Arial 15 bold")
        self.window.pack(pady=20)
        self.add_button = tk.Button(self.root, text = "Add PDF", command = self.add_files)
        self.add_button.pack(pady=10)
        self.merge_button = tk.Button(self.root, text = "Merge PDFs", command = self.merge_files)
        self.merge_button.pack(pady=10)
        self.status = tk.Label(self.root,text="", fg="green", font = "Arial 10")
        self.status.pack(pady=10)
        
    def add_files(self):
     self.files = filedialog.askopenfilenames(initialdir="/", title="Select PDF Files", filetypes=[("PDF files", "*.pdf")])
     if self.files:
        self.status.config(text = f"{len(self.files)} files selected", fg= "green")
        self.merge_button.config(state=tk.NORMAL)
     else:
        self.status.config(text="No files selected.")
        self.merge_button.config(state=tk.DISABLED)

    def merge_files(self):
     merger=pd.PdfWriter()
     for pdf in self.files:
        merger.append(pdf)

     output_file = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("Pdf file", "*.pdf")])
     if output_file:
        merger.write(output_file)
        self.status.config(text="PDFs merged successfully!", fg="green")
        merger.close()
     else:
        self.status.config(text="Save cancelled", fg="red")

if __name__ == "__main__":
    root = tk.Tk()
    app = pdfmerger(root)
    root.mainloop()
