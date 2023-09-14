from tkinter import *

# Define the global variables
expression = ""

# Define the functions
def press(number):
    global expression
    expression += number
    display.update()

def clear():
    global expression
    expression = ""
    display.update()

def equal():
    global expression

    try:
        result = eval(expression)
        expression = str(result)
    except:
        expression = "Invalid Expression"

    display.update()

# Create the main window
window = Tk()
window.title("Calculator")

# Create the display
display = Label(window, text=expression, font=("Arial", 16))
display.grid(row=0, column=0, columnspan=4)

# Create the buttons
button_1 = Button(window, text="1", command=lambda: press("1"))
button_1.grid(row=1, column=0)

button_2 = Button(window, text="2", command=lambda: press("2"))
button_2.grid(row=1, column=1)

button_3 = Button(window, text="3", command=lambda: press("3"))
button_3.grid(row=1, column=2)

button_4 = Button(window, text="4", command=lambda: press("4"))
button_4.grid(row=2, column=0)

button_5 = Button(window, text="5", command=lambda: press("5"))
button_5.grid(row=2, column=1)

button_6 = Button(window, text="6", command=lambda: press("6"))
button_6.grid(row=2, column=2)

button_7 = Button(window, text="7", command=lambda: press("7"))
button_7.grid(row=3, column=0)

button_8 = Button(window, text="8", command=lambda: press("8"))
button_8.grid(row=3, column=1)

button_9 = Button(window, text="9", command=lambda: press("9"))
button_9.grid(row=3, column=2)

button_0 = Button(window, text="0", command=lambda: press("0"))
button_0.grid(row=4, column=0)

button_clear = Button(window, text="C", command=clear)
button_clear.grid(row=4, column=1)

button_equal = Button(window, text="=", command=equal)
button_equal.grid(row=4, column=2)

# Start the main loop
window.mainloop()
