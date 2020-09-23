if input("Type Y if you have a temperature:")=="Y":
    if input("Type Y if you have a sore throat:")=="Y":
        print("You may have a throat infection.")
    elif input("Type Y if you have a cough:")=="Y":
        print("You may have a chest infection.")
    else:
        print("You may have a fever.")
    #end if
else:
    print("You seem to be fine. If there are any other problems please see a doctor.")
    
