from tkinter import *
from tkinter import messagebox
import tkinter as tk
import random

# hidden parameters
count_of_try = 3
random_num = random.randint(1, 11)


# functions
def rules():
    messagebox.showinfo("Rules", """
I guessed number between 1 and 10. You need to answered right number with 3 trying.
Sure, I will help you little
Are you ready?

Let`s go""")


def the_game():
    global count_of_try
    global text
    global random_num

    count_of_try -= 1
    guess = int(user_answer.get())
    if guess == random_num:
        text.set("You WIN!")
        check_button.pack_forget()

    elif count_of_try == 0:
        text.set(f"You have {count_of_try} attempts... You loose")
        check_button.pack_forget()

    elif guess < random_num:
        text.set(f"No! Your number is smaller. You have {str(count_of_try)} attempts remaining")

    elif guess > random_num:
        text.set(f"No! Your number is bigger. You have {str(count_of_try)} attempts remaining")


# main window
root = tk.Tk()

# Settings of window
root.title("Number Guesser")
root.geometry("600x400")
root["bg"] = "turquoise"
root.resizable(width=False, height=False)

#  welcome
hello = Label(root, text="Hello! Its my new game: \"Number guesser\"", font="Arial 15 bold", bg="white", fg="black")
hello.pack(side=TOP, pady=10)

start = Label(root, text="Try to guess below: ", font="Arial 12", bg="white", fg="black")
start.pack()

# Result info
text = StringVar()
text.set("You have 3 attempts remaining!")

guess_attempts = Label(root, textvariable=text)
guess_attempts.pack(pady=20)

# user answer
user_answer = Entry(root, width=20, borderwidth=4, bg="white", fg="black", font="Arial 14")
user_answer.pack(side=LEFT, padx=60)

# button to check result
check_button = Button(root, text="Check", activebackground="yellow", padx=40, pady=10, command=the_game)
check_button.pack(side=LEFT)

# exit button
exit_button = Button(root, text="Exit", activebackground="red", padx=50, pady=10, command=root.quit)
exit_button.pack(side=BOTTOM, pady=5)

# notification of rules
rules_button = Button(root, text="Rules", activebackground="blue", padx=50, pady=10, command=rules)
rules_button.pack(side=BOTTOM, pady=5)

# Opening of window
root.mainloop()
