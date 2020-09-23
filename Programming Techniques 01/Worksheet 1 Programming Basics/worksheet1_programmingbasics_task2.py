width = int(input("Enter the width of the room:"))
length = int(input("Enter the length of the room:"))
height = int(input("Enter the height of the room:"))
coats = int(input("Enter the coats of the room:"))

unpaintable_width = int(input("Enter the width of unpaintable areas:"))
unpaintable_length = int(input("Enter the length of unpaintable areas:"))
unpaintable_height = int(input("Enter the height of unpaintable areas:"))

area = (length*width)+(2*length*width)+(2*width*height)
unpaintable_area = unpaintable_width*unpaintable_length*unpaintable_height
area -= unpaintable_area
area *= coats
litres = area / 11
litres = round(litres,2)
print(str(litres)+" litres are required.")
