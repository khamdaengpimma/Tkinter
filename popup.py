#Import the required library
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

def close_win(top):
    top.destroy()

def add_vocabulary(vocabulary,genre,topic,meaning):
    print("what")
    vocabulary = vocabulary
    genre = genre
    topic = topic
    meaning = meaning

    try:
        # Insert the vocabulary word into the database
        sql = "INSERT INTO vocabulary (Vocabulary, Genre, Topic, Meaning) VALUES (%s, %s, %s, %s)"
        values = (vocabulary, genre, topic, meaning)
        mycursor.execute(sql, values)
        mydb.commit()
        messagebox.showinfo("Success", "vocabulary word added successfully")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")
    
#Create an instance of tkinter frame
root= Tk()
#Define geometry of the window
root.geometry("500x500")

def popupwin():
    top= Toplevel(root)
    top.geometry("500x500")
    label_vocabulary = Label(top, text="Vocabulary:")
    vocabulary = Entry(top)

    label_genre = Label(top, text="Genre:")
    genre= StringVar()
    genre.set("Select Genre")
    genre_option_menu = OptionMenu(top, genre, "None", "noun", "verb", "adjective", "adverb", "preposition","preposition","pronoun")

    label_topic = Label(top, text="Topic:")
    topic = Entry(top)

    label_meaning = Label(top, text="Meaning:")
    meaning = Entry(top)

    # Create a button to add vocabulary
    button_add = Button(top, text="Add",command=add_vocabulary(vocabulary.get(),genre.get(),topic.get(),meaning.get()))
    # Pack widgets onto the window
    label_vocabulary.pack()
    vocabulary.pack()
    label_genre.pack()
    genre_option_menu.pack()
    label_topic.pack()
    topic.pack()
    label_meaning.pack()
    meaning.pack()
    button_add.pack()


#Create a Label
toplabel = Label(root,text="Bâm vào Nút đé Thêm từ vựng",fg="blue", font= ('Roboto 20 bold'))
toplabel.pack(pady=20)
#Create a Button
button= Button(root, text= "Thêm từ vựng", command= popupwin, font= ('Roboto 20 bold'))
button.pack(pady=20)
root.mainloop()