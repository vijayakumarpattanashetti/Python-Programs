# rock,paper,scissors game
import random #get the random package
import sys
z=["rock","paper","scissors"] #list the options for player 
c=0
while c<=4: #construct the loop to continue the game
    a=random.choice(z) #define range for random no. generation
    player=input("rock, paper, scissors?")
    c=c+1
    if player==a:
        print("Draw")
    elif player=="rock":
        if a=="paper":
            print("U Lost,", a, "covers", player)
        else:
            print("U Won,", player, "smashes", a)
    elif player=="paper":
        if a=="scissors":
            print("U Lost,", a, "cut", player)
        else:
            print("U Won,", player, "covers", a)
    elif player=="scissors":
        if a=="rock":
            print("U Lost,", a, "smashes", player)
        else:
            print("U Won,", player, "cut", a)
    elif player=="Quit":
        print("Thanks for playing with me")
        sys.exit()
    else:
        print("Invalid choice,plz... try again")
   
