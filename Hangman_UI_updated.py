from tkinter import *
import re
from io import StringIO
import sys
import time

window = Tk()
window.title("Hangman")
window.geometry('400x400')


class hangman:
    def __init__(self):
        self.num_chance = 100
        self.entry = ''
        self.guess_word = "RAMIFICATION"
        self.used_words = []
        self.list_var = []
        self.regex = re.compile('[@_!#$%^&*()<>?/\|}{}]')

    def clicked(self, label2, bt):
        label2.place(x=125, y=170)

        while True:
            def get_value(event):
                self.entry = e1.get()
                def start_game(self):
                    self.choice = e2.get()
                    # print(self.used_words)
                    # if self.choice in self.used_words :
                    #     print("\n\tThis Choice is already entered  before! ")
                try:
                    print(self.used_words)
                    self.entry = int(self.entry)
                    e1.place_forget()
                    bt.place_forget()
                    label3.place_forget()
                    label_text = StringVar()
                    label_text1 = StringVar()
                    label_text2 = StringVar()
                    label_text3 = StringVar()
                    label_text.set("You have " + str(self.entry) + " chances!!")
                    label_text1.set("You have a word of %d Characters!" % len(self.guess_word))
                    Label(window, textvariable=label_text, font=("Arial Bold", 8)).place(x=120, y=220)
                    Label(window, textvariable=label_text1, font=("Arial Bold", 8)).place(x=120, y=240)
                    for i in range(len(self.guess_word)):
                        self.list_var.append("_")
                    old_stdout = sys.stdout
                    result = StringIO()
                    sys.stdout = result
                    print(*self.list_var, sep=' ')
                    result_string = result.getvalue()
                    sys.stdout = old_stdout
                    label_text2.set("Your New word now is : \n\n %s" % result_string)
                    Label(window, textvariable=label_text2, font=("Arial Bold", 8)).place(x=120, y=280)
                    time.sleep(1)
                    label_text3.set("Enter your Character : ")
                    Label(window, textvariable=label_text3, font=("Arial Bold", 8)).place(x=120, y=300)
                    e2 = Entry(window)
                    e2.place(x=140, y=320)
                    e2.bind('<Return>', start_game)

                except ValueError:
                    print("\n\tPlease Enter only Numbers!!")
                    pop = Toplevel()
                    pop.geometry('300x100')
                    msg = Message(pop, text="Please Enter only Numbers!!", width=200)
                    msg.place(x=70, y=10)
                    button = Button(pop, text="Ok", command=pop.destroy, width=10)
                    button.place(x=100, y=50)

            label3 = Label(window, text="Please Enter the number of Chances you would like to take :",
                           font=("Arial Bold", 8))
            label3.place(x=25, y=200)

            e1 = Entry(window)
            e1.place(x=140, y=250)
            e1.bind('<Return>', get_value)
            break


obj1 = hangman()
label = Label(window, text="Welcome To", font=("Arial Bold", 20)).place(x=110, y=25)
label1 = Label(window, text="Hangman", font=("Arial Bold", 20)).place(x=128, y=75)
label2 = Label(window, text="The Game begins!!", font=("Arial Bold", 10))
bt = Button(window, text="Play", command=lambda: obj1.clicked(label2, bt), width=10)

bt.place(x=150, y=125)

window.mainloop()