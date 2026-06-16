import tkinter as tk
from tkinter import filedialog, messagebox
from PyPDF2 import PdfMerger

class PDFMergerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PDF Merger")
        self.root.geometry("600x400")
        self.root.configure(bg="#f0f4f7")
        
        self.pdf_files = []
        
        self.create_widgets()
        
    def create_widgets(self):
        # Title label
        title_label = tk.Label(self.root, text="PDF Merger", font=("Arial", 20), bg="#f0f4f7", fg="#333")
        title_label.pack(pady=10)
        
        # Listbox to display selected PDF files
        self.listbox = tk.Listbox(self.root, selectmode=tk.MULTIPLE, width=50, height=10, font=("Arial", 12))
        self.listbox.pack(pady=10)
        
        # Buttons Frame
        button_frame = tk.Frame(self.root, bg="#f0f4f7")
        button_frame.pack(pady=10)
        
        # Add File Button
        add_file_button = tk.Button(
            button_frame,
            text="Add Files",
            command= self.add_files,
            bg="#007bff",
            fg="white",
            font=("Arial", 12),
            padx=10,
            pady=5,
        )
        add_file_button.pack(side="left", padx=5)

        # Remove File Button
        remove_file_button = tk.Button(
            button_frame,
            text="Remove Selected",
            command=self.remove_selected,
            bg="#dc3545",
            fg="white",
            font=("Arial", 12),
            padx=10,
            pady=5,
        )
        remove_file_button.pack(side="left", padx=5)

        # Merge PDFs Button
        merge_button = tk.Button(
            self.root,
            text="Merge PDFs",
            command=self.merge_pdfs,
            bg="#28a745",
            fg="white",
            font=("Arial", 14),
            padx=20,
            pady=10,
        )
        merge_button.pack(pady=20)
        
    
    def add_files(self):
        files = filedialog.askopenfilenames(
            filetypes=[("PDF Files", "*.pdf")], title="Select PDF files"
        )
        
        for file in files:
            if file not in self.pdf_files:
                self.pdf_files.append(file)
                self.listbox.insert(tk.END, file)
    
    def remove_selected(self):
        selected_indices = self.listbox.curselection()
        for index in reversed(selected_indices):
            self.pdf_files.pop(index)
            self.listbox.delete(index)
    
    def merge_pdfs(self):
        if not self.pdf_files:
            messagebox.showwarning("No Files","Please add at least two PDF files to merge.")
            return
        
        save_path = filedialog.asksaveasfilename(
            defaultextension=".pdf",
            filetypes=[("PDF Files", "*.pdf")],
            title="Save Merged PDF As",
        )
        if not save_path:
            return
        
        try:
            merger = PdfMerger()
            for pdf_file in self.pdf_files:
                merger.append(pdf_file)
                
            merger.write(save_path)
            merger.close()
            messagebox.showinfo("Success", f"Merged PDF saved to:\n{save_path}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while merging PDFs:\n{e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = PDFMergerApp(root)
    root.mainloop()
