import tkinter as tk
from src.gui import HuffmanGUI

if __name__ == "__main__":
    root = tk.Tk()
    app = HuffmanGUI(root)
    root.geometry("600x300")
    root.mainloop()