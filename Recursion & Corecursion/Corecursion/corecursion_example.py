def add(x,y):
    while(y>0):
        x+=1
        print("x:",x)
        y-=1
        print("y:",y,"\n")
    return x

num1 = int(input("Number 1:"))
num2 = int(input("Number 2:"))
print("\n")
print(add(num1,num2))
