import tkinter as tk

def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        result.set(num1 + num2)
    except ValueError:
        result.set("Error: Invalid input")

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Add your name label
name_label = tk.Label(root, text="Your Name")
name_label.pack()

# Create entry fields for numbers
entry_num1 = tk.Entry(root, width=10)
entry_num2 = tk.Entry(root, width=10)

entry_num1.pack()
entry_num2.pack()

# Create a button to perform the calculation
calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.pack()

# Variable to store the result
result = tk.StringVar()
result.set("Result: ")

# Label to display the result
result_label = tk.Label(root, textvariable=result)
result_label.pack()

root.mainloop()
