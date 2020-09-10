valid = False

while not valid: 
    try:
        number = int(input("Number:"))
        rows = int(input("Rows:"))
    except:
        print("\nError: you did not input an integer.\n")
    else:
        if not 0<number<21 or not 0<rows<21:
            print("\nError: Number and rows must be between 1 and 20.\n")

        else:
            if input("\nType Y to confirm your options, or N to cancel:").upper()=="Y":
                valid = True
            else:
                print("\nSelection cancelled.\n")
            #end if
        #end if
    #end try
#end while
                
print("\n")
for i in range(1,rows+1):
    answer = number*i
    print(number,"x",i,"is",answer)
#next i
