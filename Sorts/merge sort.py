#merge sort 
import math

def merge_sort(numbers):
    list1 = numbers[:len(numbers)//2]
    print(list1)
    list2 = numbers[len(numbers)//2:]
    print(list2)
    print(len(list1))
    if len(list1) > 2:
        merge_sort(list1)
        merge_sort(list2)
    else:
        print("stopped")
        new_list = []
        while len(list1) > 0 or len(list2) > 0:
            if list1[0] <= list2[0] or len(list2) == 0:
                new_list.append(list1[0])
                list1.pop(0)
            elif list2[0] <= list1[0] or len(list1) == 0:
                new_list.append(list2[0])
                list2.pop(0)

        print(new_list)











numbers = [2,5,1,2,9,8,3,7]
merge_sort(numbers)
