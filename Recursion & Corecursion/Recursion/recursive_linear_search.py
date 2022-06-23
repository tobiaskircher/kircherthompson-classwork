#recursive linear search


the_list = [1,3,4,5,7,12,16,7]

def linear_search(numbers,item,pointer=0):
    if len(numbers)==0:
        return -1
    elif numbers[0] == item:
        return pointer
    else:
        return linear_search(numbers[1:],item,pointer+1)



print(linear_search(the_list,3))
