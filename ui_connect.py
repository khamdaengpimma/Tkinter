from tkinter import*
import mysql.connector
from tkinter import messagebox

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="vocabularydatabase"
)
mycursor = mydb.cursor()


root =Tk()
root.title("MySql_Connect")
root.geometry("500x500")


# label_vocabulary =Label(root, text="Vocabulary:")
# label_vocabulary.pack()
# entry_vocabulary =Entry(root)
# entry_vocabulary.pack()

# label_genre =Label(root, text="Genre:")
# genre_var = StringVar()
# genre_var.set("Select Genre")
# genre_option_menu = OptionMenu(root, genre_var, "None", "noun", "verb", "adjective", "adverb", "preposition","preposition","pronoun")
root.mainloop()