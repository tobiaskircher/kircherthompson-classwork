import json

with open('leaderboard.json', 'r') as f:
    leaderboard = json.load(f)

running = True
while running:
    option = input('''Options: 
1. Print Leaderboard 
2. Add/Update Leaderboard 
3. Exit
>''')

    if option.isdigit() and 1 <= int(option) <= 3:
        
        option = int(option)
        print("")

        if option == 1:
            sorted_leaderboard = {k: v for k, v in sorted(leaderboard.items(), key=lambda item: item[1], reverse=True)}
            print("LEADERBOARD:\n")
            count = 0
            for i in sorted_leaderboard:
                count += 1
                print(i+": "+str(sorted_leaderboard[i]))

        elif option == 2:    
            name = input('Name: ').lower()
            score = int(input('Score: '))

            if not name in leaderboard or leaderboard[name] < score:
                leaderboard[name] = score

            with open('leaderboard.json', 'w') as f:
                json.dump(leaderboard,f)

        elif option == 3:
            running = False
            
    print("")



