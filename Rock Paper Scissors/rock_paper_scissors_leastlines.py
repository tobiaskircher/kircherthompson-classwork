### SRC - This is a great effort!
### But, too many ifs and I don't like
### Multiple assignments!
import random
while input("\nPlay Rock Paper Scissors? [Y/N]").lower()=="y":
    try:
        computer,player,wins = random.randint(0,2),int(input("\nEnter 1 (Rock), 2 (Paper)or 3 (Scissors):")),[[0, 1],[1, 2],[2, 0]]
        selection,combination=["rock","paper","scissors"],[computer,player-1]
        print("\nYou chose: "+str(selection[player-1]).upper()+"\nThe computer chose: "+str(selection[computer]).upper())
        print("You win!") if combination in wins else (print("It's a tie!") if combination[0]==combination[1] else print("You lose!"))
    except: print("\nInvalid Input!")
