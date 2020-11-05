class Dog():
    def __init__(self, myName,myColour):
        self.__name = myName
        self.__colour = myColour
    #end procedure

    def bark(self, barkTimes):
        for i in range(barkTimes):
            print("Woof!")
        #next i
    #end procedure

    def get_colour(self):
        return self.__colour
    #end procedure

    def set_colour(self, newColour):
        self.__colour = newColour
    #end procedure

    def get_name(self):
        return self.__name
    #end procedure
    
#end class

dog1 = Dog("Harry","White")
print(dog1._Dog__name) #accessing hidden variables
print(dog1.get_name())
print(dog1.get_colour())
dog1.bark(2)

