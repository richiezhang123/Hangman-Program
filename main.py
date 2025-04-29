from tkinter import *

names = []
words = []

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
        Hangman(root)

if __name__ == "__main__":
    root = Tk()
    root.title("Hangman")
    hangman_instance = MenuPage(root)
    root.mainloop()
