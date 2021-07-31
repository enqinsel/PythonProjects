import random
import sys
user_score = 0
computer_score = 0

while True:
    user = input("Rock ? Paper ? Scissors ? (Press 'q' to exit) : ")
    choice = ["Rock" , "Paper" , "Scissors"]
    computer = random.choice(choice)
    if user == "q":
        print("\n!!Logged Out!!")
        sys.exit()
    if user.title() == "Rock":
        if computer == "Rock":
            print("\nNobody Won!" , "\nComputer Score: " , computer_score , "\nUser Score: " , user_score)
        elif computer == "Paper":
            print("\nComputer's Result: ",computer)
            computer_score +=1
            print("Computer Won!" , "\nComputer Score: " , computer_score , "\nUser Score: " , user_score)
        elif computer == "Scissors":
            print("\nComputer's Result: ",computer)
            user_score +=1
            print("You Won!" , "\nComputer Score: " , computer_score , "\nUser Score: " , user_score)
    elif user.title() == "Paper":
        if computer == "Rock":
            print("\nComputer's Result: ",computer)
            user_score +=1
            print("You Won!" , "\nComputer Score: " , computer_score , "\nUser Score: " , user_score)
        elif computer == "Paper":
            print("\nComputer's Result: ",computer)
            print("Nobody Won!" , "\nComputer Score: " , computer_score , "\nUser Score: " , user_score)
        elif computer == "Scissors":
            print("\nComputer's Result: ",computer)
            computer_score +=1
            print("Computer Won!" , "\nComputer Score: " , computer_score , "\nUser Score: " , user_score)
    elif user.title() == "Scissors":
        if computer == "Rock":
            print("\nComputer's Result: ",computer)
            computer_score +=1
            print("Computer Won" , "\nComputer Score: " , computer_score , "\nUser Score: " , user_score)
        elif computer == "Paper":
            print("\nComputer's Result: ",computer)
            user_score +=1
            print("You Won" , "\nComputer Score: " , computer_score , "\nUser Score: " , user_score)
        elif computer == "Scissors":
            print("\nComputer's Result: ",computer)
            print("Nobody Won!" , "\nComputer Score: " , computer_score , "\nUser Score: " , user_score)
    if user_score or computer_score == 3:
        if user_score == 3:
            print("\n************************************\nCongratulations, You Won The Game!" , "\nComputer Score: " , computer_score , "\nUser Score: " , user_score)
            break
        elif computer_score == 3:
            print("\n************************************\nSorry, Computer Won The Game!" , "\nComputer Score: " , computer_score , "\nUser Score: " , user_score)
            break

