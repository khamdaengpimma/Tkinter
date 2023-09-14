from tkinter import * 
def button_click(event):
    text = event.widget.cget("text")

    if text == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, END)
            entry.insert(END, str(result))
        except Exception as e:
            entry.delete(0, END)
            entry.insert(END, "Error")

    elif text == "C":
        entry.delete(0, END)

    else:
        entry.insert(END, text)

root =Tk()
root.title("Calculator")



# Entry field
entry = Entry(root, font="Helvetica 20 bold", justify="right",fg='Blue')
entry.pack(fill=BOTH, expand=True)
# Your name label
your_name_label = Label(root, text="Khamdaeng",font="Helvetica 15 bold",fg="red")
your_name_label.pack()

# Buttons
button_frame = Frame(root)
button_frame.pack()

button_texts = [
    ("**", 0, 0), ("//", 0, 1), ("C", 0, 2), ("+", 0, 3),
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), ("%", 4, 1), (".", 4, 2), ("=", 4, 3)
]

for (text, row, col) in button_texts:
    button = Button(button_frame, text=text, font="Helvetica 15 bold",fg="blue", padx=30, pady=10)
    button.grid(row=row, column=col)
    button.bind("<Button-1>", button_click)

root.mainloop()
