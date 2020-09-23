year = int(input("Please input a year:"))
leapyear = False
if(year%4==0):
    leapyear= True
#endif
if(year%100==0):
    leapyear=False
#endif
if(year%400==0):
    leapyear=True
#endif
if leapyear==True:
    print(year,"is a leap year.")
else:
    print(year,"is not a leap year.")
    
