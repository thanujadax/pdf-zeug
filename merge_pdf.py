import tkinter as tk
from tkinter import filedialog, simpledialog
from PyPDF2 import PdfMerger

def merge_pdfs(pdf_list, output_path):
    merger = PdfMerger()
    for pdf in pdf_list:
        merger.append(pdf)
    merger.write(output_path)
    merger.close()

def main():
    # Create the root window
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    # Ask the user how many PDFs to merge
    num_pdfs = simpledialog.askinteger("Input", "How many PDFs do you want to merge?", minvalue=2)

    # List to hold selected PDF files
    pdf_files = []

    # Ask the user to select each PDF file
    for i in range(num_pdfs):
        file_path = filedialog.askopenfilename(
            title=f"Select PDF file {i + 1}",
            filetypes=[("PDF files", "*.pdf")],
        )
        if file_path:
            pdf_files.append(file_path)
        else:
            tk.messagebox.showerror("Error", "You must select a file.")
            return

    # Ask for the output file location
    output_path = filedialog.asksaveasfilename(
        title="Save merged PDF as",
        defaultextension=".pdf",
        filetypes=[("PDF files", "*.pdf")],
    )

    if output_path:
        merge_pdfs(pdf_files, output_path)
        tk.messagebox.showinfo("Success", "PDFs merged successfully!")
    else:
        tk.messagebox.showerror("Error", "You must specify an output file.")

if __name__ == "__main__":
    main()
