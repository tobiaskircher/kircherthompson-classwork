print('''Select one of the following options:
Enter A for Multipy
Enter B for Divide
Enter C for Add
Enter D for Subtract
Enter E for Remainder Division''')

option = input("Option:")
no1 = int(input("Enter your first number:"))
no2 = int(input("Enter your second number:"))
answer=""
if option=="A":
    answer = no1*no2
elif option=="B":
    answer = no1/no2
elif option=="C":
    answer = no1+no2
elif option=="D":
    answer=no1-no2
elif option=="E":
    answer = no1%no2
print(answer)
