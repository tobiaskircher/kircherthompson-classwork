largest = "a"
smallest = "z"
for i in range(5):
    letter = input("Enter letter:")
    if letter > largest:
        largest = letter
    #endif
    if letter < smallest:
        smallest = letter
    #endif
#next i
print("Smallest:",smallest)
print("Largest:",largest)
