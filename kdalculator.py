import tkinter as tk
def button_click(event):
    text = event.widget.cget("text")

    if text == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")

    elif text == "C":
        entry.delete(0, tk.END)

    else:
        entry.insert(tk.END, text)

root = tk.Tk()
root.title("Calculator")



# Entry field
entry = tk.Entry(root, font="Helvetica 20 bold", justify="right")
entry.pack(fill=tk.BOTH, expand=True)
# Your name label
your_name_label = tk.Label(root, text="Khamdaeng")
your_name_label.pack()

# Buttons
button_frame = tk.Frame(root)
button_frame.pack()

button_texts = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), ("C", 4, 1), ("=", 4, 2), ("+", 4, 3)
]

for (text, row, col) in button_texts:
    button = tk.Button(button_frame, text=text, font="Helvetica 20 bold", padx=20, pady=20)
    button.grid(row=row, column=col)
    button.bind("<Button-1>", button_click)

root.mainloop()
