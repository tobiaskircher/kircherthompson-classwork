def multiples(table, start_num, end_num, pupil_name):
	print("Hi, "+ pupil_name + " … here is your times table")
	for i in range(start_num, end_num + 1,table):
		print(table, " x " , i , " = " , i)
	#next i 
#end procedure

print("What is your name?")
pupil_name = input()
valid = False
while not valid:
    try:
        print("Enter times table, start number and end number:")
        table = int(input())
        start_num = int(input())
        end_num = int(input())
    except:
        print("Please only input integers.")
    else:
        valid = True
multiples(table, start_num, end_num, pupil_name)
