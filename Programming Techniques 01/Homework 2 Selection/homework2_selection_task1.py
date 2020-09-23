window = "closed"
temp = int(input("Enter the temperature:"))
humidity = int(input("Enter the humidity:"))
if window == "closed":
    if temp > 25 or humidity > 50:
        print("Open the window.")
    #end if
else:
    if temp < 10 or humidity > 50:
        print("Close the window")
    #endif
#endif
    
