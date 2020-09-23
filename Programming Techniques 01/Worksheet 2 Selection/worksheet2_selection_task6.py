print('''1. Economy Car
2. Saloon Car
3. Sports Car''')
option = int(input("Enter the number of the car you would like to choose:"))
if 0<option<4:
    valid = True
else:
    valid = False
    print("Option Invalid.")
#end if

if valid == True:
    if input("Type Y to confirm your response:")=="Y":
        print("Have a nice day.")
    else:
        print("Selection cancelled.")
    #end if
#end if
