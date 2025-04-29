from tkinter import *
import random


names = []
words = [
    "Apple",
    "Banana",
    "Candle",
    "Mystery",
    "Elephant",
    "Jazz",
    "Keyboard",
    "Whisper",
    "Oxygen",
    "Pizza",
    "Galaxy",
    "Avalanche",
    "Crocodile",
    "Quicksand",
    "Notebook",
    "Bicycle",
    "Volcano",
    "Igloo",
    "Wizard",
    "Triangle",
    "Sphinx",
    "Horizon",
    "Puzzle",
    "Robot",
    "Thunder"
]

display_word= []
guess_word = words[random.randint(0,25)]
for i in guess_word:
    display_word.append("_")

print(guess_word)

class MenuPage:
    def __init__(self, parent):
        self.quiz_frame= Frame(parent, padx = 100, pady = 100)
        self.quiz_frame.grid()

        self.heading_label = Label(self.quiz_frame, text="HANGMAN", font=("Tw Cen Mt", "36", "bold"))
        self.heading_label.grid()

        self.user_label = Label(self.quiz_frame,text="Enter your username:", font=("Tw Cen Mt", "16"))
        self.user_label.grid()

        self.entry_box = Entry(self.quiz_frame)
        self.entry_box.grid()

        self.continue_button = Button(self.quiz_frame, text = "Continue", command = self.name_collection)
        self.continue_button.grid()

    def name_collection(self):
        global name
        name = self.entry_box.get()
        names.append(name)
        self.quiz_frame.destroy()
        HangmanMain(root)

class HangmanMain:
    def __init__(self, parent):
        
        self.quiz_frame= Frame(parent, padx = 100, pady = 100)
        self.quiz_frame.grid()
        
        self.guess_word = Label(self.quiz_frame, text = display_word,font=("Tw Cen Mt", "36", "bold") )
        self.guess_word.grid()

        self.letter_entry = Entry(self.quiz_frame)
        self.letter_entry.grid()

        self.guess_button = Button(self.quiz_frame, text = "GUESS", command = check_letter)
        self.guess_button.grid()

    def check_letter(self):
        global user_guess
        user_guess = self.letter_entry.get()
        if user_guess in guess_word






if __name__ == "__main__":
    root = Tk()
    root.title("Hangman")
    hangman_instance = MenuPage(root)
    root.mainloop()
