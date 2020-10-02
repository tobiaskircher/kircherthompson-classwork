import time
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1)+fib(n-2)
    #end if
#end function

def fibonacci2(n):
    fibNumbers = [0,1]
    for i in range(2,n):
        fibNumbers.append(fibNumbers[i-1]+fibNumbers[i-2])
    #next i
    return fibNumbers

time1 = time.time()
print(fib(10))
time2 = time.time()
print(fib(20))
time3 = time.time()
print("Recursion 10 and 20:")
print(time2-time1)
print(time3-time2)
print("\n")
time1 = time.time()
print(fibonacci2(10))
time2 = time.time()
print(fibonacci2(20))
time3 = time.time()
print("For Loop 10 and 20:")
print(time2-time1)
print(time3-time2)
