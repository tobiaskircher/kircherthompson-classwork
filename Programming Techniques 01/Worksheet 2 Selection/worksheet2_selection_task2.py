total = int(input("Input total value of your order:"))
if input("Type Y if you would like to pay £5 for guaranteed next day delivery:")=="Y":
    total+=5
    postage = 5
else:
    if total < 15:
        total+=3.5
        postage = 3.5
    else:
        postage = 0
print("Your overall charge is: £",total,"which includes a £",postage," shipping fee.")
