#userinput = input("prompt>")
#print("This is how you print stuff")

# Rahul, Make me Rock, Paper, Scissors
import random

print("This is the rps game")
numofgames = raw_input("How many games do you want to play?")
numofgames = int(numofgames)
currentgame = 1
while currentgame <= numofgames:

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
  elif playerselection == "paper" and computerselection == "paper":
    print("we tied, I chose paper")
  elif playerselection == "scissors" and computerselection == "paper":
    print("You win, I chose paper")
  elif playerselection == "rock" and computerselection == "scissors":
    print("you win, I chose scissors")
  elif playerselection == "paper" and computerselection == "scissors":
    print("I win, I chose scissors")
  elif playerselection == "scissors" and computerselection == "scissors":
    print("we tied, I chose scissors")
  elif playerselection == "rock" and computerselection == "rock":
    print("we tied, I chose rock")
  elif playerselection == "paper" and computerselection == "rock":
    print("you win, I chose rock")
  elif playerselection == "scissors" and computerselection == "rock":
    print("I win, I chose rock")
  currentgame = currentgame + 1
