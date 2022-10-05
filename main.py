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

# Write your code below this line 👇

import random

human = input("What do you choose? Type 0 for Rock, 1 for paper or 2 for Scissors.")
human = int(human)
computer = random.randint(0, 2)

# if human == 0:
#   print(rock)
#   if computer == 0:
#     print("Computer chose: ")
#     print(rock)
#     print(" you are same")
#   elif computer == 1:
#     print("Computer chose: ")
#     print(paper)
#     print("you lose")
#   elif computer == 2:
#     print("Computer chose: ")
#     print(scissors)
#     print("you win")

# elif human == 1:
#   print(paper)
#   if computer == 0:
#     print("Computer chose: ")
#     print(rock)
#     print(" you win")
#   elif computer == 1:
#     print("Computer chose: ")
#     print(paper)
#     print("you are same")
#   elif computer == 2:
#     print("Computer chose: ")
#     print(scissors)
#     print("you lose")
# elif human == 2:
#   print(scissors)
#   if computer == 0:
#     print("Computer chose: ")
#     print(rock)
#     print(" you lose")
#   elif computer == 1:
#     print("Computer chose: ")
#     print(paper)
#     print("you win")
#   elif computer == 2:
#     print("Computer chose: ")
#     print(scissors)
#     print("you are same")


# other good methord

image = [rock, paper, scissors]
result = ["you win!", "You lose", "You draw", "you tyed an invalid number, You lose"]

if human > 2 or human < 0:
    print(result[3])

else:
    print(image[human])
    print("The computer chose:")
    print(image[computer])

    if (human == 0 and computer == 2) or human > computer:
        print(result[0])
    elif human == computer:
        print(result[2])
    else:
        print(result[1])