rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random
image=[rock,paper,scissors]
player_choice=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
computer_choice=random.randint(0,2)
if player_choice>=0 and player_choice<=2:
    print("Player Choose",image[player_choice])
print("Computer Choose",image[computer_choice])
if player_choice==computer_choice:
    print("It's a TIE")
else:
    if player_choice==0:
        if computer_choice==1:
            print("Computer Wins")
        elif computer_choice==2:
            print("Player Wins")
    if player_choice==1:
        if computer_choice==0:
            print("Player Wins")
        elif computer_choice==2:
            print("Computer Wins")
    if player_choice==2:
        if computer_choice==0:
            print("Computer Wins")
        elif computer_choice==1:
            print("Player Wins")