""" 
work flow 
input from user 
computer choice ( computer will choose randomly not conditionally )
result print 

cases:
A rock
rock - rock = tie 
rock -paper = paper win 
rock - scissor = rock win
B paper
paper - rock = paper win
paper - paper = tie
paper - scissor = scissor win
C scissor
scissor - rock = rock win
scissor - paper = scissor win
scissor - scissor = tie
"""
import random 
item_list = ["Rock ", "Paper ", " Scissor "]
name = input ("Enter Your Name"  )
user_choice = input (f"Enter Your Choice {name} (Rock , Paper , Scissor ) ")
computer_choice = random.choice(item_list)
print(f"{name} choice is {user_choice} and computer choice is {computer_choice}")
if  user_choice== computer_choice:
    print("Tie")
elif user_choice == "Rock ":
    if computer_choice == "Paper ":
        
      print(f"{name} WINS !!!!!!!")
    else:
        print("Computer WINS !!!!!!!")
elif user_choice == "Paper ":
    if computer_choice == "Scissor ":
        print("Computer WINS !!!!!!!")
    else:
        print(f"{name} WINS !!!!!!!")
elif user_choice == "Scissor ":
    if computer_choice == "Rock ":
        print("Computer WINS !!!!!!!")
    else:
        print(f"{name} WINS !!!!!!!")
else:
    print("Invalid choice, please choose Rock, Paper, or Scissor.")
