
import tkinter as tk
from tkinter import filedialog, messagebox
from pypdf import PdfWriter


class PDFMergerApp:

    def __init__(self, root):
        self.root = root
        self.root.title("PDF Merger App")
        self.root.geometry("760x550")
        self.root.minsize(620, 450)

        self.files = []

        # Main heading
        heading = tk.Label(
            root,
            text="PDF MERGER",
            font=("Arial", 22, "bold")
        )
        heading.pack(pady=15)

        subtitle = tk.Label(
            root,
            text="Select multiple PDF files and merge them into one",
            font=("Arial", 10)
        )
        subtitle.pack(pady=2)

        # PDF list
        list_frame = tk.Frame(root)
        list_frame.pack(fill="both", expand=True, padx=20, pady=15)

        self.file_listbox = tk.Listbox(
            list_frame,
            font=("Arial", 11),
            selectmode=tk.SINGLE,
            height=12
        )
        self.file_listbox.pack(
            side="left",
            fill="both",
            expand=True
        )

        scrollbar = tk.Scrollbar(
            list_frame,
            orient="vertical",
            command=self.file_listbox.yview
        )
        scrollbar.pack(side="right", fill="y")

        self.file_listbox.config(
            yscrollcommand=scrollbar.set
        )

        # Buttons
        button_frame = tk.Frame(root)
        button_frame.pack(pady=8)

        tk.Button(
            button_frame,
            text="Add PDFs",
            width=13,
            command=self.add_files
        ).grid(row=0, column=0, padx=5, pady=5)

        tk.Button(
            button_frame,
            text="Remove Selected",
            width=15,
            command=self.remove_selected
        ).grid(row=0, column=1, padx=5, pady=5)

        tk.Button(
            button_frame,
            text="Move Up",
            width=10,
            command=lambda: self.move_file(-1)
        ).grid(row=0, column=2, padx=5, pady=5)

        tk.Button(
            button_frame,
            text="Move Down",
            width=10,
            command=lambda: self.move_file(1)
        ).grid(row=0, column=3, padx=5, pady=5)

        tk.Button(
            button_frame,
            text="Clear All",
            width=13,
            command=self.clear_all
        ).grid(row=1, column=0, padx=5, pady=5)

        tk.Button(
            button_frame,
            text="Merge PDFs",
            width=20,
            command=self.merge_pdfs,
            bg="green",
            fg="white",
            font=("Arial", 11, "bold")
        ).grid(row=1, column=1, columnspan=3, padx=5, pady=8)

        # Status
        self.status_label = tk.Label(
            root,
            text="No PDF files selected",
            font=("Arial", 10)
        )
        self.status_label.pack(pady=10)

    def add_files(self):
        selected_files = filedialog.askopenfilenames(
            title="Select PDF Files",
            filetypes=[("PDF Files", "*.pdf")]
        )

        for file_path in selected_files:
            if file_path not in self.files:
                self.files.append(file_path)

        self.refresh_list()

    def refresh_list(self):
        self.file_listbox.delete(0, tk.END)

        for index, file_path in enumerate(self.files, start=1):
            self.file_listbox.insert(
                tk.END,
                f"{index}. {file_path.split('/')[-1].split(chr(92))[-1]}"
            )

        self.status_label.config(
            text=f"Total PDF files selected: {len(self.files)}"
        )

    def remove_selected(self):
        selected_index = self.file_listbox.curselection()

        if not selected_index:
            messagebox.showwarning(
                "Warning",
                "Please select a PDF file to remove."
            )
            return

        self.files.pop(selected_index[0])
        self.refresh_list()

    def move_file(self, direction):
        selected_index = self.file_listbox.curselection()

        if not selected_index:
            messagebox.showwarning(
                "Warning",
                "Please select a PDF file first."
            )
            return

        old_index = selected_index[0]
        new_index = old_index + direction

        if new_index < 0 or new_index >= len(self.files):
            return

        self.files[old_index], self.files[new_index] = (
            self.files[new_index],
            self.files[old_index]
        )

        self.refresh_list()
        self.file_listbox.selection_set(new_index)
        self.file_listbox.activate(new_index)

    def clear_all(self):
        if not self.files:
            messagebox.showinfo(
                "Information",
                "The PDF list is already empty."
            )
            return

        confirm = messagebox.askyesno(
            "Confirm",
            "Are you sure you want to remove all PDF files?"
        )

        if confirm:
            self.files.clear()
            self.refresh_list()

    def merge_pdfs(self):
        if len(self.files) < 2:
            messagebox.showwarning(
                "Warning",
                "Please select at least 2 PDF files!"
            )
            return

        output_file = filedialog.asksaveasfilename(
            title="Save Merged PDF",
            defaultextension=".pdf",
            filetypes=[("PDF Files", "*.pdf")],
            initialfile="merged_pdf.pdf"
        )

        if not output_file:
            return

        # Prevent overwriting one of the source files
        if output_file in self.files:
            messagebox.showerror(
                "Error",
                "Please choose a different output file name."
            )
            return

        writer = PdfWriter()

        try:
            for pdf_file in self.files:
                writer.append(pdf_file)

            with open(output_file, "wb") as output:
                writer.write(output)

            messagebox.showinfo(
                "Success",
                f"PDF files merged successfully!\n\nSaved to:\n{output_file}"
            )

            self.status_label.config(
                text="PDF merging completed successfully!"
            )

        except Exception as error:
            messagebox.showerror(
                "Error",
                f"Could not merge PDF files.\n\nDetails:\n{error}"
            )

        finally:
            writer.close()


if __name__ == "__main__":
    root = tk.Tk()
    app = PDFMergerApp(root)
    root.mainloop()

