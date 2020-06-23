from tkinter import *
from tkinter import messagebox
from tkinter.font import Font
import wikipedia


def get_answer():
    entered_string = entry.get()
    answer_text.delete(1.0, END)
    try:
        answer_value = wikipedia.summary(entered_string)
        answer_text.insert(INSERT, answer_value)
    except:
        answer_text.insert(INSERT, "Please check your input or fix your internet connection")


def about_message():
    messagebox.showinfo("About", "This is a mini search app that displays a brief summary about almost any topic or "
                                 "person or any thing you can think of.\nIt requires internet connection as this "
                                 "application uses Wikipedia as database.\nThis Application in made in python3 using Tkinter")


def about_me():
    messagebox.showinfo("About Developer", "Hi my name is Lakshay Aggarwal\nGithub : https://github.com/ProNoob25 ")


def quit_message():
    answer = messagebox.askquestion("Conformation Required", "Are your sure you want to quit")
    if answer.lower() == "yes":
        root.quit()


root = Tk()
root.title("Mini Search App")
root.config(bg='#3a2315')
my_font = Font(family="Segoe UI", size=14)

top_frame = Frame(root, bg='#3a2315')

main_menu = Menu(root)
root.config(menu=main_menu)
about_menu = Menu(main_menu)
about_menu.add_command(label="About the Application", command=about_message)
about_menu.add_command(label="About the Developer", command=about_me)
main_menu.add_cascade(label="About", menu=about_menu)
main_menu.add_command(label="Exit", command=quit_message)

entry = Entry(top_frame, font=my_font)
search_button = Button(top_frame, text="Search", command=get_answer)

entry.pack()
search_button.pack(pady=2)
top_frame.pack(side=LEFT, padx=5)

bottom_frame = Frame(root)

scroll_answer = Scrollbar(bottom_frame, orient=VERTICAL)
answer_text = Text(bottom_frame, yscrollcommand=scroll_answer.set, wrap=WORD, font=my_font, fg='#231ec9', padx=5)
scroll_answer.config(command=answer_text.yview)
scroll_answer.pack(side=RIGHT, fill=Y)
answer_text.pack()

bottom_frame.pack()

root.resizable(False, False)
root.mainloop()
