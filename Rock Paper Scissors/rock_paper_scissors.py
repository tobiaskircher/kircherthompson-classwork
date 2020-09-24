# [a,b] a = computer, b = user
# 0 = rock, 1 = paper , 2 = scissors

import random

def rock():
    print("\nRock selected")
    global options
    options[1]=0
#end procedure

def paper():
    print("\nPaper selected")
    global options
    options[1]=1
#end procedure

def scissors():
    print("\nScissors selected")
    global options
    options[1]=2
#end procedure

def tie():
    print("It's a tie!")
#end procedure
    
def not_tie():
    global user_win
    {
    True: user_win_f,
    False: computer_win_f,
    }[user_win]()
#end procedure

def user_win_f():
    print("User Wins!")
#end procedure

def computer_win_f():
    print("Computer Wins!")
#end procedure

def computer_rock():
    print("Computer picks rock")
#end procedure

def computer_paper():
    print("Computer picks paper")
#end procedure

def computer_scissors():
    print("Computer picks scissors")
#end procedure


options = ["",""]
tie_combos = [[0, 0],[1, 1],[2, 2]]
user_win_combos = [[0, 1],[1, 2],[2, 0]]
computer_option = random.randint(0,2)
options[0]=computer_option

user_option = input('''Type your option below:
rock
paper
scissors
>''').lower()
try:
    {
     'rock':rock,
     'paper':paper,
     'scissors':scissors,
    }[user_option]()

    {
     0:computer_rock,
     1:computer_paper,
     2:computer_scissors,
    }[computer_option]()


    ties = options in tie_combos
    user_win = options in user_win_combos

    print("\n")

    {
    True: tie,
    False: not_tie,
    }[ties]()
except:
    print("\nInvalid input.")
