'''=================== H A N D    C R I C K E T     G A M E ======================'''

import random

player_run = 0
system_run = 0
choice = 0

def player_input():
    global player_run
    while(1):
        player_run=int(input("Enter the number : "))
        if(player_run>=0 and player_run<=6):
            break
        print("Enter Numbers between 0 and 6")

def system_input():
    global system_run
    list=[0,1,2,3,4,5,6]
    system_run=random.choice(list)

def player_batting(choice,player_score,system_score):
    while(1):
        player_input()
        system_input()
        print(">>>player run :",player_run)
        print(">>>system run :",system_run)
        if(player_run==system_run):
            print(" # # # PLAYER OUT # # # ")
            break
        else:
            player_score=player_score+player_run
            print("Updated score:",player_score)
            if(((choice==2) and (player_score>system_score)) or ((choice==1) and (system_score>player_score))):
                break
            print("-----------------")
    return player_score,system_score

def player_bowling(choice,player_score,system_score):
    while(1):
        player_input()
        system_input()
        print(">>>system run :",system_run)
        print(">>>player run :",player_run)
        if((player_run==system_run)):
            print(" # # # SYSTEM OUT # # # ")
            break
        else:
            system_score=system_score+system_run
            print("Updated score:",system_score)
            if (((choice==1) and (system_score>player_score)) or ((choice==2) and (player_score>system_score))):
                break
            print("-----------------")
    return player_score,system_score

def display(player_score,system_score):
    print("--------======== SCORE BOARD =========---------")
    print("Total Score By Player:",player_score)
    print("Total Score By system:",system_score)
    print("----------------------------------------")
    if(player_score>system_score):
        print("***You win by",player_score-system_score,"runs***")
    elif(player_score==system_score):
        print("***DRAW MATCH***")
    else:
        print("***You lost by",system_score-player_score,"runs***")
    print("--------=========================---------")

def main_f():
    print("1:Batting\n2.Bowling\n3.exit")
    try:
        player_score=0
        system_score=0
        choice=int(input("Enter your choice:"))
        if(choice==1):
            print("========FIRST INNINGS:PLAYER BATS FIRST========")
            (player_score,system_score)=player_batting(1,player_score,system_score)
            print("-----------------------------------------------")
            print("Total Score By Player:",player_score)
            print("system need",player_score+1,"runs to win")
            print("=========SECOND INNINGS:SYSTEM TAKES BATTING NOW========")
            (player_score,system_score)=player_bowling(1,player_score,system_score)
        elif(choice==2):
            print("========FIRST INNINGS:SYSTEM BATS FIRST========")
            (player_score,system_score)=player_bowling(2,player_score,system_score)
            print("-----------------------------------------------")
            print("Total Score By system:",system_score)
            print("player need",system_score+1,"runs to win")
            print("=========SECOND INNINGS:PLAYER TAKES BATTING NOW========")
            (player_score,system_score)=player_batting(2,player_score,system_score)
        elif(choice==3):
            exit()
        else:
            print("Enter the correct choice")
            main_f()
        display(player_score,system_score)
        option=input("Do you want to continue(yes/no):")
        if(option=='yes'):
            main_f()
        else:
            exit()
    except Exception as E:
        print(E, "is the exception")

try:
    while 1:
        main_f()
except Exception as E:
    print(E,"is the Exception")
