"""
A quick programme to play the game Rock, Paper, Scissors!
"""

from random import randint
from time import sleep

options = ['R','P','S']

player_loss = "You Lost!"
player_win = "You Win!"

def decide_winner(user_choice, computer_choice):
  print "You chose %s" % user_choice
  print"Computer selecting..."
  sleep(1)
  print "Computer chose %s" % computer_choice
  user_choice_index = options.index(user_choice)
  computer_choice_index = options.index(computer_choice)

  if user_choice_index == computer_choice_index:
    print "It's a tie!"
  elif user_choice_index == 0 and computer_choice_index == 2:
   	print player_win
  elif user_choice_index == 1 and computer_choice_index == 0 :
    print player_win
  elif user_choice_index == 2 and computer_choice_index == 1 :
 	print player_win
  elif user_choice_index >2 :
    print "Not valid!"
    return
  else :
   	print player_loss


def play_RPS():
  print "Rock, Paper or Scissors?"
  user_choice = raw_input("Select R for Rock, P for Paper or S for Scissors: ")
  user_choice = user_choice.upper()
  computer_choice = options[randint(0,len(options)-1)]
  decide_winner(user_choice, computer_choice)


play_RPS()
