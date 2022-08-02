"""
Title: Rock, Paper, Scissors
Minimalistic version.
"""

import random

def main():
    win_conditions = "rockpaperscissorsrock"
    choices = ["rock", "paper", "scissors"]
    cpu = random.choice(choices)

    p1 = input("Rock, Paper, Scissors: ").lower().strip()
    while p1 not in choices:
        print("Invalid choice, try again!")
        p1 = input("Rock, Paper, Scissors: ").lower().strip()

    print(f"CPU picked: {cpu}")

    if p1 == cpu:
        print("Draw!")
    elif p1+cpu in win_conditions:
        print("CPU wins!")
    else:
        print("Player wins!")
        
if __name__ == "__main__":
    main()

