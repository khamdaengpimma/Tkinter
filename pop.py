from tkinter import *
import mysql.connector
from tkinter import messagebox

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="vocabularydatabase"
)
mycursor = mydb.cursor()


# Create an instance of tkinter frame
root = Tk()
# Define geometry of the window
root.geometry("400x350")



def popupwin():
    def add_vocabulary():
        vocabulary = vocabulary_entry.get()
        genre = genre_var.get()
        topic = topic_entry.get()
        meaning = meaning_entry.get()

        try:
            # Insert the vocabulary word into the database
            sql = "INSERT INTO vocabulary (Vocabulary, Genre, Topic, Meaning) VALUES (%s, %s, %s, %s)"
            values = (vocabulary, genre, topic, meaning)
            mycursor.execute(sql, values)
            mydb.commit()
            messagebox.showinfo("Thêm từ vựng thành công")
        except mysql.connector.Error as err:
            messagebox.showerror("Đã tồn tại", f"Error: {err}")
    top = Toplevel(root)
    top.geometry("500x500")
    top.title("Add Vocabulary")

    label_vocabulary = Label(top, text="Vocabulary:",fg="green",font=("Roboto 10 bold"))
    vocabulary_entry = Entry(top)

    label_genre = Label(top, text="Genre:",fg="green",font=("Roboto 10 bold"))
    genre_var = StringVar()
    genre_var.set("None")
    genre_option_menu = OptionMenu(top,genre_var, "None", "noun", "verb", "adjective", "adverb", "preposition", "pronoun")

    label_topic = Label(top, text="Topic:",font=("Roboto 10 bold"))
    topic_entry = Entry(top)

    label_meaning = Label(top, text="Meaning:",font=("Roboto 10 bold"))
    meaning_entry = Text(top, height = 10,
                width = 25,)

    # Create a button to add vocabulary
    button_add = Button(top, text="Add Vocabulary", command=add_vocabulary,width=15,height=2, font=("Roboto 10 bold"))

    # Pack widgets onto the window
    label_vocabulary.pack()
    vocabulary_entry.pack()
    label_genre.pack()
    genre_option_menu.pack()
    label_topic.pack()
    topic_entry.pack()
    label_meaning.pack()
    meaning_entry.pack()
    button_add.pack(pady=10)

# Create a Label
toplabel = Label(root, text="Bâm vào Nút để Thêm từ vựng", font=('Roboto 15 bold'))
toplabel.pack(pady=20)
# Create a Button
button = Button(root, text="Thêm từ vựng", command=popupwin, bg="light cyan", font=('Roboto 20 bold'))
button.pack(pady=20)

root.mainloop()
