from tkinter import *
import random

window = Tk()
window.title("Rock, Paper, Scissors")
window.geometry('300x200')

score_player = 0
score_cpu = 0
p1_pick = ''
cpu_pick = ''
result_text = ''
choices = ['rock', 'paper', 'scissors']
rules = {
    'scissorspaper': 'scissors',
    'scissorsrock': 'rock',
    'paperrock': 'paper'
}
game_text = Label(window, text=("""
Welcome!
Pick: Rock, paper scissors.
"""))
game_text.grid(column=5, row=0, rowspan=5)


def calc_winner():
    global score_player, score_cpu, cpu_pick, result_text
    cpu_pick = (random.choice(choices))

    if p1_pick + cpu_pick in rules or cpu_pick + p1_pick in rules:
        winner = rules.get(p1_pick + cpu_pick) or rules.get(cpu_pick + p1_pick)
        if p1_pick == winner:
            result_text = 'You win!'
            score_player += 1
            return score_player
        elif cpu_pick == winner:
            result_text = 'CPU wins!'
            score_cpu += 1
            return score_cpu

    elif p1_pick == cpu_pick:
        result_text = "It's a draw!"
    else:
        print('error')


def score_update():
    global game_text
    game_text.configure(text='')
    game_text = Label(window, width=20, text=(f"""
    You picked {p1_pick}
    CPU picked {cpu_pick}

    {result_text}

    *** Score ***
    You: {score_player}
    CPU: {score_cpu}
    """))

    game_text.grid(column=5, row=0, rowspan=5)


def rock_clicked():
    global p1_pick
    p1_pick = 'rock'
    calc_winner()
    score_update()


def paper_clicked():
    global p1_pick
    p1_pick = 'paper'
    calc_winner()
    score_update()


def scissors_clicked():
    global p1_pick
    p1_pick = 'scissors'
    calc_winner()
    score_update()


rock_button = Button(window, text="Rock", command=rock_clicked, width=10, pady=15)
paper_button = Button(window, text="Paper", command=paper_clicked, width=10, pady=15)
scissors_button = Button(window, text="Scissors", command=scissors_clicked, width=10, pady=15)
quit_button = Button(window, text="Quit", command=window.destroy)

rock_button.grid(column=1, row=1)
paper_button.grid(column=1, row=2)
scissors_button.grid(column=1, row=3)
quit_button.grid(column=1, row=4)

window.mainloop()
