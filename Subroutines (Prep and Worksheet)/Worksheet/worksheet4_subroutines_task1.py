def multiples(table,start_num,end_num,pupil_name):
    print("Hi,",pupil_name,"... here is your times table.")
    for i in range(start_num,end_num+1):
        total = table*i
        print(table,"x",i,"=",total)
    # next i
# end procedure

name = input("What is your name?")
table = int(input("Enter times table:"))
start_num = int(input("Enter start number:"))
end_num = int(input("Enter end number:"))
multiples(table,start_num,end_num,name)
