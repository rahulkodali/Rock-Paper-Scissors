#userinput = input("prompt>")
#print("This is how you print stuff")

# Rahul, Make me Rock, Paper, Scissors
import random

print("This is the rpc game")
playerselection = raw_input("Do you want rock, paper, or scissors?")

computerselection = random.randint(0, 2)
if computerselection == 0:
  computerselection = "rock"
elif computerselection == 1:
  computerselection = "paper"
elif computerselection == 2:
  computerselection = "scissors"

if playerselection == "rock" and computerselection == "paper":
  print("I win, I chose paper")
