import random
win_conditions = "rockpaperscissorsrock"
choices = ["rock", "paper", "scissors"]
cpu = random.choice(choices)

p1 = input("Rock, Paper, Scissors: ").lower()
while p1 not in choices:
    print("Invalid choice, try again!")
    p1 = input("Rock, Paper, Scissors: ").lower()

print(f"CPU picked: {cpu}")

if p1 == cpu:
    print("Draw!")
elif p1+cpu in win_conditions:
    print("CPU wins!")
else:
    print("Player wins!")
