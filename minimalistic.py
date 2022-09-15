import random

choices = ["rock", "paper", "scissors"]
cpu = random.choice(choices)

while (p1 := input("Rock, Paper, Scissors: ").lower()) not in choices:
    print("Invalid choice, try again!")

print(f"CPU picked: {cpu}")

if p1 == cpu:
    print("Draw!")
elif p1+cpu in "rockpaperscissorsrock":
    print("CPU wins!")
else:
    print("Player wins!")
