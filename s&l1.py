#import random package to have a random value in snake and ladder game
import random
count=0   #initial value to begin with the game
while (count<=100): #frame a loop
    roll=input('Press Z to roll the dice') #make a player active 
    if (roll=='Z'): # define 
        r=random.randint(1,6)
        count=count+r
        print('Your Lucky value is',r) #lucky value in each roll
        print('Now be at',count)#final count after each play
        if count==8:
            count==37
            print('Take Upstairs to',count)
        elif count==11:
            count==2
            print('Sin! So sorry',count)
        elif count==13: #ladder climb
            count==34
            print('Take Upstairs to',count)
        elif count==25: #snake bite
            count==4
            print('Sin! So sorry',count)
        elif count==38:
            count==9
            print('Sin! So sorry',count)
        elif count==40:
            count==68
            print('Take Upstairs to',count)
        elif count==52:
            count==81
            print('Take Upstairs to',count)
        elif count==65:
            count==46
            print('Sin! So sorry',count)
        elif count==76:
            count==97
            print('Take Upstairs to',count)
        elif count==89:
            count==70
            print('Sin! So sorry',count)
        elif count==93:
            count==64
            print('Sin! So sorry',count)
        elif (count>100): # define where to stay if you exceeds 100
            count=count-r
            print('Stay Back at',count)
        else: #define win and terminate the game
            if count==100:
                print('CONGO! You won the game.Party....')
                break 
