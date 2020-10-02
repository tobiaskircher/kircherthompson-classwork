def calc(n):
    if n == 0:
        return 0
    else:
        return n + calc(n-2)
    #end if
#end function

number = int(input("Number:"))
if number < 0 or number%2!=0:
    print("Invalid number.")
else:
    number = calc(number)
    print(number)
