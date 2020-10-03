import time
fibonacci = []
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1)+fib(n-2)
    #end if
#end function
def fib2(n):
    for i in range(n):
        fibonacci.append(fib(i))
    #next i
#end procedure
    
time1 = time.time()
fib2(20)
time2 = time.time()
print(time2-time1)
print(fibonacci)

#works faster  
