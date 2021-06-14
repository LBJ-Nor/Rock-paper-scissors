# ver 1.1

import random

score_player = 0
score_cpu = 0
choices = ['rock', 'paper', 'scissors']
rules = {
    'scissorspaper': 'scissors',
    'scissorsrock': 'rock',
    'paperrock': 'paper'
        }


def player_choose():
    while True:
        print('Rock, Paper, Scissors (R, P, S)')
        user_input = input('Choose: ').lower()
        if user_input == 'r':
            user_input = 'rock'
        elif user_input == 'p':
            user_input = 'paper'
        elif user_input == 's':
            user_input = 'scissors'

        if user_input not in choices:
            print('Invalid choice. Try again')
        else:
            return user_input

def calc_winner():
    global score_player, score_cpu

    if p1_pick + cpu_pick in rules or cpu_pick + p1_pick in rules:
        winner = rules.get(p1_pick + cpu_pick) or rules.get(cpu_pick + p1_pick)
        if p1_pick == winner:
            print('You win!')
            score_player += 1
            return score_player
        else:
            print('CPU wins!')
            score_cpu += 1
            return score_cpu
    else:
        print("Draw!")


# Game loop
while True:
    p1_pick = player_choose()
    cpu_pick = random.choice(choices)
    print()
    print('You picked ' + p1_pick)
    print('CPU picked ' + cpu_pick)
    calc_winner()

    print(f"""
    *** Score ***
    You: {score_player}
    CPU: {score_cpu}
    """)
