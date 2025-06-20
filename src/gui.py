import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
from src.huffman import HuffmanCoding
from src.file_handler import FileHandler
import os

class HuffmanGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("ZIP-ZONE")
        self.huffman = HuffmanCoding()
        self.setup_gui()

    def setup_gui(self):
        """Set up the Tkinter GUI with enhanced styling."""
        # Apply a modern theme
        style = ttk.Style()
        style.theme_use('clam')  # Modern theme
        style.configure('TButton', font=('Arial', 12), padding=10)
        style.configure('TLabel', font=('Arial', 12))
        style.configure('TEntry', font=('Arial', 12))

        # Main frame for better organization
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Title
        ttk.Label(main_frame, text="Huffman Compression Tool", font=("Arial", 16, "bold")).pack(pady=10)

        # File selection
        self.file_path_var = tk.StringVar()
        ttk.Label(main_frame, text="Selected File:").pack(anchor="w")
        file_entry = ttk.Entry(main_frame, textvariable=self.file_path_var, width=50)
        file_entry.pack(pady=5, fill=tk.X)
        ttk.Button(main_frame, text="Browse", command=self.browse_file).pack(pady=5)

        # Buttons for compress/decompress
        button_frame = ttk.Frame(main_frame)
        button_frame.pack(pady=10)
        ttk.Button(button_frame, text="Compress", command=self.compress_file, style='Accent.TButton').pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Decompress", command=self.decompress_file, style='Accent.TButton').pack(side=tk.LEFT, padx=5)

        # Status label
        self.status_var = tk.StringVar()
        ttk.Label(main_frame, textvariable=self.status_var, font=("Arial", 10, "italic"), foreground="gray").pack(pady=10)

        # Configure button style for hover effect
        style.configure('Accent.TButton', background='#4CAF50', foreground='white')
        style.map('Accent.TButton', background=[('active', '#45a049')])

    def browse_file(self):
        """Open file dialog to select a file."""
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.pdf"), ("Compressed files", "*.zip"), ("All files", "*.*")])
        if file_path:
            self.file_path_var.set(file_path)
            self.status_var.set(f"Selected: {os.path.basename(file_path)}")

    def compress_file(self):
        """Compress the selected file."""
        file_path = self.file_path_var.get()
        if not file_path or not os.path.exists(file_path):
            self.status_var.set("Error: Please select a valid file.")
            messagebox.showerror("Error", "Please select a valid file.")
            return
        try:
            text = FileHandler.read_file(file_path)
            encoded, tree = self.huffman.encode(text)
            output_path = os.path.splitext(file_path)[0] + ".zip"
            FileHandler.save_compressed(output_path, encoded, tree)
            self.status_var.set(f"Success: File compressed to {os.path.basename(output_path)}")
            messagebox.showinfo("Success", f"File compressed to {output_path}")
        except Exception as e:
            self.status_var.set(f"Error: {str(e)}")
            messagebox.showerror("Error", str(e))

    def decompress_file(self):
        """Decompress the selected file."""
        file_path = self.file_path_var.get()
        if not file_path or not file_path.endswith(".zip"):
            self.status_var.set("Error: Please select a valid .zip file.")
            messagebox.showerror("Error", "Please select a valid .zip file.")
            return
        try:
            encoded, tree = FileHandler.load_compressed(file_path)
            decoded = self.huffman.decode(encoded, tree)
            output_path = os.path.splitext(file_path)[0] + "_decompressed.txt"
            FileHandler.write_file(output_path, decoded)
            self.status_var.set(f"Success: File decompressed to {os.path.basename(output_path)}")
            messagebox.showinfo("Success", f"File decompressed to {output_path}")
        except Exception as e:
            self.status_var.set(f"Error: {str(e)}")
            messagebox.showerror("Error", str(e))