for loop in range(int(input())): #T number of test cases
    n,k,p= [int(num) for num in (input().split())]
    stacks = []
    for i in range(n):
        stacks.append([int(x) for x in(input().split())])
        print(stacks)
        
