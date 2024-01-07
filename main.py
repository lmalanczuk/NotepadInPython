import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

def save_file():
    file_path = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if not file_path:
        return
    with open(file_path, "w") as file_output:
        text = text_edit.get(1.0, tk.END)
        file_output.write(text)
    root.title(f"NOTEPAD - {file_path}")

def open_file():
    file_path = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not file_path:
        return
    text_edit.delete(1.0, tk.END)
    with open(file_path, "r") as file_input:
        text = file_input.read()
        text_edit.insert(tk.END, text)
    root.title(f"NOTEPAD - {file_path}")


root = tk.Tk()

root.title("NOTEPAD")
root.rowconfigure(0, minsize=800)
root.columnconfigure(1, minsize=800)

text_edit = tk.Text(root)
text_edit.grid(row=0, column=1, sticky="nsew")

frame_button = tk.Frame(root, relief=tk.RAISED, bd=3)
frame_button.grid(row=0, column=0, sticky="ns")

button_open = tk.Button(frame_button, text="Open File", command=open_file)
button_open.grid(row=0, column=0, padx=5, pady=5)
button_save = tk.Button(frame_button, text="Save File", command=save_file)
button_save.grid(row=1, column=0, padx=5, pady=5)



root.mainloop()
