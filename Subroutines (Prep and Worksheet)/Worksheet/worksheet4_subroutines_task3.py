def getPassword(attempt):
    valid = False
    while not valid:
        if attempt == 1:
            print("Enter password:")
        else:
            print("Enter password again:")
        #end if
        password = input(">")
        if 6<=len(password)<=8:
            valid = True
        #endif
    #endwhile
    return password

password = getPassword(1)
