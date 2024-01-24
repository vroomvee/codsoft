from tkinter import *
import random

# for a win=2, for a loss=0, for a draw=1
rules = {"ROCK": {"ROCK": 1, "PAPER": 0, "SCISSORS": 2},
         "PAPER": {"ROCK": 2, "PAPER": 1, "SCISSORS": 0},
         "SCISSORS": {"ROCK": 0, "PAPER": 2, "SCISSORS": 1}}

ps = 0
cs = 0


def logic(choice):
    global ps, cs
    outcomes = ["ROCK", "PAPER", "SCISSORS"]
    random_num = random.randint(0, 2)
    comp_choice = outcomes[random_num]
    result = rules[choice][comp_choice]
    comp_c.config(text="Computer Choice: " + str(comp_choice))

    if result == 2:
        ps = ps + 1
        score.config(text="Your Score: " + str(ps))
        winner.config(text="YOU WON!", fg="brown")
    elif result == 1:
        winner.config(text="DRAW.", fg="brown")
    else:
        cs = cs + 1
        comp.config(text="Computer: " + str(cs))
        winner.config(text="YOU LOST :(", fg="brown")


root = Tk()
root.title("ROCK PAPER SCISSORS")

choice_label = Label(root, text="Welcome to the game!", width=18, height=2, font=("Chalkduster", 14), fg="brown")
choice_label.grid(row=0, sticky=N, padx=200, pady=10)

Label(root, text="Please select an option:", font=("Chalkduster", 14)).grid(row=1, sticky=N)

score = Label(root, text="Your Score: 0", font=("Chalkduster", 10), fg="brown")
score.grid(row=2, sticky=W)

comp = Label(root, text="Computer: 0", font=("chalkduster", 10), fg="brown")
comp.grid(row=2, sticky=E)

player_c = Label(root, text="Player Choice:", font=("Chalkduster", 12))
player_c.grid(row=3, sticky=W)

comp_c = Label(root, font=("Chalkduster", 12))
comp_c.grid(row=3, sticky=E)

winner = Label(root, font=("Chalkduster", 14))
winner.grid(row=3, sticky=N)

Button(root, text="ROCK", width=10, command=lambda: logic("ROCK")).grid(row=5, sticky=W, padx=5, pady=5)
Button(root, text="PAPER", width=10, command=lambda: logic("PAPER")).grid(row=5, sticky=N, padx=5, pady=5)
Button(root, text="SCISSORS", width=10, command=lambda: logic("SCISSORS")).grid(row=5, sticky=E, padx=5, pady=5)
Label(root).grid(row=6)

root.mainloop()



