import tkinter as tk
from tkinter import filedialog, messagebox
from src.huffman import HuffmanCoding
from src.file_handler import FileHandler
import os

class HuffmanGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Huffman Compressor")
        self.huffman = HuffmanCoding()
        self.setup_gui()

    def setup_gui(self):
        """Set up the Tkinter GUI."""
        tk.Label(self.root, text="Huffman Compression Tool", font=("Arial", 16)).pack(pady=10)

        # File selection
        self.file_path_var = tk.StringVar()
        tk.Label(self.root, text="Selected File:").pack()
        tk.Entry(self.root, textvariable=self.file_path_var, width=50).pack(pady=5)
        tk.Button(self.root, text="Browse", command=self.browse_file).pack()

        # Buttons for compress/decompress
        tk.Button(self.root, text="Compress", command=self.compress_file).pack(pady=5)
        tk.Button(self.root, text="Decompress", command=self.decompress_file).pack(pady=5)

    def browse_file(self):
        """Open file dialog to select a file."""
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("Compressed files", "*.zip"), ("All files", "*.*")])
        if file_path:
            self.file_path_var.set(file_path)

    def compress_file(self):
        """Compress the selected file."""
        file_path = self.file_path_var.get()
        if not file_path or not os.path.exists(file_path):
            messagebox.showerror("Error", "Please select a valid file.")
            return
        try:
            text = FileHandler.read_file(file_path)
            encoded, tree = self.huffman.encode(text)
            output_path = os.path.splitext(file_path)[0] + ".zip"
            FileHandler.save_compressed(output_path, encoded, tree)
            messagebox.showinfo("Success", f"File compressed to {output_path}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def decompress_file(self):
        """Decompress the selected file."""
        file_path = self.file_path_var.get()
        if not file_path or not file_path.endswith(".zip"):
            messagebox.showerror("Error", "Please select a valid .zip file.")
            return
        try:
            encoded, tree = FileHandler.load_compressed(file_path)
            decoded = self.huffman.decode(encoded, tree)
            output_path = os.path.splitext(file_path)[0] + "_decompressed.txt"
            FileHandler.write_file(output_path, decoded)
            messagebox.showinfo("Success", f"File decompressed to {output_path}")
        except Exception as e:
            messagebox.showerror("Error", str(e))