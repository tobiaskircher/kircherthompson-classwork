#Software Development Homework 2, Q2

import random

def check_valid(barcode):
    
    total = barcode[0] + barcode[2] + barcode[4] + (3 * (barcode[1]+barcode[3]))
    check_digit = total % 10
    
    if barcode[5] == check_digit:
        return True
    else:
        return False
    

for i in range(100):
    barcode = [random.randint(0,9) for z in range(6)]
    barcode_string = "".join(str(x) for x in barcode)
    print(barcode)
    print(check_valid(barcode))
    
