import tkinter as tk
from tkinter import messagebox
import mysql.connector

# Create a connection to the MySQL database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="vocabularydatabase"
)

# Create the Vocabulary table if it doesn't exist
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE IF NOT EXISTS vocabulary (VocabularyID INT AUTO_INCREMENT PRIMARY KEY, Vocabulary VARCHAR(255) NOT NULL, Genre VARCHAR(255), Topic VARCHAR(255), Meaning TEXT NOT NULL)")

# Function to add a vocabulary word to the database
def add_vocabulary():
    vocabulary = entry_vocabulary.get()
    genre = genre_var.get()
    topic = entry_topic.get()
    meaning = entry_meaning.get()

    try:
        # Insert the vocabulary word into the database
        sql = "INSERT INTO vocabulary (Vocabulary, Genre, Topic, Meaning) VALUES (%s, %s, %s, %s)"
        values = (vocabulary, genre, topic, meaning)
        mycursor.execute(sql, values)
        mydb.commit()
        messagebox.showinfo("Success", "vocabulary word added successfully")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")

# Create the main tkinter window
window = tk.Tk()
window.title("Vocabulary Entry")

# Create labels and entry fields
label_vocabulary = tk.Label(window, text="Vocabulary:")
entry_vocabulary = tk.Entry(window)

label_genre = tk.Label(window, text="Genre:")
genre_var = tk.StringVar()
genre_var.set("Select Genre")
genre_option_menu = tk.OptionMenu(window, genre_var, "None", "noun", "verb", "adjective", "adverb", "preposition","preposition","pronoun")

label_topic = tk.Label(window, text="Topic:")
entry_topic = tk.Entry(window)

label_meaning = tk.Label(window, text="Meaning:")
entry_meaning = tk.Entry(window)

# Create a button to add vocabulary
button_add = tk.Button(window, text="Add Vocabulary", command=add_vocabulary)

# Pack widgets onto the window
label_vocabulary.pack()
entry_vocabulary.pack()
label_genre.pack()
genre_option_menu.pack()
label_topic.pack()
entry_topic.pack()
label_meaning.pack()
entry_meaning.pack()
button_add.pack()

# Start the tkinter main loop
window.mainloop()
