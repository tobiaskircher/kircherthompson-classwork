def calc(n):
    if n == 0: return 1 #base case/terminating condition
    elif n < 0: return "N/A"
    else:
        return n * calc(n-1)
    #end if
#end function

n = int(input("Enter number:"))
recursion = calc(n)
print(recursion)
