import time, random

def bubble_sort(bubble_list):
    print(bubble_list)
    no_swaps = False
    time_start = time.time()
    while not no_swaps:
        count = 0
        no_swaps = True
        for i in range(len(bubble_list)-1):
            if bubble_list[count] > bubble_list[count + 1]:
                temp1 = bubble_list[count]
                temp2 = bubble_list[count + 1]
                bubble_list[count] = temp2
                bubble_list[count + 1] = temp1
                no_swaps = False
            #end if
            count += 1
            #next i
        #end for
    #end while
    time_taken = round(time.time() - time_start, 3) 

    print(bubble_list)
    print(str(time_taken) + " seconds.")
#end function    


def insertion_sort(insertion_list):
    print(insertion_list)
    time_start = time.time()
    for i in range(1,len(insertion_list)):
        item = insertion_list[i]
        previous_index = i - 1
        while item < insertion_list[previous_index] and previous_index >= 0:
            insertion_list[previous_index + 1] = insertion_list[previous_index]
            previous_index -= 1
        #end while
        insertion_list[previous_index + 1] = item
        #next i
    #end for
        
    time_taken = round(time.time() - time_start, 3)
    print(insertion_list)
    print(str(time_taken) + " seconds.")
#end function   
    

the_list = []
for i in range(10000):
    the_list.append(random.randint(0,1000))

    #next i
#end for
                    
print(the_list)
bubble_list = the_list[:]
insertion_list = the_list[:]
print("Bubble sort:")
bubble_sort(insertion_list)
print("\nInsertion sort:")
insertion_sort(bubble_list)

