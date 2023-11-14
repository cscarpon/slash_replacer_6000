import tkinter as tk
from tkinter import messagebox

def replace_slashes():
    input_text = text_input.get("1.0", tk.END)
    modified_text = input_text.replace("\\", "/")
    text_input.delete("1.0", tk.END)
    text_input.insert(tk.END, modified_text)

def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(text_input.get("1.0", tk.END).strip())
    messagebox.showinfo("Copied", "Text copied to clipboard!")

def clear_text():
    text_input.delete("1.0", tk.END)

root = tk.Tk()
root.title("The Slash Replacer 6000")

text_input = tk.Text(root, height=10, width=50)
text_input.pack()

replace_button = tk.Button(root, text="Replace Slashes", command=replace_slashes)
replace_button.pack()

copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.pack()

clear_button = tk.Button(root, text="Clear", command=clear_text)
clear_button.pack()

root.mainloop()
