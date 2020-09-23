#!/usr/bin/python
# -*- coding: utf-8 -*-


def displayMenu():
    valid = False
    print('\nMenu:')
    print('1. Add Name')
    print('2. Display List')
    print('3. Quit')
    while not valid:
        try:
            choice = int(input('\nEnter choice:'))
        except:
            print('That was not an integer.')
        else:
            if choice > 0 and choice < 4:
                valid = True
            else:
                print('Invalid input, Enter a number between 1 and 3.')

        # end if
    # end while

    return choice


# end procedure

def addName(theList):
    name = input('\nEnter the name to be added to the list:')
    try:
        position = int(input('Enter the position in the list to insert the number (1-10):'))
    except:
        print("Error, you did not input an integer...")
    else:  
        theList[position-1] = name


# end procedure

def displayList(theList):
    print("\n")
    for i in range(0, 10):
        print(str(i+1) + ' ' + str(theList[i]))


    # next i
# end procedure

theList = [''] * 10

end = False
print(theList)
while not end:
    choice = displayMenu()

    if choice == 1:
        addName(theList)
    elif choice == 2:
        displayList(theList)
    else:
        print('\nProgram terminating...')
        end = True

# end switch
# end while
