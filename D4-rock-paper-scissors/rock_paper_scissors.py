import random

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

choices = [rock, paper, scissors]

print("Welcome to Rock, Paper, Scissors!")
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
computer_choice = random.randint(0, 2)

if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number. You lose!")
elif user_choice == 0 and computer_choice == 2:
    print(f"You chose:\n{rock}\nComputer chose:\n{scissors}\nYou win!")
elif user_choice == 2 and computer_choice == 0:
    print(f"You chose:\n{scissors}\nComputer chose:\n{rock}\nYou lose!")
elif user_choice == computer_choice:
    print(f"You chose:\n{choices[user_choice]}\nComputer chose:\n{choices[computer_choice]}\nIt's a draw!")
elif user_choice > computer_choice:
    print(f"You chose:\n{choices[user_choice]}\nComputer chose:\n{choices[computer_choice]}\nYou win!")
else:
    print(f"You chose:\n{choices[user_choice]}\nComputer chose:\n{choices[computer_choice]}\nYou lose!")